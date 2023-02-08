# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 16:13:04 2022

@author: Aralimarad
"""

s='  hello how are you  '  
#s=s.rstrip()
print(s)
count=0
print("String after removing a space:",s)
for i in s:
    if i==' ':
        count+=1
        print(count,i)
print("Total number of spaces in: {} are: {}".format(s,count))
