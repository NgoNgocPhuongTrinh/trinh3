# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 09:13:44 2024

@author: trinh
"""

#a
ngay_thang_nam = input("Nhập ngày sinh theo định dang:ngày tháng năm: ")
ngay_sinh = "/".join(ngay_thang_nam.split(" "))
print("Ngày tháng năm sinh của bạn là: ", ngay_sinh) 
#b
ngay, thang, nam = map(int, input("Nhập ngày sinh theo định dang: ngày tháng năm: ").split())
ngay_sinh = f"{ngay}/{thang}/{str(nam)[-2:]}"
print(f"Ngày tháng năm sinh của bạn là: ", ngay_sinh )
#c
ngay, thang, nam = map(int, input("Nhập ngày sinh theo định dạng: ngày tháng năm: ").split())
ngay_sinh = f"{nam}/{thang}/{ngay}"
print(f"Ngày tháng năm sinh của bạn là: ", ngay_sinh)

#Ngược lại 
#a
ngay_thang_nam = input("Nhập ngày sinh của bạn theo định dạng: ngày/tháng/năm ")
print(f"Ngày tháng năm sinh của bạn là: ", ngay_thang_nam.replace("/"," " ))
#b
ngay, thang, nam = input("Nhập ngày sinh của bạn theo định dạng: ngày/tháng/năm ").split("/")
if len(nam) == 2:
    nam = "19" + nam
ngay_sinh = f"{ngay} {thang} {nam}"
print(f"Ngày tháng năm sinh của bạn là: ",ngay_sinh)
#c
nam, thang, ngay = input("Nhập ngày sinh của bạn theo định dạng: năm/tháng/ngày ").split("/")
ngay_sinh = f"{ngay} {thang} {nam}"
print(f"Ngày tháng năm sinh của bạn là: ",ngay_sinh)