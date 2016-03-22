#we made this one


from django.conf.urls import url
from .views import *

urlpatterns = [
    
    url(r'^$', javapic_render, name='javapic'),
    url(r'join/$', join_render, name='join'),
    url(r'gallery', gallery_render, name='gallery')
]
