# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 12:25:31 2023

@author: Aralimarad
"""

"""
program to demonstarte polymorphism
"""
class Vehicle:
    def __init__(self,m):
     self.model=m
    def vehicle_model(self):
     print('Vehicle model name is {}'.format(self.model))
class Bike(Vehicle):
    def vehicle_model(self):
     print('Vehicle model name is {}'.format(self.model))
class Car(Vehicle):
    def vehicle_model(self):
     print('Vehicle model name is {}'.format(self.model))
class Aeroplane:
    pass
def vehicle_info(v):
  v.vehicle_model() 
b=Bike('Scooty') 
c=Car('swift')   
a=Aeroplane()    
for i in [b,c,a]:
    try:
     vehicle_info(i) 
    except AttributeError:
     print('Excepteced method not present in that object')

