# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 14:07:08 2022

@author: Aralimarad
"""

"""
Python program to illustrate keyword argument

"""
def SimpleInterset(p,t,r):
 print("simple interset is:",(p*t*r)/100)
SimpleInterset(1000,3,9.5)
SimpleInterset(1000,r=9.5,t=3)
SimpleInterset(t=3,r=9.5,p=1000)
