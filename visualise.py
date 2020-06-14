# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 9:10:13 2020

Using bokeh to visualise the data

@author: Kaan
"""
from bokeh.plotting import figure, output_file, show

def visualise(x, y):

    # prepare some data
    
    # output to static HTML file
    output_file("lines.html")
    
    # create a new plot with a title and axis labels
    p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')
    
    # add a line renderer with legend and line thickness
    p.line(x, y, legend_label="pdd.", line_width=2)
    
    
    # show the results
    show(p)
