from django.conf.urls import url

import sponsors.views


app_name = "sponsors"
urlpatterns = [url(r"^sponsors/?$", sponsors.views.home_page, name="home-page")]
