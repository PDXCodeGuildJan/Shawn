#we made this one


from django.conf.urls import url
from .views import *

urlpatterns = [
    
    url(r'^$', my_profile_render),
    url(r'^reality$', reality_render),

	]