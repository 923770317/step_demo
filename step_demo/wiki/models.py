#-- coding: utf-8 --
from __future__ import unicode_literals
from django.db import models

from django.db import models

# Create your models here.

class Wiki(models.Model):
    pagename = models.CharField(max_length=20,unique=True) #表示这个字段不能重复
    content = models.TextField()

