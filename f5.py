# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 12:19:32 2022

@author: Aralimarad
"""

"""Python program to perform all arithmetic operations on two integer
 numbers using a function calculate()

"""
def calculate(a,b):
    return a+b,a-b,a*b,a//b
x,y=input("Enter two numbers:").split()
t=calculate(int(x),int(y))
print(t)
