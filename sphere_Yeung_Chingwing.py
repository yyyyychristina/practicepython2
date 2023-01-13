'''
Given the radius compute the diameter, circumference, and volume
of a sphere.

Useful facts:
   diameter = 2 * radius
   circumference = diameter * 3.14
   surface area = 4 * PI * radius * radius
   volume = 4/3 * PI * radius * radius * radius

Hint: import math to use math.pi
'''
import math

#enter radius
radius = float(input('Enter radius:'))

#computing
diameter = 2 * radius
circumference = diameter * math.pi 
surface_area = 4 * math.pi * radius * radius
volume = 4/3.0 * math.pi * radius * radius * radius

#print out output
print(f"Diameter:{diameter:.2f}")

print(f"Circumference:{circumference:.2f}")

print(f"surface area:{surface_area:.2f}")

print(f"Volume:{volume:.2f}")






