from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.core.properties import value
from bokeh.models import ColumnDataSource
from bokeh.transform import dodge



# Create your views here.

def plot_equipo():

	x = [i for i in range(2016,2020)]
	y = [6, 10, 17, 21]

	title_ = "Indicadores por Equipo"
	x_axis = "Equipo"
	y_axis = "Indicadores"
	width = 500
	height = 350

	plot = figure(title= title_, x_axis_label= x_axis, y_axis_label= y_axis, plot_width= width, plot_height= height)

	plot.circle(x, y)
	plot.line(x, y, legend= '', line_width =1)

	script_1, div_1 =components(plot)

	graphic = {"script_equipo":script_1, "div_equipo":div_1}
	
	return graphic


def plot_jugador():

	x = [i for i in range(2016,2020)]
	y = [6, 10, 17, 21]

	title_ = "Indicadores por Jugador"
	x_axis = "Jugador"
	y_axis = "Indicadores"
	width = 500
	height = 350

	plot_1 = figure(title= title_, x_axis_label= x_axis, y_axis_label= y_axis, plot_width= width, plot_height= height)

	plot_1.circle(x, y)
	#plot.line(x, y, legend= '', line_width =1)

	script_2, div_2 =components(plot_1)

	graphic = {"script_jugador":script_2, "div_jugador":div_2}
	
	return graphic


def plot_rango():
	
	years = [str(i) for i in range(2016,2020)]
	states = ['Equipo1', 'Equipo2']

	equipo1 = [6, 10, 17, 20]
	equipo2 = [2, 4, 5, 10]

	data= {'years' : years, 'Equipo1' : equipo1, 'Equipo2' : equipo2}  
	source_ = ColumnDataSource(data= data)

	title_ = "Rango por Equipo"
	x_axis = "Años"
	y_axis = "Equipos"
	width = 500
	height = 350


	plot = figure(title= title_, x_axis_label= x_axis, x_range= years, y_axis_label= y_axis, plot_width= width, plot_height= height)

	colors = {'Equipo1' : "#718dbf", 'Equipo2' : "#e84d60"}
	location = 0
	for state in states:
		plot.vbar(x=dodge('years', location, range=plot.x_range), top=state, width=0.2, source= source_, color=colors[state], legend=value(state))
	
	plot.legend.location = "top_left"
	plot.legend.orientation = "horizontal"
	plot.xgrid.grid_line_color = None

	script, div = components(plot)
	graphic = {"script_rango" : script, "div_rango" : div}

	return graphic




































