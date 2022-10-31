#create the class
class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def info(self):
        print(f"I am a cat, my name is {self.name}. I am {self.age} years old")
        
    def sound(self):
        print("Meow")
    
    @staticmethod
    def move():
        print("faster")
        
    

cat1 = Cat("Andy",2)
cat2 = Cat("Phoeb",3)