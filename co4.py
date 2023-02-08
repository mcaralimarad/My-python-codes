# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 12:09:31 2023

@author: Aralimarad
"""

"""
Python program to create a class Student with attributes name,
sem division and  USN. Use  to set() to initialize the attributes
 and get() method to display the details of a student

"""
class Student:
    def set(self):
     print("Enter the details of a student")
     self.name=input('Enter a student name')
     self.usn=input('enter a USN')
     self.sem=int(input('Enter semester'))
     self.division=input('enter a division:')
    def get(self):
         print('Details of a student')
         print('Name:',self.name)
         print('Name:',self.usn)
         print('Name:',self.sem)
         print('Name:',self.division)
s=Student()
s.set()
s.get()
