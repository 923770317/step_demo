"""step_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import add
import list_demo
import csv_test
import login

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^add/$', add.index),
    url(r'^list/$', list_demo.index),
    url(r'^login/$', login.login),
    url(r'^logout1/$', login.logout1),
    url(r'^csv/(?P<filename>\w+)/$', csv_test.output),
]
