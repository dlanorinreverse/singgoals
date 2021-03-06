from django.conf.urls import include, url
from django.contrib import admin

from .views import home

urlpatterns = [
	url(r'^$', home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^registration/', include('registration.urls')),
    url(r'^postinfo/', include('postinfo.urls')),
]
