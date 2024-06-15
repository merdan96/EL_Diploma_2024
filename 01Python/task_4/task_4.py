#! /usr/bin/python
import math

radius = float(input("Please Enter the radius : "))

area = round(radius ** 2 * math.pi, 2)
print("The circle's area = " + str(area))