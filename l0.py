# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 11:35:39 2022

@author: Aralimarad
"""

L=[]
M=list([1,2,3])
print(L,M,type(L))
student=[]
student=[10, "2BA12CS011", "Ravi", 30.5, 78.8, 90.7]
print(student)
print(type(L))
Marks=[10,20,45,60]
print(Marks)
print(type(L))
Names=["Ravi", "Raj", "Ram", "Seema"]
print(Names)
print(type(Names))



L=[33,45,67,8,9,1]
print(len(L),max(L),min(L))
del L[3]
print(L)
M=sorted(L)
print(M,L)



L=[1,2,3,[4,5]]
x=list([3,1,["a","b"]])
M=[[1,2,3],
       [4,5,6],
       [7,8,9]]
print(L[2],L[3][1])
print(x[2][0],x[0])
print(M[2],M[1][1])
print(M[:2],L[2:],x[::])
