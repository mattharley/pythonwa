from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Talk

class TalkListView(ListView):

    model = Talk
