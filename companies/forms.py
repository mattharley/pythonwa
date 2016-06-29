from django import forms
from PIL import Image
import datetime 


class CompanyForm(forms.Form):
	name = forms.CharField()
	abn = forms.IntegerField()
	description = forms.CharField(widget=forms.Textarea)
	logo = forms.ImageField()


class CompanyEditForm(forms.Form):
	name = forms.CharField()
	abn = forms.IntegerField()
	description = forms.CharField(widget=forms.Textarea)
	logo = forms.ImageField(required=False)


