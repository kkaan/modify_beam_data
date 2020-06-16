# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 21:22:40 2020

@author: 56153805
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
from w2cadimport import w2cadimport
import visualise as vs
from pionpdd import pionpdd


root = tk.Tk()
root.withdraw()



file_path = '10X FFF_Open_PDD_sorted.ASC'

dataheader, datarray = w2cadimport(file_path)

m_10FFF = 0.000231318
b_10FFF = 0.976730208

ionpdd = datarray
m = 0

for meas in ionpdd:

    ionpdd = pionpdd(meas[:,3], m_10FFF, b_10FFF)
     
    x = datarray[m][:,2]
    y = datarray[m][:,3]
    flsz = "what"
    for item in dataheader[m].split("\n"):
        if "FlSZ" in item:
            flsz =  item.strip()
    
    
    vs.visualise(x, y, ionpdd, flsz)
    m = m+1
