from django.shortcuts import render
import json
import re
import os
import datetime
from django.shortcuts import render,HttpResponse
from django.views import View
from django.utils.decorators import method_decorator
from apps.sysmg import models as sys_db
from apps.cmdb import models as cmdb_db
from apps.rbac import models as rbac_db
from apps.rbac.authviews import login_check,perms_check
from django.db.models import Q
from AnsbOps.settings import BASE_DIR
from tools import ansible_api
from apps.sysmg.tasks import install_server
from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage
from tools import page as pg

# Create your views here.


class ServerInstallView(View):
    """环境部署"""
    @method_decorator(login_check)
    @method_decorator(perms_check)
    def dispatch(self, request, *args, **kwargs):
        return super(ServerInstallView,self).dispatch(request,*args, **kwargs)

    def get(self,request,page=1):
        caption = "脚本管理"
        hostgroup_obj = cmdb_db.AssetGroup.objects.all()
        tree_info = []
        for i in hostgroup_obj:
            hostgroup_id = i.id
            hostgroup_name = i.group_name
            host_obj = cmdb_db.Asset.objects.filter(group_id=hostgroup_id)
            if host_obj:
                tree_info.append({"id": hostgroup_id, "pId": 0, "name": hostgroup_name, "open": "True"})
                for j in host_obj:
                    host_num = str(hostgroup_id)  + "#" + str(j.id)
                    tree_info.append({"id": host_num, "pId": hostgroup_id, "name": j.asset_ip, 'open': True})
        znodes_data = json.dumps(tree_info, ensure_ascii=False)

        db_obj = sys_db.ServerInstall.objects.all().order_by('id')
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
        return render(request, 'sys/server_install.html', locals())

    def post(self,request):
        server_name = request.POST.get('server_name')
        server_version = request.POST.get('server_version')
        install_script = request.POST.get('install_script')
        try:
            env_obj = sys_db.ServerInstall(server_name=server_name, server_version=server_version,install_script=install_script)
            env_obj.save()
            msg = '添加成功'
        except Exception as e:
            msg = '添加失败：\n%s' % e
        ret = {"status": "True", "info": msg}
        data = json.dumps(ret)
        return HttpResponse(data)

    def put(self,request):
        """修改"""
        req_info = eval(request.body.decode())
        server_id = req_info.get("server_id")
        server_name = req_info.get("server_name")
        server_version = req_info.get("server_version")
        install_script = req_info.get("install_script")
        action = req_info.get("action",None)
        if action:
            """修改部署信息"""
            server_obj = sys_db.ServerInstall.objects.get(id=server_id)
            server_obj.server_name = server_name
            server_obj.server_version = server_version
            server_obj.install_script = install_script
            server_obj.save()
            msg = "已修改"
            ret = {"status": "True", "info": msg}
            data = json.dumps(ret)
            return HttpResponse(data)
        else:
            """获取修改信息"""
            server_info = sys_db.ServerInstall.objects.get(id=server_id)
            info_json = {'server_id': server_info.id, 'server_name': server_info.server_name, 'server_version': server_info.server_version,
                         'install_script': server_info.install_script}
            ret = {"status": "True", "info": info_json}
            data = json.dumps(ret)
        return HttpResponse(data)

    def delete(self,request):
        req_info = eval(request.body.decode())
        server_id = req_info.get("server_id")
        sys_db.ServerInstall.objects.get(id=server_id).delete()
        ret = {"status": "True", "info": "已删除"}
        data = json.dumps(ret)
        return HttpResponse(data)


@login_check
@perms_check
def exec_script(request):
    host_info = request.POST.get("node_id_json")
    server_id = request.POST.get("server_id")
    ip_list = []
    for i in json.loads(host_info):
        if re.search("\d+.\d+.\d+.\d", i):
            ip_list.append(i)
    server_obj = sys_db.ServerInstall.objects.get(id=server_id)
    install_script = server_obj.install_script
    server_name = server_obj.server_name
    script_name = "install_%s" % server_name
    script_file = os.path.join(BASE_DIR, 'tools', 'scripts', script_name)
    with open(script_file, 'w') as f:
        f.write(install_script)
    tk = install_server.delay(json.dumps(ip_list),script_file)
    msg = "任务ID:{}".format(tk.id)
    ret = {"status": "True", "info": msg}
    data = json.dumps(ret)
    return HttpResponse(data)


