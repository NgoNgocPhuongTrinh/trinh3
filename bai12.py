# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 23:48:33 2024

@author: trinh
"""

import random
#a 0 đến 100 
so_nguyên = random.randint(0,100)
so_thuc = random.uniform(0, 100)
print(f"Xuất ra một số nguyên: ", {so_nguyên})
print(f"Xuất ra một số thưc: ", {so_thuc})

#b  50 đến 99
so_nguyên = random.randint(50,99)
so_thuc = random.uniform(50, 99)
print(f"Xuất ra một số nguyên: ", {so_nguyên})
print(f"Xuất ra một số thưc: ", {so_thuc})

#c -39 đến 79
so_nguyên = random.randint(-39, 79)
so_thuc = random.uniform(-39, 79)
print(f"Xuất ra một số nguyên: ", {so_nguyên})
print(f"Xuất ra một số thưc: ", {so_thuc})

#d -79 đến -39
so_nguyên = random.randint(-79, 39)
so_thuc = random.uniform(-79, 39)
print(f"Xuất ra một số nguyên: ", {so_nguyên})
print(f"Xuất ra một số thưc: ", {so_thuc})