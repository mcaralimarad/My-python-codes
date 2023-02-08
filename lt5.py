# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 11:29:00 2022

@author: Aralimarad
"""

"""
Python program to perform following operations on a tuple.
Inserting a new element at given position
Modifying a element at given position 
Deleting a element from given position

"""
n=int(input("Enter a limit:"))
l=[]
for i in range(n):
 l.append(int(input("Enter a number:")))
print("Created tuple is:",tuple(l))
print("1:insert 2: modify, 3:delete")
x=int(input("Enter a choice:"))
if x==1:
    y=int(input("Enter a new element:"))
    pos=int(input("Enter a position:"))
    c=l
    if pos<len(l):
        l=l[:pos]
        l.append(y)
        l=l+c[pos:]
    else:
     l.append(y)
    print("Tuple after inserting a new element:",tuple(l))
elif x==2:
    y=int(input("Enter a new element:"))
    pos=int(input("Enter a position:"))
    c=l
    if pos<len(l):
        l=l[:pos]
        l.insert(pos,y)
        l=l+c[pos+1:]
    else:
     print("It is not in a range")
    print("Tuple after modifcation :",tuple(l))
elif x==3:
   pos=int(input("Enter a position:"))
   if pos<len(l):
        l=l[:pos]+l[pos+1:]
   else:
     print("It is not in a range")
   print("Tuple after deletion:",tuple(l))
else:
 print("Invalid chocie:")
