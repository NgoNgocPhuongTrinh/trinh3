# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 10:27:46 2024

@author: trinh
"""

gio_phut_giay = input("Nhập thời gian theo định dạng (giờ, phút, giây): ")
gio, phut, giay = map(int, gio_phut_giay.split(",") )
if gio > 0 and gio < 24 and phut > 0 and phut < 60 and giay > 0 and giay < 60:
    print(f"Kết quả: {gio} giờ {phut} phút {giay} giây")
else:
    print("Thời gian không hợp lệ, vui lòng nhập lại")