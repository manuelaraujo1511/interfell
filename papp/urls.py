from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

app_name = 'papp'

urlpatterns = [
	url(r'^$', views.index, name='index'),	
	url(r'^login$', views.login, name='login'),
	url(r'^register$', views.register, name='register'),
	url(r'^registro$', views.registro, name='registro'),
]
