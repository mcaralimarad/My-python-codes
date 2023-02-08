# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 14:28:26 2022

@author: Aralimarad
"""
# Python program to 
# demonstrate accessing of
# variables of nested functions
def f1():
    s = 'Hello sheldon cooper'
      
    def f2():
        print(s)
          
    f2()
  
# Driver's code
f1()