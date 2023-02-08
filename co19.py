# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 12:09:43 2023

@author: Aralimarad
"""

"""
Define derived class Enggstudent from a base class Student with private attributes 
branch semester and division. Base class has private members name and USN.
Override display method in base and derived class to display the details of a student

"""
class Student:
    def __init__(self,n,b):
     self.__sname=n
     self.__usn=b
    def display(self):
     print('Name of student is:',self.__sname)
     print('USN of a student is:',self.__usn)
class EnggStudent(Student):
    def __init__(self,n,a,br,s,d):
        super().__init__(n,a)
        self.__branch=br
        self.__sem=s
        self.__division=d
    def display(self):
        super().display()
        print('Branch name is:',self.__branch)
        print('Semester is:',self.__sem)
        print('Division is:',self.__division)
        
l=list(input('enter name usn branch semester and division'))
print(l)
e=EnggStudent(l[0],l[1],l[2],int(l[3]),l[4])
print(e)
print('Details of a student:')
e.display()
