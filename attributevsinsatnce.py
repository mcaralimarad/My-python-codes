# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 14:17:27 2023

@author: Aralimarad
"""
"""
class Student:
    count = 0
    def __init__(self):
        Student.count += 1        
 """       
'''       
std1=Student()
Student.count

std2=Student()
Student.count

'''


class Student:
    def __init__(self, name, age): 
        self.name = name
        self.age = age
        
       
'''        
std = Student('Bill',25)
std.name
'''