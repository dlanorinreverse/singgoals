from django.conf.urls import url

from .views import upload_info, to_upload_info

urlpatterns = [
	url(r'^uploadinfo/$', upload_info, name='upload_info'),
	url(r'^touploadinfo/$', to_upload_info, name='to_upload_info'),
]
