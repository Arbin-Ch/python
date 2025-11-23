# Built in Math related functions:

x = 3.3
y = 4
z = 5

result = round(x)       # provides round figure in whole number
# result = pow(z, y)    # z to the power y
# result = max(x,y,z)   # provide max value among three
# result = min(x,y,z)   # provides minimum value among three

print(result)

a = -4

result = abs(a)        # provides an absolute value
print(result)


import math
print(math.pi)
print(math.e)

x = 9
result = math.sqrt(x)
print(result)

x = 6.6
# result = math.floor(x)      # provides whole number, but lower the value
result = math.ceil(x)         # provides whole number, but increase the value
print(result)


# Exercise1: Radius of Circle

radius = float(input("Enter the radius of the circle: "))

circumference =2 * math.pi * radius
print(f"The radius of the circle is: {round(circumference, 2)}")


# Exercise2: Area of Circle

radius = float(input("Enter the radius of the circle: "))

area = math.pi * pow(radius, 2)
print(f"The area of the circle is: {round(area, 2)}")


# Exercise3: Hypotenuse of the triangle

import math
a = float(input("Enter Side A: "))
b = float(input("Enter Side B: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Side C is: {round(c, 2)}")