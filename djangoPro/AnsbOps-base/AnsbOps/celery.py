from __future__ import absolute_import, unicode_literals

import os
from celery import Celery,platforms
from django.conf import settings

platforms.C_FORCE_ROOT = True
# 设置django环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AnsbOps.settings')
app = Celery('AnsbOps')
# 使用CELERY_ 作为前缀，在settings中写配置
app.config_from_object('django.conf:settings',force=True,)
# 从所有已注册的Django应用程序配置中加载任务模块。
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
