# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 14:29:26 2022

@author: Aralimarad
__name__ example 
"""

print ("File1 __name__ = %s" %__name__) 
  
if __name__ == "__main__": 
    print ("File1 is being run directly")
else: 
    print ("File1 is being imported")