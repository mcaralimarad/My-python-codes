# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 12:23:49 2023

@author: Aralimarad
"""

"""
Program to Demonstrate Base and Derived Class Relationship 
Without Using __init__() Method in a Derived Class

"""
import p
class Teacher(p.Person):
    def teacher_display(self):
     print('{} is working as teacher and lives at {}'
           .format(self.name,self.address))

x,y=input('Enter name and address:').split(' ')
t=Teacher(x,y)
t.display()
t.teacher_display()

