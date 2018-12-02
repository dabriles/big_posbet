from django.shortcuts import render

from bokeh.plotting import figure
from bokeh.embed import components



# Create your views here.
def inicio(request):
	return render(request, 'webApp/index.html')

def liga(request):
	
	x = [i for i in range(2016,2020)]
	y = [6, 10, 17, 21]

	title_plot_1 = ""
	x_axis_1 = "Años"
	y_axis_1 = "Goles"
	plot_1_width = 500
	plot_1_height = 350

	plot_1 = figure(title= title_plot_1, x_axis_label= x_axis_1, y_axis_label= y_axis_1, plot_width= plot_1_width, plot_height= plot_1_height)

	plot_1.circle(x, y)
	plot_1.line(x, y, legend= '', line_width =2)

	script_1, div_1 =components(plot_1)

	return render(request, 'webApp/services.html', {'script_plot_1': script_1, 'div_plot_1' : div_1}) 






def resultados(request):
	x = [i for i in range(2016,2020)]
	y = [6, 10, 17, 21]

	title_plot_1 = ""
	x_axis_1 = "Años"
	y_axis_1 = "Goles"
	plot_1_width = 500
	plot_1_height = 350

	plot_1 = figure(title= title_plot_1, x_axis_label= x_axis_1, y_axis_label= y_axis_1, plot_width= plot_1_width, plot_height= plot_1_height)

	plot_1.circle(x, y)
	plot_1.line(x, y, legend= '', line_width =2)

	script_1, div_1 =components(plot_1)

	return render(request, 'webApp/services.html', {'script_plot_1': script_1, 'div_plot_1' : div_1}) 


def apuestas(request):
	return render(request, 'webApp/blog.html')

def contacto(request):
	return render(request, 'webApp/contact.html')



