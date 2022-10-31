#creating a class
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def myfun(self):
        print("Hello my name is ",self.name)
    
p1 = Person("Bakari",35)
p1.myfun()