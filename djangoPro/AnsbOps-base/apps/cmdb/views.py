import json
import os
from django.shortcuts import render,HttpResponse
from django.views import View
from apps.cmdb import  models as asset_db
from apps.rbac import models as rbac_db
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from tools import page as pg
from django.utils.decorators import method_decorator
from apps.rbac.authviews import login_check,perms_check
from tools import encryption,get_os_info,ansible_api,ansible_api_v2
from AnsbOps.settings import ENCRYPT_KEY,BASE_DIR


class AssetView(View):
    """
    资产视图
    """
    @method_decorator(login_check)
    @method_decorator(perms_check)
    def dispatch(self, request, *args, **kwargs):
        return super(AssetView, self).dispatch(request, *args, **kwargs)

    def get(self,request,page=1):
        caption = "资产"
        cur_role = request.session['cur_role']
        idc_obj = asset_db.IDC.objects.all()
        group_obj = asset_db.AssetGroup.objects.all()
        changshang_obj = asset_db.ChangShang.objects.all()
        if cur_role == "admin":
            db_obj = asset_db.Asset.objects.all().order_by('id')
        else:
            cur_rolo_obj = rbac_db.Role.objects.get(role=cur_role)
            db_obj = cur_rolo_obj.asset.all().order_by('id')
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
        return render(request,"cmdb/assets.html",locals())

    def post(self,request):
        asset_ip = request.POST.get("asset_ip")
        login_port = request.POST.get("login_port")
        login_user = request.POST.get("login_user")
        login_passwd = request.POST.get("login_passwd")
        login_method = request.POST.get("login_method")
        asset_type = request.POST.get("asset_type")
        asset_model = request.POST.get("asset_model")
        asset_group = request.POST.get("asset_group")
        asset_idc = request.POST.get("asset_idc")
        asset_changshang = request.POST.get("asset_changshang")
        asset_msg = request.POST.get("asset_msg")
        asset_sn = request.POST.get("asset_sn")
        purchase_time = request.POST.get("purchase_time")
        expire_time = request.POST.get("expire_time")
        if asset_group == "0":
            asset_group = None
        if asset_idc == "0":
            asset_idc = None
        if asset_changshang == "0":
            asset_changshang = None

        # 添加ssh_key
        try:
            module_name = 'script'
            module_args = "{}{}".format(BASE_DIR,"/tools/add_ssh_key.sh")
            host_list = [asset_ip]
            result = ansible_api_v2.run_ansible(module_name, module_args, host_list, login_port, login_passwd)
            ret = json.loads(result)["success"]
            if ret[asset_ip]:
                asset_status = "在线"
            else:
                asset_status = "异常"
        except Exception as e:
            asset_status = "异常"
            print("{} ssh 密钥添加异常:{}".format(asset_ip,e))

        # 加密密码
        pc = encryption.prpcrypt(ENCRYPT_KEY)  # 初始化密钥
        aes_passwd = pc.encrypt(login_passwd)

        asset_obj = asset_db.Asset(asset_ip=asset_ip,asset_type=asset_type,asset_model=asset_model,
                                 group_id=asset_group,idc_id=asset_idc,changshang_id=asset_changshang,
                                 asset_msg=asset_msg,asset_sn=asset_sn,purchase_time=purchase_time,
                                 expire_time=expire_time,asset_status=asset_status)
        asset_obj.save()

        login_user_obj = asset_db.AssetLoginInfo(asset_id=asset_obj.id,login_user=login_user,login_port=login_port,
                                                 login_passwd=aes_passwd,login_method=login_method)
        login_user_obj.save()

        #用户角色添加的资产，默认拥有权限
        cur_role = request.session['cur_role']
        if cur_role != "admin":
            role_obj = rbac_db.Role.objects.get(role=cur_role).role
            role_obj.asset.add(asset_obj)
        ret = {"status":"True","info":"添加成功"}
        return HttpResponse(json.dumps(ret,ensure_ascii=False))

    def put(self,request):
        req_info = eval(request.body.decode())
        asset_id = req_info.get("asset_id")
        asset_ip = req_info.get("asset_ip")
        login_port = req_info.get("login_port")
        login_user = req_info.get("login_user")
        login_passwd = req_info.get("login_passwd")
        login_method = req_info.get("login_method")
        asset_type = req_info.get("asset_type")
        asset_model = req_info.get("asset_model")
        asset_group = req_info.get("asset_group")
        asset_idc = req_info.get("asset_idc")
        asset_changshang = req_info.get("asset_changshang")
        asset_msg = req_info.get("asset_msg")
        asset_sn = req_info.get("asset_sn")
        purchase_time = req_info.get("purchase_time")
        expire_time = req_info.get("expire_time")
        action = req_info.get("action",None)
        if action:
            """修改服务器信息"""
            if asset_group == "0":
                asset_group = None
            if asset_idc == "0":
                asset_idc = None
            if asset_changshang == "0":
                asset_changshang = None

            # 加密密码
            pc = encryption.prpcrypt(ENCRYPT_KEY)
            aes_passwd = pc.encrypt(login_passwd)

            asset_obj = asset_db.Asset.objects.get(id=asset_id)
            asset_obj.asset_ip = asset_ip
            asset_obj.asset_model = asset_model
            asset_obj.asset_type = asset_type
            asset_obj.group_id = asset_group
            asset_obj.idc_id = asset_idc
            asset_obj.changshang_id = asset_changshang
            asset_obj.asset_msg = asset_msg
            asset_obj.asset_sn = asset_sn
            asset_obj.purchase_time = purchase_time
            asset_obj.expire_time = expire_time
            asset_obj.save()

            login_user_obj = asset_db.AssetLoginInfo.objects.get(asset_id=asset_id)
            login_user_obj.login_method = login_method
            login_user_obj.login_port = login_port
            login_user_obj.login_user = login_user
            login_user_obj.asset_passwd = aes_passwd

            ret = {"status": "True", "info": "修改成功"}
            data = json.dumps(ret)
            return HttpResponse(data)
        else:
            """获取修改信息"""
            asset_info = asset_db.Asset.objects.get(id=asset_id)
            login_user_obj = asset_db.AssetLoginInfo.objects.get(asset_id=asset_id)
            #密码解密
            pc = encryption.prpcrypt(ENCRYPT_KEY)
            passwd =login_user_obj.login_passwd.strip("b").strip("'").encode(encoding="utf-8")
            de_passwd = pc.decrypt(passwd).decode()
            if asset_info.group_id:
                asset_group = asset_info.group_id
            else:
                asset_group = 0
            if asset_info.idc_id:
                idc_id = asset_info.idc_id
            else:
                idc_id = 0
            if asset_info.changshang_id:
                asset_changshang = asset_info.changshang_id
            else:
                asset_changshang = 0

            info_json = {'asset_id': asset_info.id, 'asset_ip': asset_info.asset_ip,'login_port': login_user_obj.login_port,
                         'login_user': login_user_obj.login_user, 'login_method': login_user_obj.login_method,'login_passwd': de_passwd,
                         'asset_type': asset_info.asset_type, 'asset_model': asset_info.asset_model,'asset_group': asset_group,'asset_idc':idc_id,
                         'asset_changshang': asset_changshang,'asset_msg': asset_info.asset_msg,'asset_sn': asset_info.asset_sn,'expire_time': asset_info.expire_time,
                         'purchase_time': asset_info.purchase_time}
            ret = {"status": "True", "info": info_json}
            data = json.dumps(ret)
            return HttpResponse(data)

    def delete(self,request):
        """删除服务器"""
        req_info = eval(request.body.decode())
        asset_id = req_info.get("asset_id")
        asset_db.Asset.objects.get(id=asset_id).delete()
        ret = {"status": "True", "info": "已删除"}
        data = json.dumps(ret)
        return HttpResponse(data)


