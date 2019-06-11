import json
import uuid
import redis
from django.shortcuts import render,HttpResponse
from django.views import View
from apps.rbac import models as rbac_db
from apps.cmdb import models as cmdb_db
from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage
from tools import page as pg
from AnsbOps.settings import ENCRYPT_KEY,REDIS_PORT,REDIS_HOST
from tools import encryption
from django.utils.decorators import method_decorator
from apps.rbac.authviews import login_check,perms_check

# Create your views here.

class IndexView(View):
    """
    首页
    """
    @method_decorator(login_check)
    @method_decorator(perms_check)
    def dispatch(self, request, *args, **kwargs):
        return super(IndexView, self).dispatch(request, *args, **kwargs)

    def get(self,request):
        caption = "资产仪表"
        cur_role = request.session['cur_role']
        if cur_role == "admin":
            asset = cmdb_db.Asset.objects.all()
        else:
            role_obj = rbac_db.Role.objects.get(role=cur_role)
            asset = role_obj.asset.all()
        asset_count = asset.count()
        run_count = 0
        abnormal_count = 0
        for i in asset:
            if i.asset_status == "在线":
                run_count +=1
            else:
                abnormal_count +=1

        #获取zabbix 当前告警信息
        rd = redis.Redis(host=REDIS_HOST,port=REDIS_PORT)
        zabbix_problem = rd.get("zabbix_problem")
        zabbix_problem = json.loads(zabbix_problem)

        #获取资产饼图
        group_obj = cmdb_db.AssetGroup.objects.all()
        asset_count = cmdb_db.Asset.objects.all().count()
        n = 0
        group_data = []
        data_info = []
        for i in group_obj:
            group_data.append(i.group_name)
            asset = i.asset_set.all()
            group_count = asset.count()
            n+=group_count
            data_info.append({"value":group_count, "name":i.group_name})
        other_count = asset_count - n
        if other_count >0:
            data_info.insert(0,{"value":other_count, "name":u"未分组"})
            group_data.insert(0,"未分组")
        return render(request,"base/index.html",locals())


class RoleView(View):
    """角色管理"""

    @method_decorator(login_check)
    @method_decorator(perms_check)
    def dispatch(self, request, *args, **kwargs):
        return super(RoleView,self).dispatch(request, *args, **kwargs)

    def get(self,request,page=1):
        caption = "角色管理"
        db_obj = rbac_db.Role.objects.all().order_by('id')
        if db_obj:
            pagesize = 15
            paginator = Paginator(db_obj, pagesize)
            # 从前端获取当前的页码数,默认为1
            currentPage = int(page)
            page_nums = paginator.num_pages
            page_list = pg.control(currentPage, page_nums)
            try:
                data_list = paginator.page(page)  # 获取当前页码的记录
            except PageNotAnInteger:
                data_list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
            except EmptyPage:
                data_list = paginator.page(paginator.num_pages)
        else:
            data_list = None
        return render(request, 'rbac/role.html', locals())

    def post(self,request):
        '''添加角色'''
        role = request.POST.get("role")
        role_msg = request.POST.get("role_msg")
        try:
            role_obj = rbac_db.Role(role=role,role_msg=role_msg)
            role_obj.save()
            msg = "添加成功"
        except Exception as e:
            msg = "添加失败：\n%s" % e
        ret = {"status": "True", "info": msg}
        data = json.dumps(ret)
        return HttpResponse(data)

    def put(self,request):
        """修改角色"""
        role_info = eval(request.body.decode())
        role_id = role_info.get("role_id")
        role = role_info.get("role")
        role_msg = role_info.get("role_msg")
        action = role_info.get("action",None)
        if action:
            """修改角色信息"""
            role_obj = rbac_db.Role.objects.get(id=role_id)
            role_obj.role = role
            role_obj.role_msg = role_msg
            role_obj.save()
            ret = {"status": "True", "info": "已修改"}
            data = json.dumps(ret)
            return HttpResponse(data)
        else:
            """获取修改信息"""
            role_info = rbac_db.Role.objects.get(id=role_id)
            info_json = {'role_id': role_info.id, 'role': role_info.role, 'role_msg': role_info.role_msg}
            ret = {"status": "True", "info": info_json}
            data = json.dumps(ret)
        return HttpResponse(data)

    def delete(self,request):
        role_info = eval(request.body.decode())
        role_id = role_info.get("role_id")
        rbac_db.Role.objects.get(id=role_id).delete()
        ret = {"status": "True", "info": "已删除"}
        data = json.dumps(ret)
        return HttpResponse(data)


