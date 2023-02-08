# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 15:55:09 2022

@author: Aralimarad
"""

s=input("Enter a string:")
assert len(s)>8,"string is not accepted"
s1=s[3:7]
print("sliced string:",s1)
print(s1*3)
