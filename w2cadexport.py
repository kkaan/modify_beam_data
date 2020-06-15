# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 14:31:30 2020

Exports to w2cad format

@author: kaan
"""

def w2cadexport(filename, dataheader, datarray):
    
    filename = filename[0:-4]+'_ioned.ASC' # the [0:-4] strips existing ext
    
    nums = len(datarray)   
    
    
    with open(filename, 'w') as f:   # create a new txtfile and write to it
        f.write(f"$NUMS {nums:03}\n")   # write how many measurements
        for h in dataheader:            # h is a header for each measurement           
            f.write(f'$STOM')           # start of measurement delimiter
            f.write(h)
            for row in datarray[dataheader.index(h)]:                                                
                line = f"<{row[0]:+06} {row[1]:+06} {row[2]:+06} {row[3]:+06}>\n"
                f.write(line)
            f.write(f'$ENOM\n')         # end of measurement delimiter