# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 14:23:14 2022

@author: Aralimarad
"""

# Function for nth Fibonacci number
 
def Fibonacci(n):
    if n<= 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
 
# Driver Program
 
print(Fibonacci(6`))