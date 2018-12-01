from django.db import models
from django.db import connection

# Create your models here.

class equipoManager(models.Manager):
	def create_equipo(self,id_,EquipoLocal_, EquipoVisitante_):
		equipo = Equipo(id_equipo = id_, EquipoLocal = EquipoLocal_, EquipoVisitante = EquipoVisitante_)
		return equipo

	def get_equipos(self):
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM webApp_equipo;")
		equipos = cursor.fetchall()
		return equipos

	def get_equipo_by_id(self, id_):
		cursor = connection.cursor()
		cursor.execute("SELECT wepApp_equipo.id AS id, webApp_equipo.EquipoLocal AS local, webApp_equipo.EquipoVisitante AS visitante FROM webApp_equipo WHERE id_equipo = %s;", [id_])



class equipo (models.Model):
	id_equipo = models.IntegerField()
	EquipoLocal = models.TextField(max_length=30)
	EquipoVisitante = models.TextField(max_length=30)
	

class goles (models.Model):
	id_goles = models.IntegerField()
	golesLocal = models.TextField(max_length=10)
	golesVisitante = models.TextField(max_length=10)


class equipo_ciudad (models.Model):
	id_ciudad = models.IntegerField()
	Equipo = models.TextField(max_length=10)
	Ciudad = models.TextField(max_length=10)
	