@login_check
@perms_check
def asset_detail(request,id):
    """查看服务器详细信息"""
    caption = "资产"
    asset_obj = asset_db.Asset.objects.get(id=id)
    login_obj = asset_db.AssetLoginInfo.objects.get(asset_id=asset_obj.id)
    ip = asset_obj.asset_ip
    host_list = [ip]
    try:
        os_obj = asset_db.AssetOsInfo.objects.get(asset_id=asset_obj.id)
        nic_obj = asset_db.NIC.objects.filter(asset_id=asset_obj.id)
        device_obj = asset_db.Devices.objects.filter(asset_id=asset_obj.id)
        mount_obj = asset_db.Mounts.objects.filter(asset_id=asset_obj.id)
        server_obj = asset_db.RunServer.objects.filter(asset_id=asset_obj.id)
    except:
        with open("/etc/ansible/hosts", "a") as f:
            f.write("{} {}={}\n".format(ip, "ansible_ssh_port", login_obj.login_port))

        os_info = get_os_info.main(host_list)
        data = os_info[ip]
        os_obj = asset_db.AssetOsInfo(asset_id=asset_obj.id,hostname=data['localhost'],os_type=data['kernel'],
                                      kernel_version="{} {}".format(data['kernel'],data['kernelrelease']),os_version="{} {}".format(data['os'],data['osrelease']),product_name=data['productname'],
                                      cpu_model=data['cpu_model'],cpu_core_count=data['num_cpus'],mem_size=data['mem_size'])
        os_obj.save()

        for i in data['interface']:
            nic_obj = asset_db.NIC(asset_id=asset_obj.id,name=i["label"],model=i["type"],mac=i["hwaddr"],ip_address=i["address"],net_mask=i["netmask"],mtu=i["mtu"])
            nic_obj.save()

        for i in data['devices_list']:
            device_obj = asset_db.Devices(asset_id=asset_obj.id,device_name=i["device_name"],device_model=i["device_model"],device_size=i["device_size"],interface_type=i["interface_type"])
            device_obj.save()

        for i in data['mount_list']:
            mount_obj = asset_db.Mounts(asset_id=asset_obj.id, device=i["device"],
                                          mount=i["mount"], size_total=i["size_total"],size_available=i["size_available"],
                                          fstype=i["fstype"])
            mount_obj.save()

        module_name = 'script'
        module_args = "{}{}".format(BASE_DIR, "/tools/get_netstat_info.py")
        ret = ansible_api.run_ansible(module_name, module_args, host_list)
        data = json.loads(ret)
        server_info = data['success'][ip]["stdout_lines"]
        for i in json.loads(server_info[0]):
            server_obj = asset_db.RunServer(asset_id=asset_obj.id,server_name=i[0],server_version=i[1],server_port=json.dumps(i[2]))
            server_obj.save()

        os_obj = asset_db.AssetOsInfo.objects.get(asset_id=asset_obj.id)
        nic_obj = asset_db.NIC.objects.filter(asset_id=asset_obj.id)
        device_obj = asset_db.Devices.objects.filter(asset_id=asset_obj.id)
        mount_obj = asset_db.Mounts.objects.filter(asset_id=asset_obj.id)
        server_obj = asset_db.RunServer.objects.filter(asset_id=asset_obj.id)

    return render(request, "cmdb/asset_detail.html", locals())




