Python Installation (Windows)
=============================

Python 3.5.1 is the latest version as of this writing.

- Download Python 3.5.1 from www.python.org
- Double-click the python-3.5.1.msi to begin installation.
- IMPORTANT! Tick **Add Python 3.5 to  PATH** or else the **python** won't be found in the **Command Prompt**.
- Open start menu search for **Command Prompt** and execute it.
- Enter **python** and the interactive shell will appear and Python code can be written in it.
- Enter **exit()** to exit the shell.

Django installation
-------------------

- pip install django

Create Project
--------------

```
python manage.py startproject 
```

Instantiate Database
--------------------

```
python manage.py migrate 
```

Run Server
----------

Go to project folder:

```
python manage.py runserver
```

Check Admin
-----------

Create superuser:

```
python manage.py createsuperuser
```

In project folder, find **pdpd/urls.py**, see how the **/admin/** URL is defined.

Check it out in **localhost:8000/admin/**, and login with the newly created super user.

Create CRM app
--------------
In project folder:

```
python manage.py startapp crm
```

Edit **pdpd/settings.py**:

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crm',
]
```


Create Event Views for CRM app
------------------------------

In **pdpd/urls.py**:

```
from crm.views import event_add
from crm.views import event_list

urlpatterns = [
    url(r'^$', event_list),
    url(r'^add/$', event_add),
    url(r'^admin/', admin.site.urls),
]
```

In **crm/views.py**

```
from django.http import HttpResponse
from django.shortcuts import render

def event_add(request):
    return HttpResponse('page for adding events')

def event_list(request):
    return HttpResponse('page for listing events')
```

Create Event Model & Form
-------------------------

3 Steps in model creation.
1. Defining it as a Python model (class Event)
2. Generating the SQL required to create the SQL table (manage.py makemigrations)
3. Actually creating the SQL table (manage.py migrate)

In **crm/models.py**

```
from django.db import models

class Event(models.Model):
    name = models.CharField()
```

```
python manage.py makemigrations
python manage.py migrate 
```

In **crm/forms.py**

```
from django import forms

from crm.models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name']
```

Make Event views more useful
----------------------------

```
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from crm.forms import EventForm
from crm.models import Event

def event_add(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add')
    else:
        form = EventForm()
    return render(request, 'crm/event_add.html', {
        'number': 123,
        'form': form,
    })

def event_list(request):
    events = Event.objects.all()
    return render(request, 'crm/event_list.html', {
        'events': events,
    })
```

Add more fields to Event model
------------------------------

In **crm/models.py**:

'''
from django.db import models
from django.utils.timezone import now


class Event(models.Model):
    name = models.CharField(max_length=100)
    datetime = models.DateTimeField(default=now)
'''

'''
python manage.py makemigrations
python manage.py migrate
'''
