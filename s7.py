# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 16:21:03 2022

@author: Aralimarad
"""

s=input("Enter a main string:")
sb=input("Enter a sub string:")
p=s.find(sb)
if p!=-1:
 print("substring is found at {}".format(p))
else:
  print("substring is not found")
try:
    p1=s.rindex(sb)
    print("sub string found at{}".format(p1))
except ValueError:
    print("{} is not found".format(sb))
