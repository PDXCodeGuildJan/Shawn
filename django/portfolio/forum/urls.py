#we made this one


from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^$', render_forum)
]