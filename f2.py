# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 12:13:28 2022

@author: Aralimarad
"""

def even_odd(n):
    if n%2==0:
      print("{} is even number".format(n))
    else:
      print("{} is odd number".format(n))
x=int(input("Enter a number:"))
even_odd(x)
