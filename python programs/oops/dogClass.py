class Dog:
    attr1 = "mammal"
    attr2 = "dog"
    
    def fun(self):
        print("I am a",self.attr1)
        print("I am a",self.attr2)
    
    

#using the created class
ranger = Dog()

print(ranger.attr1)
ranger.fun()