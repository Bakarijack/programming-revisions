
class GeometricObjectClass:
    def __init__(self, color = "green", filled = True):
        self.__color = color
        self.__filled = filled
    
    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def isFilled(self):
        return self.filled

    def setFilled(self, filled):
        self.filled = filled

    def __str__(self):
        return "Color : "+str(self.__color)+" and filled : "+str(self.__filled)