# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 15:56:30 2022

@author: Aralimarad
"""

rows = int(input("Enter the number of rows: "))  
  
# the outer loop is executing in reversed order  
for i in range(rows + 1, 0, -1):    
    for j in range(0, i - 1):  
        print("*", end=' ')  
    print(" ")