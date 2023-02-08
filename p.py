# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 12:26:15 2023

@author: Aralimarad
"""

"""
Program to Demonstrate the Use of super() Function
"""
class Person:
    def __init__(self,n,a):
     self._name=n
     self.__address=a
    def display(self):
     print('{} is living at {}'.format(self._name,self.__address))
class Teacher(Person):
    def __init__(self,n,a,id,sname):
        super().__init__(n,a)
        self.__t_id=id
        self.__school_name=sname
    def teacher_display(self):
     print('{} is teacher with id {} is working at a school {}'.
           format(self._name,self.__t_id,self.__school_name))

x,y=input('Enter name and address:').split(' ')
m,n=input('Enter teacher id and school name').split(' ')
t=Teacher(x,y,m,n)
t.display()
t.teacher_display()
