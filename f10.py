# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 14:09:03 2022

@author: Aralimarad
"""

"""
Python program to illustrate variable length argument

"""
def sum(*x):
    s=0
    print(x)
    for k in x:
        s=s+k
    print("sum is:",s)
sum(2,3)
sum(2,3,4)
sum(2,3,4,5,6)
sum(1,2,3,4,5,6,7,8,9,10)
