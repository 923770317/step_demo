#-- coding: utf-8 --
from django.shortcuts import render
from step_demo.wiki.models import Wiki
from django.template import loader,Context
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

# Create your views here.

def index(request,pagename =''):
    if pagename:
        pages = Wiki.objects.filter(pagename = pagename)
        if pages:
            return process('page.html',pages[0])
        else:
            return render_to_response('edit.html',{'pagename':pagename})
    else:
        # page = Wiki.objects.get(pagename = 'FrontPage')
        page = Wiki.objects.get(pagename = 'FrontPage')
        # pages = Wiki.objects.all()
        return process('page.html',page)

def edit(request,pagename):
    page = Wiki.objects.get(pagename = pagename)
    return render_to_response('edit.html',{'pagename':pagename,'content':page.content})

def save(request,pagename):
    content = request.POST['content']
    pages = Wiki.objects.filter(pagename = pagename)
    if pages:
        pages[0].content = content
        pages[0].save()
    else:
        page = Wiki(pagename = pagename ,content = content)
        page.save()
    return HttpResponseRedirect("/wiki/%s" % pagename)

import re

r = re.compile(r'\b(([A-Z]+[a-z]+){2,})\b')
def process(template, page):
    """处理页面链接，并且将回车符转为<br>"""
    t = loader.get_template(template)
    content = r.sub(r'<a href="/wiki/\1">\1</a>', page.content)
    content = re.sub(r'[\n\r]+', '<br>', content)
    c = Context({'pagename':page.pagename, 'content':content})
    return HttpResponse(t.render(c))