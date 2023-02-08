# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 12:22:44 2022

@author: Aralimarad
"""

"""
Python program to create a dictionary 
for number of occurrences of each letter using a function find()

"""
def find(s):
    d={}
    for i in s:
        d[i]=d.get(i,0)+1
    return d
e=find(input("Enter a string:"))      
print(e)
