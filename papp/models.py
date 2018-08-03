from django.db import models
from datetime import datetime


class Usuarios(models.Model):
	nombre = models.CharField( max_length = 100, blank = True, null = True) # blank para colocarlo como obligatorio, null o default para establecer valores por defecto
	apellido = models.CharField( max_length = 100, blank = True, null = True)
	email = models.EmailField()
	password = models.CharField( max_length = 16, blank = True, null = True )
	username = models.CharField( max_length = 100, blank = True, null = True )
	pais = models.CharField( max_length = 9, blank = True, null = True)
	nivel_academico = models.CharField( max_length = 100, blank = True, null = True)
	direccion = models.CharField( max_length = 1000, blank = True, null = True)
	
	#description = models.TextField( max_length = 300 )
	