# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 14:49:47 2022

@author: Aralimarad
"""

"""
Python program to handle ZeroDivisionError exception

"""
x,y=input("Enter a two numbers").split(' ')
try:
    c=int(x)/int(y)
    print("Division of {} and {} is {}".format(x,y,c))
except ZeroDivisionError:
   print("Division by zero has happened")
