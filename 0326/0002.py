#!/usr/bin/python
# 교수님 제곱근은 어떻게 계산해요?

from math import sqrt

x1 = float(input("x1 :"))
y1 = float(input("y1 :"))
x2 = float(input("x2 :"))
y2 = float(input("y2 :"))

print( ( (x1-x2)**2 + (y1-y2)**2 ) ** 0.5 )