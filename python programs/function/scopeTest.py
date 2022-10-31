globalVar = 1 
def f1():
    localVar = 2
    print(globalVar)
    print(localVar)

f1()
#print(localVar) #outside the scope