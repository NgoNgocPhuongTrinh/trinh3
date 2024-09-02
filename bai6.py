# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 21:06:00 2024

@author: trinh
"""

nam = int(input("Nhập năm sinh của bạn "))
if nam > 0 or nam < 2022:
    print(f"Bạn sinh năm {nam} vậy tuổi của bạn là:", 2022-nam)
else:
    print("Năm sinh không hợp lệ")