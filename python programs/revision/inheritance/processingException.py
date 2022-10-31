try:
    number = eval(input("Enter a number: "))
    print("The number entered is : ",number)
except NameError as e:
    print("Exception: ",e)