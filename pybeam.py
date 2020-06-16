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

root = tk.Tk()
root.withdraw()

file_path = '10X FFF_Open_PDD_sorted.ASC'

dataheader, datarray = w2cadimport(file_path)

m_10FFF = 0.000231318
b_10FFF = 0.976730208

m_6FFF  = 0.00012807
b_6FFF  = 0.987159689


ionedarray = datarray  # ioneddata will be the update array
m = 0

for meas in ionedarray:

    ionpdd = pionpdd(meas[:,3], m_10FFF, b_10FFF)
     
    x = datarray[m][:,2]
    y = datarray[m][:,3]
    flsz = "what"
    
    for item in dataheader[m].split('\n'):
        if "FLSZ" in item:
            flsz = item
            flsz = re.sub('\%*', '', flsz)
            flsz = re.sub('\*', 'x', flsz)
    
    
    #vs.visualise(x, y, ionpdd, flsz)
    ionedarray[m][:,3] = ionpdd
    
    m = m+1

# Export the array to w2cad format
#w2cadexport(file_path, dataheader, ionedarray)
