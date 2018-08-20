from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from interfell.routers import router
from django.urls import path, include

from . import views

app_name = 'papp'

urlpatterns = [
	url(r'^$', views.index, name='index'),	
	url(r'^login$', views.login, name='login'),
	url(r'^register$', views.register, name='register'),
	url(r'^singout$', views.singout, name='singout'),
	url(r'^edit$', views.edit, name='edit'),
	url(r'^get$', views.get, name='get'),
	path('users', TemplateView.as_view(template_name='index.html')),

]
