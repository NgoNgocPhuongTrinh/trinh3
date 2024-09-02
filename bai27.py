# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 12:43:24 2024

@author: trinh
"""

import math 
nhap_hinh = input("Nhập 1 hình (hình vuông (v), hình chữ nhật (n) và hình tròn (t)): ")
if nhap_hinh == "n":
    print("Tính P và S của hình chữ nhật")
    r = float(input("Nhập chiều rộng: "))
    d =float(input("Nhập chiều dai: "))
    print("P = ", (r+d)*2 ,     "S= ", r*d )
elif nhap_hinh == "v":
    print("Tính P và S của hình vuông")
    d =float(input("Nhập độ dài: "))
    print("P = ", 4*d,      "s= ", d**2)
elif nhap_hinh == "t":
    print("Tính P và S của hình tròn")
    r = float(input("Nhập bán kính: "))
    print("P = ", 2*math.pi*r,      "S = ", 2*math.pi*r**2)
else:
    print("Vui lòng nhập lại")