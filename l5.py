# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 09:27:40 2022

@author: Aralimarad
"""

"""
Python program to read a n Employee details 
which includes name, empid salary and designation.
Retrieve a particular employee details. And count
no of employee with each designation

"""
n=int(input("Enter a number of employees:"))
print("Enter Employee Details:")
emp=[]
for i in range(n):
 emp.append(int(input("Enttera Employee id:")))
emp.append(input("Enter a employee Name:"))
emp.append(float(input("Enter a Salary:")))
emp.append(input("Enter a Desgination:"))
x=int(input("Enter a employee id:"))
for i in range(len(emp)):
    if x==emp[i]:
     print("Employee id is:",emp[i])
     print("Employee Name is:",emp[i+1])
     print("Employee Salary is:",emp[i+2])
     print("Employee Designation is:",emp[i+3])
    break
else:
 print("Employee Record is not present")
des=[]
for i in range(3,len(emp),4):
    if emp[i] not in des:
     des.append(emp[i])

k=3
print(des)
for i in des:
   print("No of employee with designation {} is {}".format(i,emp.count((emp[k]))))
k=k+4