class AssetGroupView(View):
    """
    资产分组视图
    """
    @method_decorator(login_check)
    @method_decorator(perms_check)
    def dispatch(self, request, *args, **kwargs):
        return super(AssetGroupView, self).dispatch(request, *args, **kwargs)

    def get(self,request,page=1):
        caption = "分组"
        idc_obj = asset_db.AssetGroup.objects.all().order_by('id')
        if idc_obj:
            pagesize = 10
            paginator = Paginator(idc_obj, pagesize)
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
        return render(request,"cmdb/asset_group.html",locals())

    def post(self,request):
        group_name = request.POST.get("group_name")
        group_msg = request.POST.get("group_msg")
        group_obj = asset_db.AssetGroup(group_name=group_name, group_msg=group_msg)
        group_obj.save()
        ret = {"status":"True","info":"添加成功"}
        return HttpResponse(json.dumps(ret,ensure_ascii=False))

    def put(self,request):
        req_info = eval(request.body.decode())
        group_id = req_info.get("group_id")
        group_name = req_info.get("group_name")
        group_msg = req_info.get("group_msg")
        action = req_info.get("action",None)
        if action:
            """修改group信息"""
            group_obj = asset_db.AssetGroup.objects.get(id=group_id)
            group_obj.group_name = group_name
            group_obj.group_msg = group_msg
            group_obj.save()
            ret = {"status": "True", "info": "修改成功"}
            data = json.dumps(ret)
            return HttpResponse(data)
        else:
            """获取修改信息"""
            group_obj = asset_db.AssetGroup.objects.get(id=group_id)
            info_json = {'group_id': group_obj.id, 'group_name': group_obj.group_name, 'group_msg': group_obj.group_msg}
            ret = {"status": "True", "info": info_json}
            data = json.dumps(ret)
        return HttpResponse(data)

    def delete(self,request):
        """删除权限"""
        req_info = eval(request.body.decode())
        group_id = req_info.get("group_id")
        asset_db.AssetGroup.objects.get(id=group_id).delete()
        ret = {"status": "True", "info": "已删除"}
        data = json.dumps(ret)
        return HttpResponse(data)

