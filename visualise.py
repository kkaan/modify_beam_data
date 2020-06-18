# -*- coding: utf-8 -*-
"""
Using bokeh to visualise the data

Created on Mon Jun 15 9:10:13 2020
@author: Kaan
"""
from bokeh.plotting import figure, output_file, show
from bokeh.palettes import OrRd9, Oranges9   #  BuGn9, GnBu9 for 10FFF

def visualise(ioned, headers):

    # prepare some data
    
    # output to static HTML file
    output_file("6FFF_recombination.html")
    
    
    TOOLTIPS = [
    ("(depth(mm),pdd)", "($x, $y)"),
    ]
    
    
    # create a new plot with a title and axis labels
    p = figure(plot_width=1200, plot_height=800, title="6FFF ion recombination corrected", x_axis_label='depth(mm)', 
               y_axis_label='pdd', tooltips=TOOLTIPS)
    
    # add a line renderer with legend and line thickness
    for data, name, color1, color2 in zip(ioned, headers, OrRd9, Oranges9):
        p.line(data[:,2], data[:,3], legend_label=name, color=color1, line_width=2)
        p.line(data[:,2], data[:,4], legend_label=name, color=color2, line_width=2)
    
 
    # show the results
    p.legend.location = "top_right"
    p.legend.click_policy="hide"
    
    
    show(p)
