from django.conf.urls import url
from . import views

urlpatterns = [url(r'^$', views.inicio, name='inicio'),
              url(r'^datos/$', views.datos, name='datos'),
	      url(r'^contacto/$', views.contacto, name='contacto'),
	      url(r'^elementos/$', views.elementos, name='elementos'),
	      url(r'^servicio/$', views.servicio, name='servicio'),
              url(r'^detalle/$', views.detalle, name='detalle'),
	      
	#url(r'^registar_terapeuta/$', views.registerTherapist, name='register_therapist'),
	#url(r'^consultar_paciente/$', views.searchPatient, name='search_patient'),
]
