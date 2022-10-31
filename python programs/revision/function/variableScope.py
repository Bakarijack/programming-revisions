globalvar = 1

def f():
    localvar = 5 
    print(globalvar)
    print(localvar)

f()
print(globalvar)

x = 1         
def increase():
    global x
    x += 1
    print("inside the function ",x)

increase()
print("Outiside the function ",x)