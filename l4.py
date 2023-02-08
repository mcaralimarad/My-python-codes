# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 09:25:58 2022

@author: Aralimarad
"""

"""
Python program to read a list of student names in 3 sem
and  a list of student names in 5 sem. find common names in both list
"""
n=int(input("Number of students in 3 sem:"))
s3=[]
print("Enter a student names of 3 sem:")
for i in range(n):
    s3.append((input("Enter a name:")))

m=int(input("Number of students in 5 sem:"))
s5=[]
print("Enter a student names of 5 sem:")
for i in range(m):
    s5.append((input("Enter a name:")))
print("students in 3 sem are:",s3)
print("students in 5 sem are:",s5)
comnames=[]
for i in s3:
    if i in s5:
     comnames.append(i)
print("Common names in both list are:",comnames)     
