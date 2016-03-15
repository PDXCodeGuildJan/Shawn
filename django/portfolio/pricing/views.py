
from django.shortcuts import render


#We added this to handle the HttpResponse in this particular manner.
from django.http.response import HttpResponse

# Create your views here.


def pricing_render(request):
	return render(request, 'pricing/pricing.html')
