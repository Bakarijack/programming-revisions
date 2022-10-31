#Enter the first point with two float values
x1,y1 = eval(input("Enter x1 and y1 for point 1 : "))

#Enter the second point with  two float values
x2,y2 = eval(input("Enter x2 and y2 for point 2 : "))

#compute distance
distance = ((x1 - x2)**2 + (y1 - y2)**2) **0.5

#Display results
print("The distance between the two points is : ",end = ' ')
print(format(distance,"10.2f"))       #format the output
