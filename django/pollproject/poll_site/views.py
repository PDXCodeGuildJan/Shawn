from django.shortcuts import render, get_object_or_404 #we added the last one for url var passing?

#We added this to handle the HttpResponse in this particular manner.
from django.http.response import HttpResponse

#Allow getting things from DB
from .models import Question, Choice

# Create your views here.

def hello_world(request):
	#VC must always take at least a HttpRequest
	#Alwys need to return a HttpResponse
	content = "<h1>Hello World!</h1><h2>Goodbye poverty.</h2>"
	return HttpResponse(content)

def hello_world_render(request):

	#get things from db. 1st import the models
	questions = Question.objects.all()

	print(questions)
	#access to from one object to a related object is always objectname_set
	print(questions[0].choice_set.all)

	# questions[0].choice_set.all
	




	context = {'questions':questions,
		'name': "Shaw Kinglove", 'fav_color': "Purple", 'toys': ['ax', 'mace', 'wings', 'torch', 'fountain']} #pased to template index.html

	return render(request, 'poll_site/index.html', context)

def linked_page(request):
	return render(request, 'poll_site/linked_page.html')

def question_details(request, question_id):

	print("passed question", question_id)

	question = get_object_or_404(Question, pk=question_id)

	context = {
		'question': question,
	}

	return render(request, 'poll_site/question_details.html', context)