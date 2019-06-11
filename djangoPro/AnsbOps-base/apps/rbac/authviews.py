import datetime
import json
import re
import uuid
import os
from django.views import View
from django.shortcuts import render,HttpResponse,redirect
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.contrib.sessions.models import Session
from apps.rbac import models as rbac_db
from apps.cmdb import models as cmdb_db
from AnsbOps.settings import ENCRYPT_KEY,BASE_DIR
from tools import encryption,perms_control


class CustomBackend(ModelBackend):
    """自定义登录认证"""
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = rbac_db.User.objects.get(Q(user=username) | Q(email=username) | Q(phone=username))
            if user:
                # 加密密码
                pc = encryption.prpcrypt(ENCRYPT_KEY)  # 初始化密钥
                aes_passwd = pc.encrypt(password)
                user_passwd = user.passwd.strip("b").strip("'").encode(encoding="utf-8")
                if aes_passwd == user_passwd:
                    return user
        except Exception as e:
            print (e)
            return None

def login_check(func):
    """登录认证装饰器"""
    def wrapper(request, *args, **kwargs):
        next_url = request.get_full_path()
        if request.session.get("user"):
            return func(request, *args, **kwargs)
        else:
            return redirect("/login/?next={}".format(next_url))
    return wrapper

def perms_check(func):
    """权限装饰器"""
    def wrapper(request, *args, **kwargs):
        req_url = request.get_full_path()
        if  req_url== "/":
            pass
        else:
            paths=req_url.strip().strip("/").split("/")[:2]
            req_url = "/{}/{}/".format(paths[0],paths[1])
        req_method = request.method
        try:
            uuid_str = "{}{}".format(req_url, req_method)
            perms_key = str(uuid.uuid3(uuid.NAMESPACE_DNS, uuid_str))
            perms_list = request.session['perms_list']
            if perms_key in perms_list:
                return func(request, *args, **kwargs)
            else:
                ret = {"status": "perms_false", "info": "权限不足，请联系管理员"}
                data = json.dumps(ret,ensure_ascii=False)
                return HttpResponse(data)
        except Exception as e:
            ret = {"status": "perms_false", "info":e}
            data = json.dumps(ret)
            return HttpResponse(data)
    return wrapper


class LoginView(View):
    """登录认证视图"""
    def dispatch(self, request, *args, **kwargs):
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        """
        处理GET请求
        """
        return render(request, 'base/login.html')

    def post(self, request):
        """
        处理POST请求
        """
        username = request.POST.get('username')
        passwd = request.POST.get('passwd')
        user = authenticate(username=username, password=passwd)
        if user:
            login(request, user)
            #设置会话参数
            request.session['user'] = user.user
            request.session['name'] = user.name
            request.session['cur_role'] = user.role.role
            #更新用户状态
            user.status = "online"
            user.save()
            #获取用户权限清单
            request.session['menu_list'] = perms_control.menus_list(username)
            request.session['perms_list'] =perms_control.perms_list(username)
            next_url = request.POST.get("next")
            if next_url:
                return redirect(next_url)
            else:
                return redirect('/')
        else:
            return render(request, 'base/login.html', {"msg": "用户名或密码错误,请重新登录！"})
        return render(request, 'base/login.html')

@login_check
def Logout(request):
    user = request.session['user']
    user_obj = rbac_db.User.objects.get(user=user)
    user_obj.status = "offline"
    user_obj.save()
    logout(request)
    request.session.delete()
    return render(request, "base/login.html")


