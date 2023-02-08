# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 14:08:04 2022

@author: Aralimarad
"""

"""
Python program to illustrate default arguments

"""
def f(a,b,c=2,d=3):
    print(a,b,c,d)
f(10,20,30,40)
f(10,20,30)
f(10,20)
f(b=20,a=10)
f(10)