class BatchView(View):
    """批量管理"""
    @method_decorator(login_check)
    @method_decorator(perms_check)
    def dispatch(self, request, *args, **kwargs):
        return super(BatchView,self).dispatch(request,*args, **kwargs)

    def get(self,request):
        caption = "批量管理"
        hostgroup_obj = cmdb_db.AssetGroup.objects.all()
        tree_info = []
        for i in hostgroup_obj:
            hostgroup_id = i.id
            hostgroup_name = i.group_name
            hostinfo_obj = cmdb_db.Asset.objects.filter(Q(group_id=hostgroup_id))
            if hostinfo_obj:
                tree_info.append({"id": hostgroup_id, "pId": 0, "name": hostgroup_name, "open": "false"})
                for j in hostinfo_obj:
                    host_id = j.id
                    host_ip = j.asset_ip
                    id = hostgroup_id * 10 + host_id
                    tree_info.append({"id": id, "pId": hostgroup_id, "name": host_ip})
        znodes_data = json.dumps(tree_info, ensure_ascii=False)
        return render(request, 'sys/batch.html', locals())


@login_check
@perms_check
def batch_run_cmd(request):
    """批量执行命令"""
    cmd = request.POST.get('cmd')
    ip_list = json.loads(request.POST.get("ip_list"))

    ret = ansible_api.run_ansible("shell",cmd,ip_list)
    result = json.loads(ret)
    data_txt = ""
    for ip in result["success"].keys():
        head_txt = '=================== %s (SUCCESS)===================\n' % ip
        result_info = "%sCommand：%s\nOutput：\n%s\n\r" % (head_txt, cmd, result["success"][ip]["stdout"])
        data_txt += result_info
    for ip in result["failed"].keys():
        head_txt = '=================== %s (FAILED)===================\n' % ip
        result_info = "%sCommand：%s\nOutput：\n%s\n\r" % (head_txt, cmd, result["failed"][ip]["stderr"])
        data_txt += result_info

    ret = {"status": "True", "info": data_txt}
    data = json.dumps(ret)
    return HttpResponse(data)

@login_check
@perms_check
def batch_upload_file(request):
    """批量上传文件"""
    upload_path = request.POST.get('upload_path')
    upload_file = request.FILES.get("upfile")
    ip_list = json.loads(request.POST.get("ip_list"))
    up_file_path = os.path.join(BASE_DIR, 'statics', 'upload')
    if os.path.exists(up_file_path):
        pass
    else:
        os.makedirs(up_file_path)
    file_path = os.path.join(up_file_path, upload_file.name)
    dest = os.path.join(upload_path,upload_file.name)
    if os.path.exists(file_path):
        date_str = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        os.rename(file_path, file_path + "_" + date_str)
    else:
        pass
    f = open(file_path, 'wb')
    for chunk in upload_file.chunks():
        f.write(chunk)
    f.close()

    module_name = "copy"
    module_arg = "src={} dest={} backup=yes".format(file_path, dest)
    ret = ansible_api.run_ansible(module_name,module_arg,ip_list)
    data_txt=''
    result = json.loads(ret)
    for ip in result["success"].keys():
        head_txt = '=================== %s (SUCCESS)===================\n' % ip
        result_info = "%s\nOutput：\n%s\n\r" % (head_txt, result["success"][ip]["dest"])
        data_txt += result_info
    for ip in result["failed"].keys():
        head_txt = '=================== %s (FAILED)===================\n' % ip
        result_info = "%s\nOutput：\n%s\n\r" % (head_txt, result["failed"][ip]["msg"])
        data_txt += result_info

    ret = {"status": "True", "info": data_txt}
    data = json.dumps(ret)
    return HttpResponse(data)



@login_check
@perms_check
def batch_script(request):
    """批量执行脚本"""
    up_script = request.FILES.get("script_file")
    ip_list = json.loads(request.POST.get("ip_list"))
    script_dir = os.path.join(BASE_DIR, 'tools', 'scripts')
    if os.path.exists(script_dir):
        pass
    else:
        os.makedirs(script_dir)
    script_file = os.path.join(script_dir, up_script.name)
    if os.path.exists(script_file):
        date_str = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        os.rename(script_file, script_file + "_" + date_str)
    else:
        pass
    f = open(script_file, 'wb')
    for chunk in up_script.chunks():
        f.write(chunk)
    f.close()
    ret = ansible_api.run_ansible("script", script_file,ip_list)
    result = json.loads(ret)
    data_txt=''
    for ip in result["success"].keys():
        head_txt = '=================== %s (SUCCESS)===================\n' % ip
        result_info = "%s\nOutput：\n%s\n\r" % (head_txt, result["success"][ip]["stdout"])
        data_txt += result_info
    for ip in result["failed"].keys():
        head_txt = '=================== %s (FAILED)===================\n' % ip
        result_info = "%s\nOutput：\n%s\n\r" % (head_txt, result["failed"][ip]["stdout"])
        data_txt += result_info

    ret = {"status": "True", "info": data_txt}
    data = json.dumps(ret)
    return HttpResponse(data)

    return HttpResponse(data_txt)
