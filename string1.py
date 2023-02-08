# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 12:17:53 2022

@author: Aralimarad
"""

s=input("Enter a string:")
print("length of a string:",len(s))
print("Characters in a string in forward directions(first method)")
for i in s:
    print(i)
print("Characters in a string in forward directions(second method)")
for i in range(len(s)):
    print(s[i])
print("Characters in a string in reverse directions(first method)")
for i in range(-1,-(len(s)+1),-1):
    print(s[i])
    #print(i)