from django.conf.urls import url
from home.views import home_page
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^companies/', 'pdpdmeetup.views.home', name='home'),
    
	url(r'^$', home_page, name='home-page'),
]

urlpatterns += static ( settings.STATIC_URL, document_root = settings.STATIC_ROOT )
urlpatterns += static ( settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )