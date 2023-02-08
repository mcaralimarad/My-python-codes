# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 14:07:48 2023

@author: Aralimarad
"""

"""
Python  Program to Demonstrate Passing of an Object as an Argument
 to a Function Call

"""
class Track:
    def __init__(self,s,a):
     self.song=s
     self.artist=a
    def print_trackinfo(self):
     print('song is:',self.song)
     print('Artist is:',self.artist)
     
     
t=Track('Deepavuninade','k.s.narasimhaswamy')
t.print_trackinfo()

