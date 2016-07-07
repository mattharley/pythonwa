from django.conf.urls import url

from .views import DivideByView, SleepView

urlpatterns = [
    url(r'^divide$', DivideByView.as_view(), name='divide'),
    url(r'^sleep$', SleepView.as_view(), name='sleep'),
]