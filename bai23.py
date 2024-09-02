# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 12:39:33 2024

@author: trinh
"""

#Phương trình bậc hai: ax2 + bx + c = 0
import math 
a = float(input("Nhập giá trị của a: "))
b = float(input("Nhập giá trị của b: "))
c = float(input("Nhập giá trị của c: "))
delta = b**2 -4*a*c
if a == 0:
    print("Đây không phải phương trình bậc 2")
else:
    if delta == 0:
        print ("Phương trình có nghiệm kép x = ",-b/2*a)
    elif delta > 0:
        print("Phương trình có 2 nghiệm phân biệt:")
        print("x1 = ", (-b + math.sqrt(delta))/2*a)
        print("x2 = ", (-b - math.sqrt(delta))/2*a)
    else:
        print("Phương trình vô nghiệm")