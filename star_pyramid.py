# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 15:57:26 2022

@author: Aralimarad
"""

n = int(input("Enter the number of rows: "))  
m = (2 * n) - 2  
print(m)
for i in range(0, n):  
    for j in range(0, m):  
        print(end=" ")  
       # print("n,m",n,m)
        print("i,j",i,j)
    m = m - 1  # decrementing m after each loop  
    for j in range(0, i + 1):  
        # printing full Triangle pyramid using stars  
        print("* ", end=' ') 
        #print("n,m",n,m)
        print("i,j",i,j)
    print(" ")  