from django.shortcuts import render


#We added this to handle the HttpResponse in this particular manner.
from django.http.response import HttpResponse

# Create your views here.

def landing_page_render(request):
	return render(request, 'portfolio/index.html')

"""
def zen_garden_render(request):
	return render(request, 'zen_garden/zen_mockup.html')

def javapic_render(request):
	return render(request, 'javapic/index.html')

def pricing_render(request):
	return render(request, 'pricing/pricing.html')

def my_profile_render(request):
	return render(request, 'my_profile/profile.html')
"""