from django.db import models
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.conf import settings
from pdpdmeetup.settings import MEDIA_URL
# Create your models here.
import datetime    

year_choices = []
for r in range(1980, (datetime.datetime.now().year+1)):
    year_choices.append((r,r))

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
	name = models.CharField(null=True, blank=True, max_length=100)
	photo = models.URLField(null=True, blank=True)
	email = models.EmailField(null=True, blank=True)
	frontend = models.TextField(null=True, blank=True)
	backend = models.TextField(null=True, blank=True)
	year_started_learning = models.IntegerField(('year_started_learning'), max_length=4, choices=year_choices, default=datetime.datetime.now().year)
	company = models.TextField(null=True, blank=True)

	def __str__(self):
		return '{0.name} - {0.email}'.format(self)

