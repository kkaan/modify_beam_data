# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 9:35:25 2020

@author: kaan
"""

import os
import re
import pandas as pd
import numpy as np



def w2cadimport(filename):
    
    filename = 'P:/13 Equipment/Software/pybeam/10X FFF_Open_PDD_sorted.ASC'
    
    with open(filename, 'r') as myfile:
        data = myfile.read()
    
    nums = data.partition('\n')[0]  #pulls out the first line
    nums = int(re.search(r'\d+', nums).group()) 
    
    listofdata = []
    
    count = 0
    
    for result in re.findall('STOM(.*?)\$ENOM', data, re.S): #non greedy
        listofdata.append(result)
        count = count +1  #count should equal to nums if all goes well
    
    
    datarray = []
          
    for s in listofdata:
        s = s[s.find('<'):s.rfind('>')].replace("<", "").replace(">", "")
        c = np.fromstring(s, dtype=float, sep=' ')
        c = np.reshape(c, (-1, 4))
        datarray.append(c)
    
    dataheader = []
    
    for h in listofdata:
        p = h[0:h.find('<')]
        dataheader.append(p)
        

    return dataheader, datarray
    


 
