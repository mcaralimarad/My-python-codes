# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 15:51:31 2023

@author: Aralimarad
"""


try:
    f=open("mydata.txt","r")
    s=f.read()
    print("The content of a file:",s)
except Exception:
    print("Error")
