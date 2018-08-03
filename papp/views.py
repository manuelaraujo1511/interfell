from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
	# IMPORTANTE: comprobar conexion a internet
	

	return render(request, 'index.html')

def login(request):
	return render(request, 'login.html')

def register(request):
	return render(request, 'register.html')	

def registro(request):

	if request.method == "POST":
		nombre = request.POST['nombre']
		apellido = request.POST['apellido']
		ciudad = request.POST['ciudad']
		nivel_academico = request.POST['nivel_academico']
		email = request.POST['email']
		password = request.POST['password']
		username = email

		'''
		if Usuarios.objects.filter(username=username).exists():
			messages.error(request, 'Nombre de Usuario ya existe')
			return render(request, 'registro.html')
		else:
		'''
		if Usuarios.objects.filter(email=email).exists():
			user = Usuarios.objects.get(email=email)
			if user.fin_registro == 1:
				messages.error(request ,'Email ya se encuentra registrado')
			else:

				if user.fin_registro == 0:
					if user.password == password:
						messages.success(request, 'Finaliza tu registro.')
						user = authenticate(request, username=username, password=password)
						login(request, user)
						context = {
							'username': username,
							'password' : password,
							'success':1
						}
						return render(request, 'registroinsta.html', context)
					else:
						messages.success(request, 'Puedes finalizar tu resgistro.')
						return render(request, 'singup.html',{'success':1})
		else:
			user = User.objects.create_user(username, email, password)
			user.first_name = nombre
			user.last_name = apellido
			user.save()

			u = Usuarios(nombre=nombre, apellido=apellido, email=email,password=password,username=username)
			u.save()
			user = authenticate(request, username=username, password=password)
			login(request, user)

			context = {
				'username': username,
				'password' : password
			}
			#messages.success(request, 'calida')
			return render(request, 'registroinsta.html', context)
	
	return render(request, 'registro.html')
	return render(request, 'register.html')	