# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 14:18:06 2022

@author: Aralimarad

local and global variable example
"""

def greet():

    # local variable
    message = 'Hello'
    
    print('Local', message)

greet()

# try to access message variable 
# outside greet() function
"print(message)"

# declare global variable
message = 'Hello'

def greet():
    # declare local variable
    print('Local', message)

greet()
print('Global', message)