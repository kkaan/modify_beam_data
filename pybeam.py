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
# pddedit:  select pdds to apply filters to
# pionfilter: will apply the pion correction to the pdds
# displaybeam: will use bokeh to display results.
# w2cadexport: write back to w2cad format
# 
# =============================================================================


import tkinter as tk
from tkinter import filedialog
from w2cadimport import w2cadimport
import visualise as vs


root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

datarray = w2cadimport(file_path)

x = datarray[0][:,2]
y = datarray[0][:,3]
    
vs.visualise(x, y)