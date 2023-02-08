# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 11:23:22 2022

@author: Aralimarad
"""

"""
Python program to read a tuple with n student details.
Where every element of a tuple is a tuple which contains name,usn,sem,marks for each student.
Sort the nested tuple on name of student
sort the nested tuple on marks

"""
n=int(input("Enter number of students:"))
stud=[]
for i in range(n):
    det=[]
    print("Enter a details of {} student".format(i+1))
    det.append(input("Enter a name:"))
    det.append(input("Enter a uns number:"))
    det.append(input("Enter a semester:"))
    det.append(float(input("Enter a marks:")))
    det=tuple(det)
stud.append(det)
stud=tuple(stud)
print("Nested tuple with student details is:",stud)
stud_s=sorted(stud)
print("Sorted nested tuple is:",tuple(stud_s))
stud_s1=sorted(stud,key=lambda x:x[3])
print("Sorted nested tuple is:",tuple(stud_s1))

