# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 10:43:15 2024

@author: trinh
"""

chu = input("Nhập 1 chữ cái: ")
if chu.isupper():
    print("Kết quả: ", chu.lower())
else:
    print("Kết quả: ", chu.upper())