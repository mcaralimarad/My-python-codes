# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 09:19:41 2022

@author: Aralimarad
"""

"""
Python program to create list of odd number from n to m using range function
and print the elements of a list in forward and backward direction.
Find the length of the list.

"""
n=int(input(" Enter a starting limit:"))
m=int(input("Enter a ending limit:"))
if n<m:
   l=list(range(n,m+1,2)) 
print("Length of list is",len(l)) 
print("List is:",l) 
print("Elements of list in forward direction:")
for i in l:
    print(i) 
print("Elements of list in backward direction:")
for i in range(-1,-(len(l)+1),-1):
    print(l[i])
