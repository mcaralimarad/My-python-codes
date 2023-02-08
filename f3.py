# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 12:14:52 2022

@author: Aralimarad
"""

def fact(x):
    f=1
    for i in range(1,x):
        f=f*i
    return f
n=int(input("Enter a last limit:"))
for i in range(1,n):
 print(" factorial of {} is {}".format(i,fact(i)))
