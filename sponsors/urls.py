from django.conf.urls import url

import sponsors.views

urlpatterns = [
    url(r'^sponsors/?$', sponsors.views.home_page, name='home-page'),
]
