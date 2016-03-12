#we made this one


from django.conf.urls import url
from .views import *



urlpatterns = [
	url(r'^linked_page$', linked_page, name="linked_page"),
	#urldatapassingput into regex
	url(r'question(?P<question_id>[0-9]+)', question_details, name="question_details")
]