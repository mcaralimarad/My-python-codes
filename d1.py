# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 14:22:16 2022

@author: Aralimarad
"""

# Python3 code to demonstrate
# to get key and value
# using in operator
 
# initializing dictionary
test_dict = {"Geeks": 1, "for": 2, "geeks": 3}
 
# Printing dictionary
print("Original dictionary is : " + str(test_dict))
 
# using in operator to
# get key and value
print("Dict key-value are : ")
for i in test_dict:
    print(i, test_dict[i])
    
    
    
    
    
# Python3 code to demonstrate
# to get key and value
# using dict.items()
 
# initializing dictionary
test_dict = {"Geeks": 1, "for": 2, "geeks": 3}
 
# Printing dictionary
print("Original dictionary is : " + str(test_dict))
 
# using dict.items() to
# get key and value
print("Dict key-value are : ")
for key, value in test_dict.items():
    print(key, value)