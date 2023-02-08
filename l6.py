# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 09:31:03 2022

@author: Aralimarad
"""

"""
Python program to read a list of at least three engineering courses
and for each course read at least three subjects belongs to that course. 
Find total no of subjects that starts with letter p 

"""
course=[]
n=int(input("Enter a no of engineering courses:"))
if n>=3:
    for i in range(n):
     course.append(input("Enter a course:"))
     while True:
            m=int(input("Enter a number of subjects:"))
            if m>=3:
                s=[]
                for k in range(m):
                 s.append(input("Enter a subject:"))
                 course.append(s)
                 break
            else:
             print("minimum subjects must be 3:")
else:
 print("Minimum course must be 3:")
 print(course)
count=0
for i in range(1,len(course),2):
    for j in course[i]:        
       if j.startswith('p') or j.startswith('P'):
           count=count+1
print("Total number of courses that starts with letter p are:",count)

