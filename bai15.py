# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 12:24:07 2024

@author: trinh
"""
 
a = float(input("Nhập số thứ nhất "))
b = float(input("Nhập số thứ hai "))
A = ( (a + b) / (pow(a,(1/3)) + pow(b,1/3)) - (pow(a*b, (1/3))) ) / (pow(a, (1/3)) - pow(b, (1/3)))**2 
print("kết quả: ", A)