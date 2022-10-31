from defineClass import Circle

def main():
    c1 = Circle()
    print(format(c1.getArea(), ".2f"))
    c1.setRadius(7)
    print(format(c1.getArea(), ".2f"))
    print(c1.radius)
    print(Circle(14).getArea())   #anonymous object

main() #calling the main function