class UserView(View):
    """用户管理"""
    @method_decorator(login_check)
    @method_decorator(perms_check)
    def dispatch(self, request, *args, **kwargs):
        return super(UserView,self).dispatch(request, *args, **kwargs)

    def get(self,request,page=1):
        caption = "用户管理"
        user = request.session['user']
        cur_role = rbac_db.User.objects.get(user=user).role.role
        if cur_role=="admin":
            db_obj = rbac_db.User.objects.all().order_by('id')
        else:
            db_obj = rbac_db.User.objects.filter(user=user).order_by('id')
        role_list = rbac_db.Role.objects.all()
        if db_obj:
            pagesize = 10
            paginator = Paginator(db_obj, pagesize)
            # 从前端获取当前的页码数,默认为1
            # 把当前的页码数转换成整数类型
            currentPage = int(page)
            page_nums = paginator.num_pages
            page_list = pg.control(currentPage, page_nums)
            try:
                data_list = paginator.page(page)  # 获取当前页码的记录
            except PageNotAnInteger:
                data_list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
            except EmptyPage:
                data_list = paginator.page(paginator.num_pages)
        else:
            data_list = None
        return render(request, 'rbac/user.html', locals())

    def post(self,request):
        '''添加用户'''
        user = request.POST.get("user")
        name = request.POST.get("name")
        passwd = request.POST.get("passwd")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        role_id = request.POST.get("role_id")
        # 加密密码
        pc = encryption.prpcrypt(ENCRYPT_KEY)
        en_passwd = pc.encrypt(passwd)
        try:
            if role_id !="0":
                user_obj = rbac_db.User(user=user, name=name, passwd=en_passwd, phone=phone, email=email, role_id=role_id)
            else:
                user_obj = rbac_db.User(user=user, name=name, passwd=en_passwd, phone=phone, email=email)
            user_obj.save()
            msg = "添加成功"
        except Exception as e:
            msg = "添加失败：\n%s" % e
        ret = {"status": "True", "info": msg}
        data = json.dumps(ret)
        return HttpResponse(data)

    def put(self,request):
        """修改用户"""
        req_info = eval(request.body.decode())
        user_id = req_info.get("user_id")
        user = req_info.get("user")
        name = req_info.get("name")
        phone = req_info.get("phone")
        email = req_info.get("email")
        role_id = req_info.get("role_id")
        action = req_info.get("action")
        if action:
            user_obj = rbac_db.User.objects.get(id=user_id)
            user_obj.name = name
            user_obj.user = user
            user_obj.email = email
            user_obj.phone = phone
            if role_id != "0":
                user_obj.role_id = role_id
            else:
                user_obj.role_id = None
            user_obj.save()
            ret = {"status": "True", "info": "已修改"}
            data = json.dumps(ret)
            return HttpResponse(data)
        else:
            """获取修改的用户信息"""
            user_obj = rbac_db.User.objects.get(id=user_id)
            if user_obj.role_id:
                role_id = user_obj.role_id
            else:
                role_id = 0
            data = {"user": user_obj.user, "email": user_obj.email,
                    "passwd": user_obj.passwd,"name": user_obj.name,
                    "phone": user_obj.phone, "role_id": role_id, "user_id": user_obj.id}
            ret = {"status": "True", "info": data}
            data = json.dumps(ret)
            return HttpResponse(data)

    def delete(self,request):
        user_info = eval(request.body.decode())
        user_id = user_info.get("user_id")
        rbac_db.User.objects.get(id=user_id).delete()
        ret = {"status": "True", "info": "已删除"}
        data = json.dumps(ret)
        return HttpResponse(data)


