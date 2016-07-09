from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    # Examples:
    # url(r'^$', 'pdpdmeetup.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('talks.urls')),
    url(r'^', include('companies.urls')),   
    url(r'^', include('profiles.urls')),
    url(
        r'^\.well-known/acme-challenge/fWHI3SJWItBWKR9khrIM0ICS4ZzR0T6k-z0P84SksYM', 
        TemplateView.as_view(template_name="ssl.html")
    )
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

