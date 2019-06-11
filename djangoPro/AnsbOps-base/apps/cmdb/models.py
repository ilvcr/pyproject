from django.db import models
# Create your models here.

class Asset(models.Model):
    """资产表"""
    asset_ip = models.CharField(max_length=64,unique=True)
    asset_msg = models.CharField(max_length=256)
    asset_type = models.CharField(default='服务器', max_length=128, null=True)
    asset_model = models.CharField(max_length=128, null=True)
    purchase_time = models.CharField(max_length=128, null=True)
    expire_time = models.CharField(max_length=128,null=True)
    asset_sn = models.CharField(max_length=128,null=True)
    asset_status = models.CharField(default="在线",max_length=16)
    group = models.ForeignKey(to="AssetGroup",on_delete=models.SET_NULL,null=True)
    idc = models.ForeignKey(to="IDC",on_delete=models.SET_NULL, null=True)
    changshang  = models.ForeignKey(to="ChangShang",on_delete=models.SET_NULL, null=True)
    add_time = models.DateTimeField(auto_now_add=True)
    m_time = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.asset_ip

class AssetLoginInfo(models.Model):
    """远程登陆信息"""
    asset = models.ForeignKey(to="Asset",on_delete=models.CASCADE)
    login_method = models.CharField(max_length=16,default="SSH")
    login_port = models.CharField(max_length=64)
    login_user = models.CharField(max_length=64)
    login_passwd = models.CharField(max_length=64)

class AssetOsInfo(models.Model):
    asset = models.ForeignKey(to="Asset",on_delete=models.CASCADE)
    hostname = models.CharField(max_length=128, null=True)
    os_type = models.CharField(max_length=128,null=True)
    kernel_version =models.CharField(max_length=128,null=True)
    os_version = models.CharField(max_length=128,null=True)
    product_name = models.CharField(max_length=128,null=True)
    cpu_model = models.CharField('CPU型号', max_length=128, blank=True, null=True)
    cpu_core_count = models.CharField(max_length=16, default=1)
    mem_size = models.CharField(max_length=128, null=True)

class Devices(models.Model):
    """存储设备"""
    asset = models.ForeignKey('Asset',on_delete=models.CASCADE)
    device_name = models.CharField(max_length=128)
    device_model = models.CharField(max_length=128, null=True)
    device_size = models.CharField(max_length=128, null=True)
    interface_type = models.CharField( max_length=128,default='unknown')

class Mounts(models.Model):
    asset = models.ForeignKey('Asset', on_delete=models.CASCADE)
    device = models.CharField(max_length=128)
    mount = models.CharField(max_length=128, null=True)
    size_total = models.CharField(max_length=128, null=True)
    size_available = models.CharField(max_length=128, null=True)
    fstype = models.CharField(max_length=64, null=True)


class NIC(models.Model):
    """网卡组件"""
    asset = models.ForeignKey('Asset',on_delete=models.CASCADE)
    name = models.CharField( max_length=64)
    model = models.CharField(max_length=64,null=True)
    mac = models.CharField(max_length=128,null=True)
    ip_address = models.CharField(max_length=64,null=True)
    net_mask = models.CharField(max_length=64, null=True)
    mtu = models.CharField(max_length=64,null=True)

class RunServer(models.Model):
    """服务器上运行中服务软件信息表"""
    asset = models.ForeignKey(to="Asset",on_delete=models.CASCADE)
    server_name = models.CharField(max_length=256)
    server_version = models.CharField(max_length=512,null=True)
    server_port = models.CharField(max_length=1026,null=True)

class AssetGroup(models.Model):
    """资产分组表"""
    group_name = models.CharField(max_length=64,unique=True)
    group_msg = models.CharField(max_length=256,null=True)
    def __unicode__(self):
        return self.group_name


class IDC(models.Model):
    """机房管理信息"""
    idc_name = models.CharField(max_length=64, unique=True)
    idc_msg = models.CharField(max_length=128, null=True)
    contact = models.CharField(max_length=128, null=True)
    contact_phone = models.CharField(max_length=128, null=True)
    contact_email = models.EmailField(error_messages={'invalid': '邮件格式不正确'},null=True)
    def __unicode__(self):
        return self.idc_name

class ChangShang(models.Model):
    changshang = models.CharField(max_length=128,unique=True)
    contact = models.CharField(max_length=128, null=True)
    contact_phone = models.CharField(max_length=128, null=True)
    contact_email = models.EmailField(error_messages={'invalid': '邮件格式不正确'},null=True)
    def __unicode__(self):
        return self.changshang