@login_check
@perms_check
def get_role_perms(request):
    """获取角色权限"""
    role_id = request.POST.get("role_id")
    #获取角色已授权菜单
    menu_list = perms_control.menus_list(username=None,role_id=role_id)
    perms_list = perms_control.perms_id_list(role_id)
    #提取角色已有授权的菜单id
    one_menu_ids = []
    two_menu_ids = []
    menu_perms_ids = []
    for i in menu_list:
        one_menu_ids.append(i['id'])
        for j in i['two_menu']:
            two_menu_ids.append(j['id'])
            menu_perms = rbac_db.Permssions.objects.filter(parent_id=j['id'])
            for k in menu_perms:
                if k.id in perms_list:
                    menu_perms_ids.append(k.id)

    #获取所有权限
    all_menu_list = []
    one_menu = rbac_db.Permssions.objects.filter(perms_type__contains="一级菜单")
    for i in one_menu:
        two_menu = rbac_db.Permssions.objects.filter(parent_id=i.id)
        two_menu_list = []
        for j in two_menu:
            menu_perms = rbac_db.Permssions.objects.filter(parent_id=j.id)
            menu_perms_list = []
            for k in menu_perms:
                menu_perms_list.append({'id':k.id,'perms': k.perms})
            two_menu_list.append({'id':j.id,'perms': j.perms,"menu_perms":menu_perms_list})
        all_menu_list.append({'id':i.id,'perms': i.perms, "two_menu": two_menu_list})

    #生成菜单树
    nodes = []
    for i in all_menu_list:
        if i["id"] in one_menu_ids:
            nodes.append({"id": i['id'], "pId":0, "name": i['perms'], 'open': True,'checked': True})
        else:
            nodes.append({"id": i['id'], "pId": 0, "name": i['perms'], 'open': True})
        for j in i['two_menu']:
            node_id ="{}#{}".format(i['id'],j['id'])
            if j['id'] in two_menu_ids:
                nodes.append({"id": node_id, "pId":i['id'] , "name": j['perms'], 'open': True, 'checked': True})
            else:
                nodes.append({"id": node_id, "pId": i['id'], "name": j['perms'], 'open': True})
            for  k in j["menu_perms"]:
                perms_node_id = "{}#{}#{}".format(i['id'], j['id'],k["id"])
                if k['id'] in menu_perms_ids:
                    nodes.append({"id": perms_node_id, "pId": node_id, "name": k['perms'], 'open': True, 'checked': True})
                else:
                    nodes.append({"id": perms_node_id, "pId": node_id, "name": k['perms'], 'open': True})

    ret = {"status": "True", "info":nodes}
    data = json.dumps(ret)
    return HttpResponse(data)


@login_check
@perms_check
def add_role_perms(request):
    """权限授权"""
    menu_nums = request.POST.get("node_id_json")
    role_id = request.POST.get("role_id")
    role_obj = rbac_db.Role.objects.get(id=role_id)
    if role_obj.role == "admin":
        data = "超级管理员禁止修改！"
    else:
        menu_nums = json.loads(menu_nums)
        role_obj.perms.clear()
        for i in menu_nums:
            i = str(i)
            if re.search(r"#",i):
                id = i.split("#")[-1]
            else:
                id= i
            menu_obj = rbac_db.Permssions.objects.get(id=id)
            role_obj.perms.add(menu_obj)
        data = "授权已更新，重新登录即生效！"
    ret = {"status": "True", "info": data}
    data = json.dumps(ret)
    return HttpResponse(data)



@login_check
@perms_check
def get_role_asset(request):
    """获取资产"""
    role_id = request.POST.get("role_id")
    role_obj = rbac_db.Role.objects.get(id=role_id)
    if role_obj.role == "admin":
        host_list = cmdb_db.Asset.objects.all()
    else:
        host_list = role_obj.asset.all()
    asset_num_list = []
    for i in host_list:
        host_num = str(i.group.id) + "#" + str(role_id) + "#" + str(i.id)
        asset_num_list.append(host_num)

    nodes = []
    hostgroup_obj = cmdb_db.AssetGroup.objects.all()
    for i in hostgroup_obj:
        hostgroup_id = i.id
        hostgroup_name = i.group_name
        host_obj = cmdb_db.Asset.objects.filter(group_id=hostgroup_id)
        if host_obj:
            nodes.append({"id": hostgroup_id, "pId": 0, "name": hostgroup_name, "open": "True",'checked': True})
            for j in host_obj:
                host_num = str(hostgroup_id) + "#" + str(role_id) + "#" + str(j.id)
                if host_num in asset_num_list:
                    nodes.append({"id": host_num, "pId": hostgroup_id, "name": j.asset_ip, 'open': True, 'checked': True})
                else:
                    nodes.append({"id": host_num, "pId": hostgroup_id, "name": j.asset_ip, 'open': True})
    ret = {"status": "True", "info": nodes}
    data = json.dumps(ret)
    return HttpResponse(data)


@login_check
@perms_check
def add_role_asset(request):
    """资产授权"""
    asset_nums = request.POST.get("node_id_json")
    role_id = request.POST.get("role_id")
    role_obj = rbac_db.Role.objects.get(id=role_id)
    if role_obj.role == "admin":
        data = "超级管理员禁止修改！"
    else:
        asset_nums = json.loads(asset_nums)
        role_obj.asset.clear()
        for i in asset_nums:
            if re.search(r"#",str(i)):
                asset_id = i.split("#")[-1]
                host_obj = cmdb_db.Asset.objects.get(id=asset_id)
                role_obj.asset.add(host_obj)
        data = "资产授权成功"
    ret = {"status": "True", "info": data}
    data = json.dumps(ret)
    return HttpResponse(data)

