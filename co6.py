# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 12:31:08 2023

@author: Aralimarad
"""
"""
Write Python Program to Simulate a Bank Account with private 
data attributes name and balance and protected methods depositMoney, 
withdrawMoney and showBalance 
"""
class BankAccount:
    def __init__(self,n,b):
     self.__name=n
     self.__balance=b
    def _showBalance(self):
        print('user{} has a balance{}'.format(self.__name,self.__balance))
    def _withdrawMoney(self,amount):
        if self.__balance>amount:
         self.__balance-=amount
         print('Balance after withdraw')
         self._showBalance()
        else:
         print('No suffiecent balance in an account')
    def _depositMoney(self,k):
     self.__balance+=k
     print('Balance after deposit')
     self._showBalance()
     
name=input('Enter a user name:')
ba=float(input('Enter a amount'))
b1=BankAccount(name,ba)
b1._showBalance()
k=float(input('Enter amount to be withdrawn'))
b1._withdrawMoney(k)
k1=float(input('enter amount to be deposited'))
b1._depositMoney(k1)


