# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 22:44:41 2024

@author: trinh
"""

print("============ MENU ============ ")
print("1. Hủ tiếu \n2. Cháo lòng \n3. Bánh canh \n4. Bún riêu \n5. Phở bò")
print("==============================")
menu = ["Hủ tiếu", "Cháo lòng", "Bánh canh", "Bún riêu", "Phở bò"]
lựa_chọn = input("Mời nhập lựa chọn: ")
if lựa_chọn in menu:
    print("==============================")
else:
    print("Mời nhập lại")