from django.shortcuts import render

#We added this to handle the HttpResponse in this particular manner.
from django.http.response import HttpResponse

# Create your views here.

def hello_world(request):
	#VC must always take at least a HttpRequest
	#Alwys need to return a HttpResponse
	content = "<h1>Hello World!</h1><h2>Goodbye poverty.</h2>"
	return HttpResponse(content)

def hello_world_render(request):

	context = {'name': "Shaw Kinglove", 'fav_color': "Purple", 'toys': ['ax', 'mace', 'wings', 'torch', 'fountain']} #pased to template index.html

	return render(request, 'poll_site/index.html', context)

def linked_page(request):
	return render(request, 'poll_site/linked_page.html')

