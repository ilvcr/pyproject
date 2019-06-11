from django.db import models

# Create your models here.

class ServerInstall(models.Model):
    server_name = models.CharField(max_length=128)
    server_version = models.CharField(max_length=128,null=True)
    install_script = models.TextField(null=True)
    def __unicode__(self):
        return self.server_name