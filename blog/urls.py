from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name  = 'blog'

urlpatterns = [


    url(r'^$', views.blog, name= 'all_blogs'),

    url(r'^(?P<blog_id>\d+)/$', views.detail, name= 'detail'),

]
