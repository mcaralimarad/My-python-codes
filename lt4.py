# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 11:14:15 2022

@author: Aralimarad
"""

"""
Python program to create a tuple of n integer numbers
and convert it to a singleton tuples of values. 
Example t=(1,2,3) must be converted as t=((1,),(2,),(3,))

"""
n=int(input("Enter a length:"))
l=[]
for i in range(n):
 l.append(int(input("Enter a number:")))
print("Tuple is:",tuple(l))
x=[]
for k in l:
    m=tuple((k,))   #m=k, m=tuple(1,)  m=(1,)
    x.append(m)      #x=[(1,),(2,),(3,)]
print("Tuple converted into a singleton tuple", tuple(x))

