# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 14:12:54 2023

@author: Aralimarad
"""

# Python id() function example  
l1 = [1,2,3,4]  
l2 = [1,2,3,4]  
l3 = [3,5,6,7]  
# Calling function  
id1 = id(l1)  
id2 = id(l2)  
id3 = id(l3)  
# Displaying result 
print(id1)
print(id2) 
print((l1==l2),(l1==l3))  
# Objects with the same values can have different ids  
print((id1==id2),(id1==id3))  
# l1 and l2 returns True, while id1 and id2 returns False