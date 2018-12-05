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









