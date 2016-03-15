from django.shortcuts import render

# Create your views here.

def javapic_render(request):
	return render(request, 'javapic/index.html')


def join_render(request):
	return render(request, 'javapic/join.html')

def gallery_render(request):
	return render(request, 'javapic/gallery.html')