# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 16:05:07 2023

@author: Aralimarad
"""

"""
Python program to read the numbers stored in a file test.txt.
Check the number is even or odd. If even
 write it to a file even.txt otherwise write it to a file odd.txt
"""
f=open("num.txt")
f1=open("even.txt","w")
f2=open("odd.txt","w")
while True:
        k=f.readline()
        print(k)
        if k:
            if int(k)%2==0:
                f1.write(k+'\n')
            else:
                f2.write(k+'\n')
        else:
            break
f.close()
f1.close()
f2.close()

