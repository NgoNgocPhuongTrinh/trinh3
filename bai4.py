# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 11:33:47 2024

@author: trinh
"""

a = int(input("Nhập số nguyên dương N có 2 chữ số: "))  
b = a//10 
c = a%10
if a > 0:
    print("N = ", b+c, )
else:
    print("Lại")