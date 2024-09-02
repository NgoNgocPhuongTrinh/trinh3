# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 22:34:13 2024

@author: trinh
"""

cân_nặng = float(input("Nhập cân nặng của bạn (kg): "))
chiều_cao = float(input("Nhập chiều cao của bạn (m): "))
BMI = cân_nặng / (cân_nặng**2)
if cân_nặng > 0 and chiều_cao > 0:
    print(f"Số đo kiểm tra kết quả của bạn là: ",{BMI})
else:
    print("Vui lòng nhập lại")