<<<<<<< HEAD
# DjangoDB

# Database configuration
``
In settings.py file you can edit the ENGINE parameter used for DATABASES
``
# Manging migrations
``
python manage.py migrate
``
<br>
# Manage changes to app
add app to installed apps in settings.py
 
``
INSTALLED_APPS = [
``
<br>
``
  'django.contrib.admin',
``
<br>
``
 'django.contrib.auth',
``
<br>
``
   'django.contrib.contenttypes',
``
<br>
``
  'django.contrib.sessions',
``
<br>
``
    'django.contrib.messages',
``
<br>
``
  'django.contrib.staticfiles',
``
<br>
``
   'first_app'
``
<br>
``
]
``
<br>
<br>
``
python manage.py makemigrations app1
``
<br>
``
 python manage.py sqlmigrate polls 0001
``
<br>
``
python manage.py migrate
``
# Admin interface
``
from app. models import Model1, Model2 
``
<br>
``
admin.site.register(Model1)
``
<br>
``
admin.site.register(Model2)
``
# To use DB you need a Superuser
``
python manage.py createsuperuser
``
# Check if postgresql is running
``
/etc/init.d/postgresql status (start/stop)
``
# Getting started with postgresql
``
postgres=#create user no_two with login password 'qwerty';
``
https://www.freecodecamp.org/news/how-to-get-started-with-postgresql-9d3bc1dd1b11/

# Getting started with models and creating test data using shell
``
python manage.py shell
``
<br>
``
from first_app.models import Topic
``
<br>
``
print(Topic.objects.all())
``
<br>
``
t = Topic(topic_name.objects.all())
``
<br>
``
t.save()
``
<br>
``
t.id
``
<br>

from polls.models import Choice, Question

# Make sure our __str__() addition worked.
Question.objects.all()
<br>
<QuerySet [<Question: What's up?>]>

# Django provides a rich database lookup API that's entirely driven by
# keyword arguments.
Question.objects.filter(id=1)
<br>
<QuerySet [<Question: What's up?>]>
<br>
Question.objects.filter(question_text__startswith='What')
<br>
<QuerySet [<Question: What's up?>]>

# Get the question that was published this year
from django.utils import timezone
<br>
 current_year = timezone.now().year
<br>
Question.objects.get(pub_date__year=current_year)
<Question: What's up?>

# Request an ID that doesn't exist, this will raise an exception.
Question.objects.get(id=2)
<br>
Traceback (most recent call last):
<br>
DoesNotExist: Question matching query does not exist.

# Lookup by a primary key is the most common case, so Django provides a shortcut for primary-key exact lookups. The following is identical to Question.objects.get(id=1).
Question.objects.get(pk=1)
<br>
<Question: What's up?>

# Make sure our custom method worked.
q = Question.objects.get(pk=1)
<br>
q.was_published_recently()
<br>
True

# Give the Question a couple of Choices. The create call constructs a new
# Choice object, does the INSERT statement, adds the choice to the set
# of available choices and returns the new Choice object. Django creates
# a set to hold the "other side" of a ForeignKey relation
# (e.g. a question's choice) which can be accessed via the API.
>>> q = Question.objects.get(pk=1)

# Display any choices from the related object set -- none so far.
>>> q.choice_set.all()
<QuerySet []>

# Create three choices.
 q.choice_set.create(choice_text='Not much', votes=0)
 <br>
<Choice: Not much>
<br>
q.choice_set.create(choice_text='The sky', votes=0)
<br>
<Choice: The sky>
<br>
c = q.choice_set.create(choice_text='Just hacking again', votes=0)

# And vice versa: Question objects get access to Choice objects.
q.choice_set.all()
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
q.choice_set.count()
3

# The API automatically follows relationships as far as you need.
 Use double underscores to separate relationships.
This works as many levels deep as you want; there's no limit.
Find all Choices for any question whose pub_date is in this year
(reusing the 'current_year' variable we created above).
Choice.objects.filter(question__pub_date__year=current_year)
<br>
``<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
``
# Let's delete one of the choices. Use delete() for that.
c = q.choice_set.filter(choice_text__startswith='Just hacking')
<br>
c.delete()
<br>
``
print(Topic.objects.all())
``
# Creating admin panel with superuser
``
python manage.py createsuperuser
``
<br>
``
python manage.py runserver
``
<br>
``
127.0.0.1/admin
``
# Scripting 
create a populate script, import faker write script see example in populate_first_app.py then run scrpt and see changes
<br>
``
python populate.py
``
<br>
``
python manage.py
``
<br>
``
python manange.py runserver
//checkout /admin
``
=======
# ModelForms
>>>>>>> 900120dd0e9a14fc383130cc0c355ea4197410c8
