# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 14:10:22 2022

@author: Aralimarad
"""

"""
Write a python program to find sum and average of a n numbers stored in a list

"""
def sum_avg(m):
    s=0;
    for k in range(len(m)):
        s=s+m[k]
    return s,s/len(m)

n=int(input("Enter a limit:"))
print("Enter a {} numbers".format(n))
l=[]
for i in range(n):
 l.append(int(input("Enter a number:")))
p,y=sum_avg(l)
print("Sum is:",p)
print("Average is:",y)

