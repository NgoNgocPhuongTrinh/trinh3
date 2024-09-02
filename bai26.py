# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 11:13:57 2024

@author: trinh
"""

#(a) Hãy in ra màn hình theo thứ tự tăng dần các số 
a = float(input("Nhập giá trị của a: "))
b = float(input("Nhập giá trị của b: "))
c = float(input("Nhập giá trị của c: "))
bien = 0 
if a > b:
    bien = a 
    a = b
    b = bien
if a > c:
    bien = a
    a = c
    c = bien
if b > c:
    bien = b
    b = c
    c = bien
print("Thứ tự tăng dần là: ", a, b, c)

#(b)  in ra số có các con số theo thứ tự tăng dần
N = int(input("Nhập số nguyên N: "))
thu_tu_tang_dan = int("".join((sorted(str(N)))))
print("Thứ tự tăng dần là: ", thu_tu_tang_dan)