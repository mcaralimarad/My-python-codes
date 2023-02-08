# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 16:01:58 2023

@author: Aralimarad
"""

"""
Python program that generates the factorial of all integers from 1 to 10 
and stores them in a file called fact.txt

"""
import math
try:
    f=open("fact.txt","w")
    for i in range(1,11):
     f.write("The factorial of {} is {}\n".format(i,math.factorial(i)))
except Exception:
    print("Error")

finally:
  f.close()
 
