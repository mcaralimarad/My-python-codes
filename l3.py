# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 09:24:23 2022

@author: Aralimarad
"""

"""
python program to find a list with unique elements
"""
n=int(input("Enter a length of list:"))
l=[]
for i in range(n):
    x=int(input("Enter a element:"))
    l.append(x)
print("Entered list is:",l) 
uq=[]
for i in l:
    if i not in uq:
     uq.append(i) 
print("List with unique list:",uq)

