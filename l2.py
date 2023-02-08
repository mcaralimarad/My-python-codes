# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 09:22:16 2022

@author: Aralimarad
"""

"""
Created on Tue Oct 13 20:21:52 2020

@author: Hp
"""
L=[5,2,'HELLO',3]
print(L[::])
print(L[1:3])
print(L[:2])
L[1:3]=[7,8,9]
print(L,len(L)) 
L[1:5]=[6]
print(L,len(L)) #L=[5,6]
L[:1]=[]
print(L,len(L)) #L=[2,'HELLO',3]
