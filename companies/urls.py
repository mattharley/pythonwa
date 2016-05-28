from django.conf.urls import url
from companies.views import company_list
from companies.views import company_create
from companies.views import company_edit
from companies.views import company_delete
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^companies/', 'pdpdmeetup.views.home', name='home'),
    
	url(r'^create/$', company_create, name='companies-create'),
	url(r'^companies/$', company_list, name='companies-home'),
	url(r'^companies-edit/(?P<id>\d+)/', company_edit, name='company-edit'),
	url(r'^companies-delete/$', company_delete, name='company-delete'),
]

urlpatterns += static ( settings.STATIC_URL, document_root = settings.STATIC_ROOT )
urlpatterns += static ( settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )