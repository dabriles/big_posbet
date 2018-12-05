from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.core.properties import value
from bokeh.models import ColumnDataSource
from bokeh.transform import dodge
import pandas as pd
from math import pi
from bokeh.palettes import Category20c
from bokeh.transform import cumsum


# Create your views here.


def plot_equipo():

	df =pd.read_csv('/home/dsabrile/Escritorio/Data Set/v2/datosequipo.csv',header=0)
	#print (datos1['tempo.rada'])	
	
	
	df_f = df [ df['EquipoLocal'] == 'Barcelona']
	temporadas = df [ df['EquipoLocal'] == 'Barcelona'].drop_duplicates('temporada')
	
	
	x_t = temporadas['temporada']
	x = []	

	for x_ in x_t:
		x.append(int(x_.split("-")[0]))

	y_local = []
	y_visitante = []

	goles_local = df_f.groupby(['temporada'], sort=False)[['golesLocal']].sum() 
	y_ = goles_local['golesLocal']

	goles_local = df_f.groupby(['temporada'], sort=False)[['golesVisitante']].sum() 
	y_2 = goles_local['golesVisitante']

	for gl in y_:
		y_local.append(gl)

	for gl in y_2:
		y_visitante.append(gl)
#	
	title_ = "Indicadores por Equipo"
	x_axis = "Años"
	y_axis = "Goles"
	width = 500
	height = 350

	print(x)
	print(y_local)
	print(y_visitante)

	plot = figure(title= title_, x_axis_label= x_axis, y_axis_label= y_axis, plot_width= width, plot_height= height)

	plot.circle(x, y_local)
	plot.line(x, y_local, legend= 'Local', line_width =1, color='#00FF88')

	plot.circle(x, y_visitante)
	plot.line(x, y_visitante, legend= 'Visitante', line_width =1, color='#660088')

	script_1, div_1 =components(plot)

	graphic = {"script_equipo":script_1, "div_equipo":div_1}
	
	return graphic


def plot_jugador():


	df =pd.read_csv('/home/dsabrile/Escritorio/Data Set/v2/datosjugador.csv',header=0)
	
	df_f = df [ df['Equipo'] == 'Barcelona']
	df_f_ = df [ df['jugador'] == 'Messi']

	
	x_t = df_f_['Jornada']
	x = []	

	for x_ in x_t:
		x.append(int(x_))
	
	
	y = []
	y_t =df_f_ ['Min jugados']

	for y_ in y_t:
		y.append(float(y_.replace(',','.')))
	
	
		
	
	title_ = "Indicadores por Jugador"
	x_axis = "Jornada"
	y_axis = "Minutos"
	width = 500
	height = 350

	plot_1 = figure(title= title_, x_axis_label= x_axis, y_axis_label= y_axis, plot_width= width, plot_height= height)

	plot_1.circle(x, y)
	#plot.line(x, y, legend= '', line_width =1)

	script_2, div_2 =components(plot_1)

	graphic = {"script_jugador":script_2, "div_jugador":div_2}
	
	return graphic


def plot_rango():
	
	df =pd.read_csv('/home/dsabrile/Escritorio/Data Set/v2/datosequipo.csv',header=0)	

	df_f = df [ (df['EquipoLocal'] == 'Barcelona')& (df['EquipoVisitante'] == 'Atletico de Madrid')]
	temporadas = df [ df['EquipoLocal'] == 'Barcelona'].drop_duplicates('temporada')	
	

	x_t = temporadas['temporada']
	x = []	

	for x_ in x_t:
		x.append(int(x_.split("-")[0]))


	y_local = []
	y_visitante = []
	
	goles_local = df_f['golesLocal'] 
	
	goles_visitante = df_f['golesVisitante']


	for gl in goles_local:
		y_local.append(gl)

	for gl in goles_visitante:
		y_visitante.append(gl)




	states = ['EquipoLocal', 'EquipoVisitante']

	'''equipo1 = [6, 10, 17, 20]
	equipo2 = [2, 4, 5, 10]

	data= {'years' : years, 'Equipo1' : equipo1, 'Equipo2' : equipo2}  
	source_ = ColumnDataSource(data= data)
'''
	title_ = "Rango por Equipo"
	x_axis = "Años"
	y_axis = "Equipos"
	width = 500
	height = 350


	plot = figure(title= title_, x_axis_label= x_axis, y_axis_label= y_axis, plot_width= width, plot_height= height)


	plot.circle(x, y_local)
	plot.line(x, y_local, legend= 'Barcelona', line_width =1, color='#00FF88')

	plot.circle(x, y_visitante)
	plot.line(x, y_visitante, legend= 'Atletico de Madrid', line_width =1, color='#660088')



	colors = {'Equipo1' : "#718dbf", 'Equipo2' : "#e84d60"}
	location = 0
#	for state in states:
#	plot.vbar(x=dodge('years', location, range=plot.x_range), top=state, width=0.2, source= source_, color=colors[state], legend=value(state))
	
#	plot.legend.location = "top_left"
#	plot.legend.orientation = "horizontal"
#	plot.xgrid.grid_line_color = None

	script, div = components(plot)
	graphic = {"script_rango" : script, "div_rango" : div}

	return graphic


def plot_proyeccion():
	

	df =pd.read_csv('/home/dsabrile/Escritorio/Data Set/v2/datosequipo.csv',header=0)
	
	df_f = df [ (df['EquipoLocal'] == 'Barcelona')& (df['EquipoVisitante'] == 'Atletico de Madrid')]
	temporadas = df [ df['EquipoLocal'] == 'Barcelona'].drop_duplicates('temporada')	
	

	x_t = temporadas['temporada']
	x = []	

	for x_ in x_t:
		x.append(int(x_.split("-")[0]))


	y_local = []
	y_visitante = []
	
	goles_local = df_f['golesLocal'] 
	
	goles_visitante = df_f['golesVisitante']


	for gl in goles_local:
		y_local.append(gl)

	for gl in goles_visitante:
		y_visitante.append(gl)

	cont_loc = 0
	cont_vis = 0


	for i in range(len(y_local)):
		if y_local[i] > y_visitante[i]:
			cont_loc += 1
		else:
			cont_vis += 1

	
	x = {
   	 'Barcelona': cont_loc,
    	 'Atletico de Madrid': cont_vis,	
	}

	data = pd.Series(x).reset_index(name='value').rename(columns={'index':'country'})
	data['angle'] = data['value']/data['value'].sum() * 2*pi
		

	data['color'] = ['#6baed6', '#9ecae1']

	plot = figure(plot_height=350, title="Partidos Ganados", toolbar_location=None,
           tools="hover", tooltips="@country: @value", x_range=(-0.5, 1.0))

	plot.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend='country', source=data)

	plot.axis.axis_label=None	
	plot.axis.visible=False
	plot.grid.grid_line_color = None

	script, div = components(plot)
	graphic = {"script_proyeccion" : script, "div_proyeccion" : div}

	return graphic






























