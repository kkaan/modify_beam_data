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


file_path = 'P:/13 Equipment/Software/pybeam/10X FFF_Open_PDD_sorted.ASC'

dataheader, datarray = w2cadimport(file_path)

m_10FFF = 0.000231318
b_10FFF = 0.976730208

iondarray = datarray

for meas in datarray:
    pdd = meas[:,3]
    ionpdd = pionpdd(pdd, m_10FFF, b_10FFF)
    ionmeas = 
    iondarray.append(ion)


x = datarray[0][:,2]
y = datarray[0][:,3]
ionpdd = iondarray[]
    
vs.visualise(x, y, ionpdds)

w2cad