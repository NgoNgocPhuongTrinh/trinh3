# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 11:43:45 2024

@author: trinh
"""

# Phương trình bậc nhất ax + b = 0
a = float(input("Nhập giá trị của a: "))
b = float(input("Nhập giá trị của b: "))
if a == 0:
    if b == 0:
        print(f"Phương trình có vô số nghiệm")
    else:
        print(f"Phương trình vô nghiệm")
else:
    x = -b/a 
    print(f"Vậy nghiệm của phương trình là: {x}")