"""AnsbOps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path,include
from apps.sysmg import views

urlpatterns = [
    path("install/",views.ServerInstallView.as_view()),
    path("install/<int:page>/",views.ServerInstallView.as_view()),
    path("exec/",views.exec_script),
    path("batch/",views.BatchView.as_view()),
    path("runcmd/",views.batch_run_cmd),
    path('upfile/', views.batch_upload_file),
    path('script/', views.batch_script),
]
