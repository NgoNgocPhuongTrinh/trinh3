# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 00:04:21 2024

@author: trinh
"""

h1 = int(input("Nhập vào thời gian thứ nhất\n\tGiờ: "))
p1 = int(input("\tPhút: "))
s1 = int(input("\tGiây: "))

h2 = int(input("Nhập vào thời gian thứ hai\n\tGiờ: "))
p2 = int(input("\tPhút: "))
s2 = int(input("\tGiây: "))

if ( 0 <= h1 < 24 and 0 <= p1 < 60 and 0 <= s1 < 60
    and 0 <= h2 < 24 and 0 <= p2 < 24 and 0 <= s2 < 24):
    print("Tổng hai giờ này là: ",h1+h2,"giờ",p1+p2,"phút",s1+s2,"giây")
    print("Hiệu hai giờ này là: ",abs(h1-h2),"giờ",abs(p1-p2),"phút",abs(s1-s2),"giây")
else:
    print("Vui lòng nhập lại thời gian hợp lệ !")