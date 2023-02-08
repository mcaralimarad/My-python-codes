# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 14:53:14 2022

@author: Aralimarad
"""

"""
Python program to handle multiple exception

"""
def sum_avg(l):
    s=0
    for x in l:
        s+=x
    a=s/len(l)   
    return s,a
try:
 x,y=sum_avg([1,2])
 print("total is {} and average is{}".format(x,y))
except TypeError:
 print("Type Error occured and provide a numbers")
except ZeroDivisionError:
 print("Zero division occured please do not provide a empty list")

