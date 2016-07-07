from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Examples:
    # url(r'^$', 'pdpdmeetup.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('talks.urls')),
    url(r'^', include('companies.urls')),   
    url(r'^', include('profiles.urls')),    
    url(r'^demos/', include('demos.urls')),   
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

