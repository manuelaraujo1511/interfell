from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseForbidden
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext
from django.contrib.auth.hashers import *
from django.template.loader import render_to_string
from django.contrib.auth import login as auth_login

from django.contrib.auth.decorators import login_required

from .models import *
# Create your views here.

@login_required
def index(request):
	# IMPORTANTE: comprobar conexion a internet
	

	return render(request, 'index.html')

def login(request):
	return render(request, 'login.html')

def register(request):
	if request.method == "POST":
		nombre = request.POST['nombre']
		apellido = request.POST['apellido']
		ciudad = request.POST['ciudad']
		nivel_academico = request.POST['nivel_academico']
		email = request.POST['email']
		password = request.POST['password']
		username = email
		if Usuarios.objects.filter(email=email).exists():
			messages.error(request ,'Email ya se encuentra registrado')
		else:
			user = User.objects.create_user(username, email, password)
			user.first_name = nombre
			user.last_name = apellido
			user.save()
			u = Usuarios(nombre=nombre, apellido=apellido, email=email,password=password,username=username, ciudad=ciudad, nivel_academico=nivel_academico)
			u.save()
			userr = authenticate(request, username=username, password=password)
			auth_login(request, userr)
			return redirect("papp:index")
	else:
		return render(request, 'register.html')	
