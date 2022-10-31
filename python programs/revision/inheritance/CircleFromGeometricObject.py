from GeomentricObject import GeometricObjectClass
from InvalidRadiusException import InvalidRadiusExceptionClass
import math

class Circle(GeometricObjectClass):
    def __init__(self, radius = 1):
        super().__init__()
        self.setRadius(radius)
        
    def getRadius(self):
        return self._radius
    
    def setRadius(self, radius):
        if radius < 0:
            raise InvalidRadiusExceptionClass(radius)
        else:
            self._radius = radius
    
    def getArea(self):
        return self._radius * self._radius * math.pi
    
    def getDiameter(self):
        return 2 * self._radius
    
    def getPerimeter(self):
        return 2 * self._radius * math.pi
    
    def printCircle(self):
        print(self.__str__() + " radius : " + str(self._radius))

    #override a function
    def __str__(self):
        return super().__str__() + " radius is " + str(self.getRadius())