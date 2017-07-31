#-- coding: utf-8 --
from __future__ import unicode_literals

import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

from django.contrib import admin
from django.db import models

# Create your models here.
class Address(models.Model):
    name = models.CharField('姓名',max_length=30,unique=True)
    gender = models.CharField('性别',choices=(('M','男'),('F','女')),max_length=1)
    mobile = models.CharField('电话',max_length=11)
    email = models.EmailField('邮件',max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']

admin.site.register(Address)