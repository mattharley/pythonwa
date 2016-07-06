from django.http import HttpResponse
from django.shortcuts import render,  get_object_or_404
from django.core.urlresolvers import reverse
from .models import Company
from .forms  import CompanyForm
from .forms  import CompanyEditForm

from django.shortcuts import redirect
from django.contrib import messages
import json

# Create your views here.

def company_create(request):
	form = CompanyForm(request.POST or None, request.FILES or None)

	if form.is_valid():
		company_name = form.cleaned_data.get("name")
		company_abn  = form.cleaned_data.get("abn")
		company_description = form.cleaned_data.get("description")
		company_logo = request.FILES['logo']

		instance = Company.objects.create()
		instance.name = company_name
		instance.abn = company_abn
		instance.description = company_description
		instance.logo = company_logo
		instance.save()

		form = CompanyForm( None, None)
		messages.success(request, 'Record succesfully created');

	context = {
		"title" : "Create a new Company",
		"form" : form,
	}

	return render(request, "companies-create.html", context )


def company_edit(request, id=None):
	
	instance = get_object_or_404(Company, id=id)

	form = CompanyEditForm(request.POST or None, request.FILES or None)
	form.fields['name'].initial = instance.name
	form.fields['abn'].initial = instance.abn
	form.fields['description'].initial = instance.description
	form.fields['logo'].initial = instance.logo



	if form.is_valid():
		company_name = form.cleaned_data.get("name")
		company_abn = form.cleaned_data.get("abn")
		company_description = form.cleaned_data.get("description")
		company_logo = form.cleaned_data.get("logo")

		if company_logo:
			instance.name = company_name
			instance.abn = company_abn
			instance.description = company_description
			instance.logo = company_logo
			instance.save()
		else:
			instance.name = company_name
			instance.abn = company_abn
			instance.description = company_description
			instance.save()

		messages.success(request, 'Record succesfully updated');
		#return redirect(company_list)
		

	context = {
		"title":    "Updating Form",
		"tabtitle": "Company Update",
		"form":     form
	}
	
	return render(request, "companies-edit.html", context)


def company_list(request):
	queryset = Company.objects.all()
	
	context = {

		"object_list" : queryset,
		"count" : queryset.count(),
		"title" : "Companies List"
	
	}

	return render(request, "companies-index.html", context)


def company_delete(request):
	
	response = {}
	
	if request.method == 'POST':
		company_id = request.POST.get('id')
		instance = get_object_or_404(Company, id=company_id)
		instance.delete()
		response['id'] = company_id
		response['result'] = '1'


	return HttpResponse( json.dumps( response ), content_type="application/json")