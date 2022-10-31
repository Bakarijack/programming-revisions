#Prompt the user to enter a radius
radius = eval(input("Enter the radius : "))

#Compute the area
if radius<0:
 print("Invalid input")
else:
 area = radius * radius * 3.14159
 #Display the area
 print("The area of the circle of radius ",radius," is ",area)