class PermsView(View):
    """权限管理"""
    @method_decorator(login_check)
    @method_decorator(perms_check)
    def dispatch(self, request, *args, **kwargs):
        return super(PermsView,self).dispatch(request, *args, **kwargs)

    def get(self,request,page=1):
        """查看权限"""
        caption = "权限管理"
        menu_list = rbac_db.Permssions.objects.filter(perms_type__contains="菜单")
        db_obj = rbac_db.Permssions.objects.all().order_by('id')
        one_perms = rbac_db.Permssions.objects.filter(perms_type__contains="一级菜单")
        perms_list = []
        for i in one_perms:
            one_child = []
            tow_perms = rbac_db.Permssions.objects.filter(parent_id=i.id)
            for j in tow_perms:
                two_child = []
                three_perms = rbac_db.Permssions.objects.filter(parent_id=j.id)
                for k in three_perms:
                    two_child.append({"id":k.id,"perms":k.perms,"perms_id":k.perms_id,"perms_img":k.perms_img,
                                      "perms_url":k.perms_url,"perms_method":k.perms_method,"status":k.status})

                one_child.append({"id":j.id,"perms":j.perms,"perms_id":j.perms_id,"perms_img":j.perms_img,
                                  "perms_url":j.perms_url,"perms_method":j.perms_method,"status":j.status,"child":two_child})

            perms_list.append({"id":i.id,"perms": i.perms, "perms_img":i.perms_img,"perms_id": i.perms_id,
                               "perms_url": i.perms_url, "perms_method": i.perms_method, "status": i.status,"child":one_child})
        return  render(request,'rbac/perms.html',locals())

    def post(self,request):
        """添加权限"""
        perms = request.POST.get("perms")
        perms_img = request.POST.get("perms_img")
        perms_type = request.POST.get("perms_type")
        perms_method = request.POST.get("perms_method")
        perms_parent = request.POST.get("perms_parent")
        perms_url = request.POST.get("perms_url")
        uuid_str = "{}{}".format(perms_url,perms_method)
        perms_id = uuid.uuid3(uuid.NAMESPACE_DNS,uuid_str)
        try:
            if perms_parent != "0":
                perms_obj = rbac_db.Permssions(perms=perms, perms_id=perms_id, perms_img=perms_img,
                                               perms_type=perms_type, parent_id=perms_parent, perms_url=perms_url,
                                               perms_method=perms_method)
            else:
                perms_obj = rbac_db.Permssions(perms=perms, perms_id=perms_id, perms_img=perms_img,
                                               perms_type=perms_type, perms_url=perms_url, perms_method=perms_method)
            perms_obj.save()
            msg = "添加成功"
        except Exception as e:
            msg = "添加失败：\n%s" % e
        ret = {"status": "True", "info": msg}
        data = json.dumps(ret)
        return HttpResponse(data)

    def put(self,request):
        """修改权限"""
        req_info = eval(request.body.decode())
        perms_id = req_info.get("perms_id")
        perms = req_info.get("perms")
        perms_img = req_info.get("perms_img")
        perms_type = req_info.get("perms_type")
        perms_method = req_info.get("perms_method")
        perms_parent = req_info.get("perms_parent")
        perms_url = req_info.get("perms_url")
        action = req_info.get("action")
        if action:
            perms_obj = rbac_db.Permssions.objects.get(id=perms_id)
            perms_obj.perms = perms
            perms_obj.perms_type = perms_type
            perms_obj.perms_img = perms_img
            perms_obj.perms_method = perms_method
            if perms_parent != "0":
                perms_obj.parent_id = perms_parent
            else:
                perms_obj.parent_id = None
            perms_obj.perms_url = perms_url
            uuid_str = "{}{}".format(perms_url, perms_method)
            perms_key = uuid.uuid3(uuid.NAMESPACE_DNS, uuid_str)
            perms_obj.perms_id = perms_key
            perms_obj.save()
            ret = {"status": "True", "info": "已修改"}
            data = json.dumps(ret)
            return HttpResponse(data)
        else:
            edit_perms_obj = rbac_db.Permssions.objects.get(id=perms_id)
            if edit_perms_obj.parent_id:
                parent_id = edit_perms_obj.parent_id
            else:
                parent_id = 0
            data= {"perms_id":edit_perms_obj.id,"perms":edit_perms_obj.perms,"perms_type":edit_perms_obj.perms_type,
                   "perms_parent":parent_id,"perms_url":edit_perms_obj.perms_url,"perms_img":edit_perms_obj.perms_img,
                   "perms_method":edit_perms_obj.perms_method}
            ret = {"status": "True", "info": data}
            data = json.dumps(ret)
            return HttpResponse(data)

    def delete(self,request):
        """删除权限"""
        req_info = eval(request.body.decode())
        perms_id = req_info.get("perms_id")
        rbac_db.Permssions.objects.get(id=perms_id).delete()
        ret = {"status": "True", "info": "已删除"}
        data = json.dumps(ret)
        return HttpResponse(data)