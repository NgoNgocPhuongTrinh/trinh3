# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 11:28:04 2024

@author: trinh
"""

a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))
c = int(input("Nhập số nguyên thứ ba: "))
d = int(input("Nhập số nguyên thứ tư: "))
if a > b and a > c and a > d:
    print("Số có giá trị nhỏ nhất là: ", a)
elif b > a and b > c and b > d:
    print("Số có giá trị nhỏ nhất là: ", b)
elif c > a and c > b and c > d:
    print("Số có giá trị nhỏ nhất là: ", c)
else:
    print("Số có giá trị nhỏ nhất là: ", d)