# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 15:58:32 2022

@author: Aralimarad
"""

s=input("Enter a string:")
if len(s)>=6:
    print("Length of entered string is",len(s))
    print(s[-1:-3:-1]+s[len(s)//2:len(s)//2+2])
else:
    print("length of the string is less than six")