class IdcView(View):
    """
    机房视图
    """
    @method_decorator(login_check)
    @method_decorator(perms_check)
    def dispatch(self, request, *args, **kwargs):
        return super(IdcView, self).dispatch(request, *args, **kwargs)

    def get(self,request,page=1):
        caption = "机房"
        idc_obj = asset_db.IDC.objects.all().order_by('id')
        if idc_obj:
            pagesize = 10
            paginator = Paginator(idc_obj, pagesize)
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
        return render(request, 'cmdb/idc.html', locals())

    def post(self,request):
        idc_name = request.POST.get("idc_name")
        idc_msg = request.POST.get("idc_msg")
        contact = request.POST.get("contact")
        contact_phone = request.POST.get("contact_phone")
        contact_email = request.POST.get("contact_email")
        idc_obj = asset_db.IDC(idc_name=idc_name,idc_msg=idc_msg,contact=contact,contact_phone=contact_phone,
                               contact_email=contact_email)
        idc_obj.save()
        ret = {"status":"True","info":"添加成功"}
        return HttpResponse(json.dumps(ret,ensure_ascii=False))

    def put(self,request):
        req_info = eval(request.body.decode())
        idc_id = req_info.get("idc_id")
        idc_name = req_info.get("idc_name")
        idc_msg = req_info.get("idc_msg")
        contact = req_info.get("contact")
        contact_phone = req_info.get("contact_phone")
        contact_email = req_info.get("contact_email")
        action = req_info.get("action",None)
        if action:
            """修改IDC信息"""
            idc_obj = asset_db.IDC.objects.get(id=idc_id)
            idc_obj.idc_name = idc_name
            idc_obj.idc_msg = idc_msg
            idc_obj.contact = contact
            idc_obj.contact_phone = contact_phone
            idc_obj.contact_email = contact_email
            idc_obj.save()
            ret = {"status": "True", "info": "修改成功"}
            data = json.dumps(ret)
            return HttpResponse(data)
        else:
            """获取修改信息"""
            idc_obj = asset_db.IDC.objects.get(id=idc_id)
            info_json = {'idc_id': idc_obj.id, 'idc_name': idc_obj.idc_name, 'idc_msg': idc_obj.idc_msg,
                         'contact': idc_obj.contact,'contact_phone': idc_obj.contact_phone,'contact_email': idc_obj.contact_email}
            ret = {"status": "True", "info": info_json}
            data = json.dumps(ret)
        return HttpResponse(data)

    def delete(self,request):
        """删除权限"""
        req_info = eval(request.body.decode())
        idc_id = req_info.get("idc_id")
        asset_db.IDC.objects.get(id=idc_id).delete()
        ret = {"status": "True", "info": "已删除"}
        data = json.dumps(ret)
        return HttpResponse(data)

class ChangShangView(View):
    """
    设备厂商视图
    """
    @method_decorator(login_check)
    @method_decorator(perms_check)
    def dispatch(self, request, *args, **kwargs):
        return super(ChangShangView, self).dispatch(request, *args, **kwargs)

    def get(self,request,page=1):
        caption = "厂商"
        db_obj = asset_db.ChangShang.objects.all().order_by('id')
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
        return render(request,"cmdb/changshang.html",locals())

    def post(self,request):
        changshang = request.POST.get("changshang")
        contact = request.POST.get("contact")
        contact_phone = request.POST.get("contact_phone")
        contact_email = request.POST.get("contact_email")
        changshang_obj = asset_db.ChangShang(changshang=changshang,contact=contact,contact_phone=contact_phone,contact_email=contact_email)
        changshang_obj.save()
        ret = {"status":"True","info":"添加成功"}
        return HttpResponse(json.dumps(ret,ensure_ascii=False))

    def put(self,request):
        req_info = eval(request.body.decode())
        changshang_id = req_info.get("changshang_id")
        changshang = req_info.get("changshang")

        contact = req_info.get("contact")
        contact_phone = req_info.get("contact_phone")
        contact_email = req_info.get("contact_email")
        action = req_info.get("action",None)
        if action:
            """修改changshang信息"""
            changshang_obj = asset_db.ChangShang.objects.get(id=changshang_id)
            changshang_obj.changshang = changshang
            changshang_obj.contact = contact
            changshang_obj.contact_phone = contact_phone
            changshang_obj.contact_email = contact_email
            changshang_obj.save()
            ret = {"status": "True", "info": "修改成功"}
            data = json.dumps(ret)
            return HttpResponse(data)
        else:
            """获取修改信息"""
            changshang_obj = asset_db.ChangShang.objects.get(id=changshang_id)
            info_json = {'changshang_id': changshang_obj.id, 'changshang': changshang_obj.changshang,
                         'contact': changshang_obj.contact,'contact_phone': changshang_obj.contact_phone,
                         'contact_email': changshang_obj.contact_email}
            ret = {"status": "True", "info": info_json}
            data = json.dumps(ret)
        return HttpResponse(data)

    def delete(self,request):
        """删除权限"""
        req_info = eval(request.body.decode())
        changshang_id = req_info.get("changshang_id")
        asset_db.ChangShang.objects.get(id=changshang_id).delete()
        ret = {"status": "True", "info": "已删除"}
        data = json.dumps(ret)
        return HttpResponse(data)