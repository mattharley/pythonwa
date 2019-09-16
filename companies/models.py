from django.db import models


# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=100)
    abn = models.CharField(max_length=12)
    description = models.CharField(max_length=200)
    logo = models.ImageField(null=True, upload_to="images/")
