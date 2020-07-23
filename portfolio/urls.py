from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name  = 'home'

urlpatterns = [


    url(r'^$', views.portfolio, name= 'home'),


]
