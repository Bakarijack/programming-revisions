class Example:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b


#Testing the class
e = Example(5,4)
print(e.add())