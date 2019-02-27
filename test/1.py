# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print("ข้อ Birth day")
import datetime
today = datetime.datetime.now()
print("เกิดวันเดือนไหนค่ะ ")
h = int(input("ชั่วโมง :"))
d = int(input("วัน :"))
M = int(input("เดือน :"))
y = int(input("ป(ค.ศ.) :"))
nowdayD = today.day
nowdayH = today.hour
x = datetime.datetime(y,M,d,h)
c = today-x
h = (c.total_seconds())/(60*60)
print("คุณเกิดมาแล้ว %.2f ชั่วโมง" % h)


