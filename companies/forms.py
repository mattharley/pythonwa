from django import forms
from PIL import Image
from django.core.validators import MaxLengthValidator, RegexValidator
import datetime

name_validation = RegexValidator(r"^[A-Za-z ]{1,100}$")
abn_validation = RegexValidator(r"^[0-9]{12,12}$")
description_validation = RegexValidator(r"^[A-Za-z0-9 .\"'?!,@$-]{1,200}$")


class CompanyForm(forms.Form):
    name = forms.CharField(validators=[name_validation])
    abn = forms.CharField(validators=[abn_validation])
    description = forms.CharField(widget=forms.Textarea, validators=[description_validation])
    logo = forms.ImageField()


class CompanyEditForm(forms.Form):
    name = forms.CharField(validators=[name_validation])
    abn = forms.IntegerField(validators=[abn_validation])
    description = forms.CharField(widget=forms.Textarea, validators=[description_validation])
    logo = forms.ImageField(required=False)
