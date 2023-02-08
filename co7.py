# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 12:36:49 2023

@author: Aralimarad
"""

"""
Define a class student with private data attributes name and marks.
Read n student details and print student details along with grade obtained.

"""
class Student:
    def __init__(self,n,m):
     self.__name=n
     self.__marks=m
    def display(self):
     print('Name of the students is:',self.__name)
     print('Marks obtained by the student is:',self.__marks)
     if self.__marks>=90:
         print('Grade obtained by student is A')
     elif self.__marks>=70:
      print('Grade obtained by student is B')
     elif self.__marks>=40:
      print('Grade obtained by student is C')
     else:
      print('U r failed')
      

      
n=int(input('Enter number of students'))
i=0;
while i<n:
       x,y=input('Enter name and marks').split()
       s=Student(x,float(y))
       print(i+1,'student Details')
       s.display()
       i+=1
       
       
       

