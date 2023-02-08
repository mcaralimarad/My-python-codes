# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 10:58:21 2022

@author: Aralimarad
"""

"""
Python program two read a matrix of order m and n 
and find a transpose of matrix and print it in matrix form.
"""
m,n=input("Enter a number of rows and column of a matrix:").split(',')
mat=[]
m=int(m)
n=int(n)
print("Enter a elements of matrix:")
for i in range(m):
    col=[]
    
print("Enter a",i+1,"row elements:")
    
for j in range(n):
 col.append(input())
 mat.append(col)     
 print("Elements of matrix before Transpose:")
for i in range(m): 
    for j in range(n):
        print(mat[i][j],end=' ') 
        print()                      

print("Transpose of a matrix:")
for i in range(n): 
    for j in range(m): 
        print(mat[j][i],end=' ')  
        print()                       
