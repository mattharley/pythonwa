from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Company
from .forms import CompanyForm
from .forms import CompanyEditForm

import json


# Create your views here.


def company_create(request):
    form = CompanyForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        Company.objects.create(
            name=form.cleaned_data.get("name"),
            abn=form.cleaned_data.get("abn"),
            description=form.cleaned_data.get("description"),
            logo=request.FILES['logo']
        )

        messages.success(request, 'Record successfully created')

        return redirect(company_list)

    context = {
        "title": "Create a new Company",
        "form": form,
    }

    return render(request, "companies-create.html", context)


def company_edit(request, id=None):
    instance = get_object_or_404(Company, id=id)

    form = CompanyEditForm(request.POST or None, request.FILES or None)
    form.fields['name'].initial = instance.name
    form.fields['abn'].initial = instance.abn
    form.fields['description'].initial = instance.description
    form.fields['logo'].initial = instance.logo

    if form.is_valid():
        instance.name = form.cleaned_data.get("name")
        instance.abn = form.cleaned_data.get("abn")
        instance.description = form.cleaned_data.get("description")
        instance.logo = form.cleaned_data.get("logo")

        instance.save()

        messages.success(request, 'Record successfully updated')

        return redirect(company_list)

    context = {
        "title": "Updating Form",
        "tabtitle": "Company Update",
        "form": form
    }

    return render(request, "companies-edit.html", context)


def company_list(request):
    queryset = Company.objects.all()

    context = {

        "object_list": queryset,
        "count": queryset.count(),
        "title": "Companies List"

    }

    return render(request, "home-companies.html", context)


def company_delete(request):
    response = {}

    if request.method == 'POST':
        company_id = request.POST.get('id')
        instance = get_object_or_404(Company, id=company_id)
        instance.delete()
        response['id'] = company_id
        response['result'] = '1'

    return HttpResponse(json.dumps(response), content_type="application/json")
