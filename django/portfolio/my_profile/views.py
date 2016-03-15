from django.shortcuts import render

# Create your views here.

def my_profile_render(request):
	return render(request, '/my_profile/profile.html')

def reality_render(request):
	return render(request, '/my_profile/reality.html')