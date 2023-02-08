# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 15:16:42 2022

@author: Aralimarad
"""

"""
Python program to illustrate user defined exception

"""
class MyException(Exception):
    def __init__(self,a):
        self.msg=a
bank={'Raj':3000.0,'Ravi':800.00,'Ramesh':6000.00}
try:
    for i,j in bank.items():
        print("Name:{} Balance:{}".format(i,j))        
        if j<2000.00:
             raise MyException('Balance is less than 2000.00 in account of'+ i)
except MyException as m:
    print(m)
