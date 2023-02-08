# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 12:07:30 2023

@author: Aralimarad
"""

"""
Python program to create a class Mobile with attributes name, price and model.
Use constructor to initialize the instance variable 
and display method to display the details of a mobile

"""
class Mobile:
    def __init__(self,n,p,m):
        self.name=n
        self.price=p
        self.model=m
    def display(self):
        print('Details of mobile are as follows:')
        print("Name:",self.name)
        print('pirce:',self.price)
        print('model:',self.model)
m=Mobile('nokia',8000.00,'A67')
m.display()
m1=Mobile('Samsung',10000,'M10')
m1.display()
