# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 12:29:44 2023

@author: Aralimarad
"""

"""
Write Python Program to Create a Class Called as Complex and 
Implement __add__() Method to Add Two Complex Numbers.
Display the Result by Overloading the + Operator

"""
class Complex:
    def __init__(self,r,i):
     self.real=r
     self.imag=i
    def __add__(self,other):
        c3=Complex(0,0)
        c3.real=self.real+other.real
        c3.imag=self.imag+other.imag
        return c3
    def __str__(self):
        return f'{self.real}+i{self.imag}'
c1=Complex(2,4)
c2=Complex(5,6)
c4=c1+c2
print(f'sum of complex number {c1} and {c2} is {c4}')

