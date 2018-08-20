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

	todos_usuarios = Usuarios.objects.all()
	context={
	'usuarios': todos_usuarios
	}
	return render(request, 'index.html', context)

def login(request):
	if request.method == "POST":
		email = request.POST['email']
		password = request.POST['password']
		try:

			user_u = Usuarios.objects.get(email=email)
			user_name=user_u.username

		
			if user_name is not False:
				user = authenticate(request, username=user_name, password=password)
				if user:
					auth_login(request, user)
					return redirect('papp:index')
				else:
					messages.error(request, 'Datos Incorrectos, Intente de Nuevo')
				return render(request, 'login.html')	
			else:
				messages.error(request, 'Datos Incorrectos, Intente de Nuevo')
				return render(request, 'login.html')	
			
		except ObjectDoesNotExist:
			messages.error(request, 'Datos Incorrectos, Intente de Nuevo.')
			return render(request, 'login.html')

	return render(request, 'login.html')
		

@login_required
def singout(request):
	logout(request)
	
	return redirect('papp:login')
	

def register(request):
	if request.method == "POST":
		nombre = request.POST['nombre']
		apellido = request.POST['apellido']
		pais = request.POST['pais']
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

def get(request):
	if request.method == "POST":
		if request.is_ajax():
			id_user = request.POST.get('id')
			user = Usuarios.objects.get(id=id_user)
			usuario = {'nombre': user.nombre,'apellido':user.apellido, 'pais': user.pais,  'ciudad': user.ciudad, 'nivel_academico': user.nivel_academico}
			context = {'usuario':usuario}
			return JsonResponse(context)

def edit(request):
	if request.method == "POST":
		id_user = request.POST['id_user']
		nombre = request.POST['nombre']
		apellido = request.POST['apellido']
		pais = request.POST['pais']
		ciudad = request.POST['ciudad']
		nivel_academico = request.POST['nivel_academico']
		user = Usuarios.objects.filter(id=id_user)	

		for u in user:			

			u.nombre = nombre
			u.apellido=apellido
			u.pais= pais
			u.ciudad=ciudad
			u.nivel_academico= nivel_academico
			u.save()
			estado=1
		
		context={'estado': estado}
		return redirect("papp:index")
