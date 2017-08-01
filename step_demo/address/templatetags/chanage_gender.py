#-- coding: utf-8 --
from django import template

register = template.Library()

def change_gender(value):
    if value == 'M':
        return '男'
    else:
        return '女'

register.filter("change_gender",change_gender)