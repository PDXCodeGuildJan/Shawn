#we made this one


from django.conf.urls import url
from .views import *

urlpatterns = [
    
    url(r'^$', my_profile_render, name='profile'),
    url(r'.reality', reality_render, name='reality'),

	]