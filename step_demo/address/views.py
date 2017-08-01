#-- coding: utf-8 --
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import  render_to_response
from models import Address
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage
from django.http import request

# Create your views here.

#页面列表
def list(request):
    limit = 3
    addresses = Address.objects.all()
    pageinator = Paginator(addresses,limit)

    page = request.GET.get('page')
    try:
        addresses = pageinator.page(page)
    except PageNotAnInteger:
        addresses = pageinator.page(1)
    except EmptyPage:
        addresses = pageinator.page(pageinator.num_pages)
    return render_to_response("address_list.html",{"addresses":addresses})


def search(request):
    limit = 3
    # name = request.POST['search']
    name = request.GET['search']
    if name:
        addresses = Address.objects.filter(name__icontains=name)
        pageinator = Paginator(addresses, limit)
        page = request.GET.get('page')
        try:
            addresses = pageinator.page(page)
        except PageNotAnInteger:
            addresses = pageinator.page(1)
        except EmptyPage:
            addresses = pageinator.page(pageinator.num_pages)
        return render_to_response("address_list.html", {"addresses": addresses})
    else:
        return HttpResponseRedirect("/list/")

#上传
def upload(request):
    file_obj = request.FILES.get("file",None)
    print '111'
    print file_obj
    if file_obj:
        import csv
        import StringIO
        # buf = StringIO.StringIO(file_obj['content'])
        try:
            reader = csv.reader(file_obj,encoding='utf-8')
        except:
            return render_to_response('address/error.html',{'message':'你需要上传一个csv格式的文件！'})

        for row in reader:
#           objs = Address.objects.get_list(name__exact=row[0])
            objs = Address.objects.filter(name=row[0])
            if not objs:
                obj = Address(name=row[0], gender=row[1],
                    telphone=row[2], mobile=row[3], room=row[4])
            else:
                obj = objs[0]
                obj.gender = row[1]
                obj.telphone = row[2]
                obj.mobile = row[3]
                obj.room = row[4]
            obj.save()

        return HttpResponseRedirect('/address/')
    else:
        return render_to_response('address/error.html', {'message':'你需要上传一个文件！'})


#下载
