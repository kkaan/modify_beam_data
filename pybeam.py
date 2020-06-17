# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 21:22:40 2020

@author: kaan
"""

# =============================================================================
# 
# 
# w2cadimport: take in the w2cad and convert to array
# 
# pionpdd: will apply the pion correction to the pdds
# displaybeam: will use bokeh to display results.
# w2cadexport: write back to w2cad format
# 
# =============================================================================


import tkinter as tk
from tkinter import filedialog
from w2cad import w2cadimport
from w2cad import w2cadexport
import visualise as vs
from pionpdd import pionpdd
import re

import numpy as np



# root = tk.Tk()
# root.withdraw()
# file_path = filedialog.askopenfilename()

file_path = '10X FFF_Open_PDD_sorted.ASC'


# dataheader: each item on list is the header of each measurment
# datalist: each item is an array containing [x u x pdd] for each measurement
dataheader, datalist = w2cadimport(file_path)


ionedlist = [] 


# This loop will add a fourth empty column for poinised data
for m in datalist:
    b = np.zeros((m.shape[0],m.shape[1]+1))  # create zero matrix b the same 
                                             # size as m but with additional 
                                             # column of zeroes
                                             
    b[:,:-1] = m  # make the first three columns of b to be the same as m
    ionedlist.append(b)


# Pion fit constants:
m_10FFF = 0.000231318 # gradient of the poin slope
b_10FFF = 0.976730208 # intercept of the pion slope

m_6FFF  = 0.00012807  # gradient of the poin slope
b_6FFF  = 0.987159689 # intercept of the pion slope




pltitle = []

m = 0
for meas in ionedlist:
# this loop will ionise and add ionised pdd to the fourth column.
    meas[:,4] = pionpdd(meas[:,3], m_10FFF, b_10FFF)
    
    flsz = "what"
    
    for item in dataheader[m].split('\n'):
    # this loop will generate plot names based on field size
        if "FLSZ" in item:
            flsz = item
            flsz = re.sub('\%*', '', flsz)
            flsz = re.sub('\*', 'x', flsz)
            pltitle.append(flsz)
         
    m = m+1

# Export the array to w2cad format
w2cadexport(file_path, dataheader, ionedlist)

# Generate plots
# vs.visualise(ionedlist, pltitle)