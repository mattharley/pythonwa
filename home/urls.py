from django.conf.urls import url
from home.views import home_page, ajax_meetups_tab
from django.conf.urls.static import static
from django.conf import settings

import home.views

urlpatterns = [
    url(r'^$', home.views.home_page, name='home-page'),
    url(r'^getinvolved/?$', home.views.get_involved, name='get-involved'),
    url(r'/meetupsapi/(?P<event_status>\w+)/?$', ajax_meetups_tab, name='ajax_meetups_tab'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
