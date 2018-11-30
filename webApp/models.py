from django.db import models

# Create your models here.
	
class equipo (models.Model):
	EquipoLocal = models.TextField(max_length=30)
	EquipoVisitante = models.TextField(max_length=30)
	

class goles (models.Model):
	golesLocal = models.TextField(max_length=10)
	golesVisitante = models.TextField(max_length=10)


class equipo_ciudad (models.Model):
	Equipo = models.TextField(max_length=10)
	Ciudad = models.TextField(max_length=10)
	
