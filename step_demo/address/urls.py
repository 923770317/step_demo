
from django.conf.urls import url
from models import Address
import views

# info_dict = {'queryset':Address.objects.all()}
address = Address.objects.all()

urlpatterns = [
    url(r'^/?$',views.list), url(r'^upload/$', views.upload),]
