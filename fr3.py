# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 15:56:51 2023

@author: Aralimarad
"""

"""
Python program to read each line from a file biodata 
and count number of lines using readline() function

"""
count=0
try:
    h=open("mydata.txt","r")
    while True:
        k=h.readline()
        if k:
            print(k)
            count=count+1
        else:
            break
except Exception:
    print("Error")           
else:
 print("Total number of lines:",count)

