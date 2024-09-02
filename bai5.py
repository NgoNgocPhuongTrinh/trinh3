# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 11:46:54 2024

@author: trinh
"""
thoigian = input("Nhập giờ, phút, giây theo định dạng hh:mm:ss ")
try:
    gio, phut, giay = map(int, thoigian.split(":") )
except:
        print("Định dạng giờ phút giây không hợp lệ. Vui lòng nhập lại ")
else:
    if gio > 24 or gio < 0:
        print("Thời gian không hợp lệ")
    elif phut > 60 or phut < 0:
        print("Thời gian không hợp lệ")
    elif giay > 60 or giay < 0:
        print("Thời gian không hợp ")
    else:
        print("Kết quả", gio*60*60 + phut*60 + giay,)