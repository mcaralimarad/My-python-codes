# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 12:18:16 2022

@author: Aralimarad
"""

"""
Python program to generate prime numbers from n to m 
with the help of a function prime()

"""
def prime(x):
    for i in range(2,(x//2)+1):
        if x%i==0:
            break
    else:
        return x
    
    
n=int(input("Enter a first limit:"))
m=int(input("Enter a last limit:"))
print("prime numbers from {} and {} is".format(n,m))
for k in range(n,m+1):
    l=prime(k)
    if l != None:
        print(l)

