# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 19:35:25 2020

@author: kaan
"""

import os
import re
import pandas as pd
import numpy as np
from bokeh.plotting import figure, output_file, show


os.getcwd()

with open('P:/02 Linacs/03 G3 4385/True Beam Golden Beam Data/W2CAD/10FFF/10X ' 
              +'FFF_Open_PDD_sorted.ASC', 'r') as myfile:
    data = myfile.read()

nums = data.partition('\n')[0]  #pulls out the first line
nums = int(re.search(r'\d+', nums).group()) 

listofdata = []

count = 0

for result in re.findall('STOM(.*?)ENOM', data, re.S): #non greedy
    listofdata.append(result)
    count = count +1  #count should equal to nums if all goes well


datarray = []
      
for s in listofdata:
    s = s[s.find('<'):s.rfind('>')].replace("<", "").replace(">", "")
    c = np.fromstring(s, dtype=float, sep=' ')
    c = np.reshape(c, (-1, 4))
    datarray.append(c)


# prepare some data
x = datarray[0][:,2]
y = datarray[0][:,3]

# output to static HTML file
output_file("lines.html")

# create a new plot with a title and axis labels
p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')

# add a line renderer with legend and line thickness
p.line(x, y, legend_label="pdd.", line_width=2)


# show the results
show(p)