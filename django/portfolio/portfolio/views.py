from django.shortcuts import render


#We added this to handle the HttpResponse in this particular manner.
from django.http.response import HttpResponse

# Create your views here.

def zen_garden_render(request):
	return render(request, 'zen_garden/zen_mockup.html')

def javapic_render(request):
	return render(request, 'javapic/index.html')


def pricing_render():
	return render(request, 'pricing/pricing.html')