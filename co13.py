# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 11:25:50 2023

@author: Aralimarad
"""

"""
Write Python Program to Compute the End Time,
While Start Time and Duration are Given using a class Time

"""
class Time:
    def __init__(self,x,y,z):
     self.h=x
     self.m=y
     self.s=z
    def add_time(self,t):
        t3=Time(0,0,0)
        t3.s=self.s+t.s
        t3.m=t3.s//60
        t3.s=t3.s%60
        t3.m+=self.m+t.s
        t3.h=t3.m//60
        t3.m=t3.m%60
        t3.h+=self.h+t.h
        return t3
    def display_time(self):
     print('Time is:{}:{}:{}'.format(self.h,self.m,self.s))
     
     
start=input('Enter a start time in formrat hh:mm:ss')
print(start)
l=start.split(':')
print(l)
t1=Time(int(l[0]),int(l[1]),int(l[2]))
duration=input('Enter a duration time in formrathh:mm:ss')
l=duration.split(':')
t2=Time(int(l[0]),int(l[1]),int(l[2]))       
t4=t1.add_time(t2)
t4.display_time()

