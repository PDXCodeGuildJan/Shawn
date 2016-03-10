from django.shortcuts import render

# Create your views here.
def javapic_render(request):
	return render(request, 'javapic/index.html')