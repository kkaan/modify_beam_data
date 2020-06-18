# -*- coding: utf-8 -*-
"""
Import and export functions that deal with W2CAD fomats for processing 
and displaying on third party scripts.

Created on Mon Jun 15 9:35:25 2020
@author: kaan
"""

import os
import re
import pandas as pd
import numpy as np



def w2cadimport(filename):
    # Import w2cad file and change it to an arracy of measurements
    # and a corresponding list of headers.
    # Insert details on what kind of object are created here
    
    # filename = 'P:/13 Equipment/Software/pybeam/10X FFF_Open_PDD_sorted.ASC'
    
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
    


def w2cadexport(filename, dataheader, datarray):
    # Export a formated header array and list of measurement data
    # to a TPS readable format.
    # Insert requirements for dataheader and ionedarray here

    filename = filename[0:-4]+'_ioned.ASC' # the [0:-4] strips existing ext
    
    nums = len(datarray)   
    
    
    with open(filename, 'w') as f:   # create a new txtfile and write to it
        f.write(f"$NUMS {nums:03}\n")   # write how many measurements
        for h in dataheader:            # h is a header for each measurement           
            f.write(f'$STOM')           # start of measurement delimiter
            f.write(h)
            for row in datarray[dataheader.index(h)]:                                                
                line = f"<{row[0]:+06.01f} {row[1]:+06.01f} {row[2]:+06.01f} {row[4]:+06.01f}>\n"
                f.write(line)
            f.write(f'$ENOM\n')         # end of measurement delimiter
        f.write(f"$ENOF")
 
