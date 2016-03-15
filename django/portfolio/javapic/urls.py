#we made this one


from django.conf.urls import url
from .views import *

urlpatterns = [
    
    url(r'^$', javapic_render),
    url(r'join/$', join_render),
    url(r'gallery', gallery_render)
]
