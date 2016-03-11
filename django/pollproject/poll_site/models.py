from django.db import models

# Create your models here.

class Question(models.Model):
	"""Defines the question class and model."""

	# Define the prop of the question Model
	# that are stored in the DB.
	question_text = models.CharField(max_length=200)
	
	pub_date = models.DateTimeField('date published')

class choice(models.Model):
	"""Defines the choice class and model. Ids are automagic."""

	choice_text = models.CharField(max_length=150)
	votes = models.PositiveSmallIntegerField(default=0)
	#Establish th one to many relationship from question to choice.
	#Picks up the auoto generated id in question automagically.
	question_id = models.ForeignKey(Question)
	# now after this we ran python3 manage.py makemigrations
	#in the virtual environment. then we ran
	#$python3 manage.py migrate


