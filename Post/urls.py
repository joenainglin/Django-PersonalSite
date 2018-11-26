from django.conf.urls import url
from . import views


app_name = 'Post'

urlpatterns = [
		# map to Post list view
		url(r'^$', views.MainPost, name = 'MainPost'),
		url(r'^Feature$', views.AllFeaturePost, name = 'AllFeaturePost'),
		url(r'^Contact$', views.ContactUs, name = 'ContactUs'),
		url(r'^About$', views.AboutUs, name = 'AboutUs'),
		]