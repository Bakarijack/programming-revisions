from CircleFromGeometricObject import Circle
from InvalidRadiusException import InvalidRadiusExceptionClass

def main():
    try:
        c1 = Circle(7)
        print("radius : ",c1.getRadius())
        c1.printCircle()
        c1.setColor("red")
        print(c1.getColor())
        c1.printCircle()
        print(c1.__str__())
        c2 = Circle(-3)
        print(c2.getArea())
    except InvalidRadiusExceptionClass as e:
        print("Radius ", e.radius," is Invalide radius ")
    except:
        print("Something went wrong!")

main() #calling main function