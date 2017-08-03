from django.shortcuts import render
from django.views.generic.list import ListView

from rest_framework import viewsets
from rest_framework_swagger.views import get_swagger_view

from .models import Profile
from .serializers import ProfileSerializer

class ProfileListView(ListView):
    model = Profile

class ProfileViewSet(viewsets.ModelViewSet):
    model = Profile
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

schema_view = get_swagger_view(title='Profiles API')