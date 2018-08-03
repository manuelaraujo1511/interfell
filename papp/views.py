from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
	# IMPORTANTE: comprobar conexion a internet
	

	return render(request, 'index.html')

def login(request):
	return render(request, 'login.html',)

def register(request):
	return render(request, 'register.html',)	