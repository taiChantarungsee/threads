import math

from django.shortcuts import render, render_to_response
from .models import location, district

from bokeh.plotting import figure, output_file, show 
from bokeh.embed import components
from bokeh.models import LabelSet, ColumnDataSource, ranges
from bokeh.palettes import PuBu

def index(request):
	# 'values_list' returns a list, so order is preserved.
	names = list(location.objects.values_list('laua_name', flat=True))
	speeds = list(location.objects.values_list('average_download_speed', flat=True))

	source = ColumnDataSource(dict(x=names,y=speeds))

	x_label = ""
	y_label = "Average Download Speed"
	plot = figure(
		plot_width=1300, 
		plot_height=600,
        x_axis_label = x_label,
        y_axis_label = y_label,
        title="Average Download Speed By Address",
        x_minor_ticks=2,
        x_range = source.data["x"],	
        )

	labels = LabelSet(x='x', y='y', text='y', level='glyph',
        x_offset=-13.5, y_offset=0, source=source, render_mode='canvas')

	plot.vbar(source=source,x='x',top='y',bottom=0,width=0.3,color=PuBu[7][2])

	plot.add_layout(labels)
	#Store components 
	script, div = components(plot)

	locs = location.objects.all()
	context = {'locs':locs, 'script' : script , 'div' : div}
	return render_to_response('index.html', context)

def district_view(request):
	names = list(district.objects.values_list('la_name', flat=True))
	speeds = list(district.objects.values_list('average_download_speed', flat=True))

	source = ColumnDataSource(dict(x=names,y=speeds))

	x_label = ""
	y_label = "Average Download Speed"
	plot = figure(
		plot_width=1300, 
		plot_height=600,
        x_axis_label = x_label,
        y_axis_label = y_label,
        title="Average Download Speed By district",
        x_minor_ticks=2,
        x_range = source.data["x"],	
        )

	labels = LabelSet(x='x', y='y', text='y', level='glyph',
        x_offset=-13.5, y_offset=0, source=source, render_mode='canvas')

	plot.vbar(source=source,x='x',top='y',bottom=0,width=0.3,color=PuBu[7][2])

	plot.add_layout(labels)
	#Store components 
	script, div = components(plot)

	locs = location.objects.all()
	context = {'locs':locs, 'script' : script , 'div' : div}

	return render_to_response('district.html', context)