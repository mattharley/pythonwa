from django.conf.urls import url

from .views import TalkListView

urlpatterns = [
    url(r'^$', TalkListView.as_view(), name='talk-list'),
]