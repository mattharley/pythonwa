from django.conf.urls import url

from .views import TalkListView

import talks.views

urlpatterns = [
    url(r'^meetups/?$', talks.views.home_page, name='home-page'),
    url(r'^$', TalkListView.as_view(), name='talk-list'),
]
