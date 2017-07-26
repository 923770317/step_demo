#-- coding: utf-8 --
from django.shortcuts import render_to_response
from django.template import loader,Context
from django.http import HttpResponse

address = [('张三','shanghai'),('李四','常州')]

def output(request,filename):
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attachment; filename=%s.csv' % filename

    t = loader.get_template('csv.html')
    c = Context({'data':address,})

    response.write(t.render(c))
    return response
