# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 11:08:35 2022

@author: Aralimarad
"""
"""
Python program to create a tuple with  n names
and print all names in a tuple in alphabetical order. 
Find second minimum and maximum alphabetical ordered name

"""
n=int(input("Enter a length:"))
names=[]
for i in range(n):
 names.append(input("Enter a name:"))
names=tuple(names)
print("A tuple with {} names{}".format(n,names))
names=('suma','ram','ravi')

names_s=sorted(names)
names_s=('ram','ravi','suma')

print("Names in a tuple in alphabetical order:")
for k in names_s:
    print(k)
print("Second minimum alphabetical order name is:",names_s[1])
print("Second maximum alphabetical order name is:",names_s[-2])

