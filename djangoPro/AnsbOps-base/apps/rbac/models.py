from django.db import models
from apps.cmdb.models import Asset
# Create your models here.

class User(models.Model):
    """用户表"""
    user = models.CharField(max_length=64,unique=True)
    name = models.CharField(max_length=64,null=False)
    passwd = models.CharField(max_length=512,null=False)
    phone = models.CharField(max_length=64,null=False)
    email = models.EmailField(error_messages={'invalid': '邮件格式不正确'},null=True)
    role = models.ForeignKey(to="Role",on_delete=models.SET_NULL,null=True)
    status = models.CharField(max_length=64,null=False,default="offline")
    last_login = models.DateTimeField(auto_now=True)
    add_time = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.user

class Role(models.Model):
    """角色表"""
    role = models.CharField(max_length=64, unique=True)
    role_msg = models.CharField(max_length=128, null=True)
    perms = models.ManyToManyField(to='Permssions')
    asset = models.ManyToManyField(to=Asset)
    def __unicode__(self):
        return self.role

class Permssions(models.Model):
    """权限表"""
    perms = models.CharField(max_length=128)
    perms_img = models.CharField(max_length=64,null=True)
    perms_method = models.CharField(max_length=64, default="GET")
    perms_id = models.CharField(max_length=128)
    parent = models.ForeignKey(to="Permssions",on_delete=models.CASCADE,null=True)
    perms_type = models.CharField(max_length=64)
    status = models.CharField(max_length=64,default="正常")
    perms_url = models.CharField(max_length=256, null=True)
    def __unicode__(self):
        return  self.perms

