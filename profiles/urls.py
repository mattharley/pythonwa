from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers

from .models import Profile
from .views import ProfileListView, ProfileViewSet, schema_view

router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet)

urlpatterns = [
                  url(r'^profiles/$', ProfileListView.as_view(queryset=Profile.objects.all()), name='profiles-page'),
                  url(r'^api/', include(router.urls)),
                  url(r'^api-docs/$', schema_view)
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
