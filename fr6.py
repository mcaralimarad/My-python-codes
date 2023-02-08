# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 15:59:28 2023

@author: Aralimarad
"""

"""
Python program to accept string from user until user press @ symbol.
Write the inputted string to a file input by the user

"""
s=input("Enter a file name:")
print("Enter a string and exit by pressing @ symbol")
try:
    f=open(s,"w")
    m=''
    while m!='@':
        m=input("Enter a string:")
        if m!='@':
         f.write(m+'\n')
except Exception:
    print("Error")
finally:
 f.close()
