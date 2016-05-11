from django.conf.urls import url
from .models import Profile
from .views import ProfileListView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^profiles/$', ProfileListView.as_view(queryset=Profile.objects.all())),   
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 