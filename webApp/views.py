from django.shortcuts import render
from bokeh.plotting import figure
from bokeh.embed import components
import plots


# Create your views here.

def inicio(request):

	return render(request, 'webApp/index.html')

def liga(request):
	parameters = {}
	parameters.update(plots.plot_equipo())
	parameters.update(plots.plot_jugador())
		
	return render(request, 'webApp/services.html', parameters) 
	

def resultados(request):
	parameters = {}
	parameters.update(plots.plot_rango())
	#parameters.update(plots.plot_proyeccion())	

	return render(request, 'webApp/services_1.html', parameters) 


def apuestas(request):
	return render(request, 'webApp/blog.html')

def contacto(request):
	return render(request, 'webApp/contact.html')





