import  math
#prompt user for input
radius = eval(input("Enter a radius for the circle : "))

if radius >=0 :
    area = radius * radius * math.pi
    print("The area for the circle of radius ",radius," is ",format(area,".2f"))
else:
    print("Negative input")