# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 14:23:53 2023

@author: Aralimarad
"""

"""
Given a point(x, y), Write Python Program to Find Whether it Lies 
in the First, Second, Third or Fourth Quadrant of x - y Plane
"""
class Quantrangle:
    def __init__(self,x,y):
     self.x_cord=x
     self.y_cord=y
    def check_quantarnt(self):
        if self.x_cord>0 and self.y_cord>0:
         print('({},{}) lies in first quadrant'.format(self.x_cord,self.y_cord))
        elif self.x_cord<0 and self.y_cord>0:
         print('({},{}) lies in second quadrant'.format(self.x_cord,self.y_cord))
        elif self.x_cord<0 and self.y_cord<0:
         print('({},{}) lies in Third quadrant'.format(self.x_cord,self.y_cord))
        elif self.x_cord>0 and self.y_cord>0:
         print('({},{}) lies in fourth quadrant'.format(self.x_cord,self.y_cord))


x,y=input('Enter x and y coordinates:').split(' ')
q=Quantrangle(int(x),int(y))
q.check_quantarnt()

