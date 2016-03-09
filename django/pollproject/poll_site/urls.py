#we made this one


from django.conf.urls import url
from .views import *



urlpatterns = [
	url(r'^linked_page$', linked_page, name="linked_page"),
]