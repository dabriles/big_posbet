from django.conf.urls import url
from . import views

urlpatterns = [url(r'^$', views.index, name='index'),
	#url(r'^registar_terapeuta/$', views.registerTherapist, name='register_therapist'),
	#url(r'^consultar_paciente/$', views.searchPatient, name='search_patient'),
]
