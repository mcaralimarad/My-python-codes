# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 14:51:25 2022

@author: Aralimarad
"""

"""
Python program to handle syntax error given by eval() function

"""
try:
    date=eval(input("Enter date:"))
except SyntaxError:
 print("Invalid date is entered")
else:
 print("Entered date is:",date)
