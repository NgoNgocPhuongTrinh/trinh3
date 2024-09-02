# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 09:22:59 2024

@author: trinh
"""

time = input("nhập thời gian (theo dạng: 1h8p8s): ")
m, p, s = 0, 0, 0
if "h" in time:
    h = int(time.split("h")[0])
    time = time.split("h")[1]
if "p" in time:
    p = int(time.split("p")[0])
    time = time.split("p")[1]
if "s" in time:
    s = int(time.split("s")[0])
print("Kết quả ", h*60*60 + p*60 + s, "giây")