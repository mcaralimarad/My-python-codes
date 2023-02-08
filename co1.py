# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 11:34:09 2023

@author: Aralimarad
"""

"""
Python program to illustrate classes and object creation

"""
class Mobile:
    def __init__(self):
     print("This message is from constructor method")
    def send_message(self):
     print('send message using mobile')
    def receive_message(self):
     print('Receive message from mobile')
def main():
    m=Mobile()
    m.send_message()
    m.receive_message()
if __name__=='__main__':
  main()
