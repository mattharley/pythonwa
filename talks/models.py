from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Talk(models.Model):
    name = models.CharField(max_length=200, help_text="Title of the talk")
    description = models.CharField(max_length=1000, help_text="Description of the talk")
    location = models.CharField(max_length=200, help_text="Location of talk")
    time = models.DateTimeField(help_text="Time when talk was or will be presented")
    presenters = models.ManyToManyField(
        settings.AUTH_USER_MODEL, help_text="The presenters of the talk"
    )

    def __str__(self):
        return "{0.name} - {0.time:%c}".format(self)
