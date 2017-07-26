#-- coding: utf-8 --

from django.shortcuts import render_to_response

address = [{'name':'张三','address':'shanghai'},{'name':'李四','address':'常州'}]

def index(request):
    return render_to_response('list.html',{'address':address})