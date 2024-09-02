# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 21:16:16 2024

@author: trinh
"""

import math
r = float(input("Nhập bán kính hình tròn r = "))
Chuvi = 2*math.pi*r
dientich = 2*math.pi*r**2
if r>0:
    print(f"Chu vi hình tròn là {Chuvi}")
    print(f"Diện tích hình tròn là {dientich}")
else:
    print("Bán kính không hợp lệ:")

