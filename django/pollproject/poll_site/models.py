from django.db import models

# Create your models here.

class Question(models.Model):
	"""Defines the question class and model."""

	# Define the prop of the question Model
	# that are stored in the DB.
	question_text = models.CharField(max_length=200)
	
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		"""Return a string"""
		return self.question_text

class Choice(models.Model):
	"""Defines the choice class and model. Ids are automagic."""

	choice_text = models.CharField(max_length=150)
	votes = models.PositiveSmallIntegerField(default=0)
	#Establish th one to many relationship from question to choice.
	#Picks up the auoto generated id in question automagically.
	question_id = models.ForeignKey(Question)
	# now after this we ran python3 manage.py makemigrations
	#in the virtual environment. then we ran
	#$python3 manage.py migrate

	#Next we look into the db using the admin portfolio
	#(poll_site) shawnwaldow@shawnwaldow-K53E:~/Documents/CodeSchool/Week1/django/pollproject$ python3 manage.py createsuperuser
	#point browser to http://127.0.0.1:8000/admin/
	def __str__(self):
		"""Return a string"""
		return self.choice_text





