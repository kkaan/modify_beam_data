# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 9:10:13 2020

Using bokeh to visualise the data

@author: Kaan
"""
from bokeh.plotting import figure, output_file, show

def visualise(x, y, ya, flsz):

    # prepare some data
    
    # output to static HTML file
    output_file(flsz+"_recombination.html")
    
    # create a new plot with a title and axis labels
    p = figure(title=flsz+"ion recombination corrected", x_axis_label='pdd', 
               y_axis_label='depth (mm)')
    
    # add a line renderer with legend and line thickness
    p.line(x, y, legend_label="pdd imported", line_width=2)
    p.line(x, ya, legend_label="pdd pioned", line_color = "red", line_width=2)
    
 
    # show the results
    show(p)
