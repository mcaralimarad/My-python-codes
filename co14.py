# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 11:26:39 2023

@author: Aralimarad
"""


"""
Program to Illustrate Class Variables and Instance Variables

"""
class Dog:
    kind='canine'
    x=0
    def __init__(self,x):
     self.dog_name=x
     self.x=self.x+1  
     
d=Dog('Fido') # d dog_name='Fido'  x=1
e=Dog('Bubby') #e  dog_name='Bubby' x=1 
print('Value for Shared Variable or Class Variable "kind" and x is {} {}'.format(d.kind,d.x))   
print('Value for Shared Variable or Class Variable "kind" and x is {} {} '.format(e.kind,e.x)) 
print('Value for Unique Variable or Instance Variable "dog_name" is {} '.format(d. dog_name))
print("Value for Unique Variable or Instance Variable 'dog_name' is {}".format(e.dog_name))
