from django.views.generic.list import ListView
from django.shortcuts import render

from .models import Talk


class TalkListView(ListView):
    model = Talk


def home_page(request):
    return render(
        request,
        'home-talks.html',
        {
        },

        # context_instance=RequestContext(request)
    )
