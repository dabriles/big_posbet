from django.conf.urls import url
from . import views

urlpatterns = [url(r'^$', views.inicio, name='inicio'),
              url(r'^liga/$', views.liga, name='liga'),
	      url(r'^resultados/$', views.resultados, name='resultados'),
	      url(r'^apuestas/$', views.apuestas, name='apuestas'),
	      url(r'^contacto/$', views.contacto, name='contacto'),
	      url(r'^servicio/$', views.servicio, name='servicio'),

	      
	#url(r'^registar_terapeuta/$', views.registerTherapist, name='register_therapist'),
	#url(r'^consultar_paciente/$', views.searchPatient, name='search_patient'),
]
