from Circle import Circle

def main():
    #create a circle of radius 1
    circle1 = Circle()
    print("The area of the circle of radius",circle1.radius,"is",format(circle1.getArea(),".2f"))
    
    #create a circe of radius 25
    circle2 = Circle(25)
    print("The area of the circle of radius ",circle2.radius,"is",format(circle2.getArea(),".2f"))
    
    #create a circle of radius 125
    circle3 = Circle(125)
    print("The area of the circle of radius ",circle3.radius,"is",format(circle3.getArea(),".2f"))
    
main() #call the main method