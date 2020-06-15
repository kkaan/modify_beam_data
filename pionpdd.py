# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 11:37:45 2020

Correct PDDS using Corns et al 2015 method. 

%dd = (100 * S * Pion)/(S_dmax * Pion_dmax)

@author: 56153805
"""

def pionpdd(y, m, b):

    ya = m*y**2+b*y
    return ya


    