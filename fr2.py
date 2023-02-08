# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 15:54:43 2023

@author: Aralimarad
"""

"""
Python program to read a line of text from keyboard and 
write it to a file inputted by the user.

"""
x=input("Enter a file name:")
try:
    k=open(x,"a")
    s=input("Enter a line of text")
    k.write(s)
except Exception:
    print("Error")
finally:
 k.close()
