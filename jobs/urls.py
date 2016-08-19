from django.conf.urls import url

import jobs.views

urlpatterns = [
    url(r'^jobs/?$', jobs.views.home_page, name='home-page'),
]
