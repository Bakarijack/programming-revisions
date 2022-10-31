from numpy import math


import math

radius = eval(input("Enter the radius of the circle : "))
#PI = 3.14159
if radius < 0:
    print("Incorrect input")
else:
    area = radius * radius * math.pi
    print("Area is ",format(area, ".2f")," cm2")

lightOn = True
print(lightOn," is equal to ", end="")
print(int(lightOn))

lightOff = False
print(lightOff," is equal to ", end="")
print(int(lightOff))

print(bool(0))
print(bool(23))
print(bool(-54))