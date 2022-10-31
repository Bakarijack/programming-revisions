def max(num1, num2):
    return num1 if num1 > num2 else num2  #returning the result of the condition expression

def display():
    print("Functions are cool!")

def printMessage(num):
    if num < 0 or num > 5:
        print(num,"is Invalide input!")
        return #returns control to the caller return None can also be used
    
    for i in range(num):
        print("Hello World ",i+1)

def main():
    print("The larger number between 2 and 5 is ", max(2, 5))
    print("The larger number between 25 and 15 is ", max(25, 15))
    print("The larger number between 22 and 51 is ", max(22, 51))  #value-returning functions are treated as values
    display() #calls the function that only print words    NB non value-returning function is treated as statement
    print(display())  #this will print the default None since does not return any value
    printMessage(4)
    printMessage(-1)
    printMessage(6)

main() #calling the main function