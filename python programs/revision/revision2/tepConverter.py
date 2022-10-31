import numbers


import math
temp = eval(input("Enter the temperature in celsius  : "))
print(temp," in Fahrenheit, is that is ",((9 / 5) * temp) + 32)

print("Hello","World",sep=" # ")
print(math.pow(temp,2))
while True:
    try:
        number1,number2 = eval(input("Enter two numbers separated by comma : "))
        print("The division of the numbers is : ", number1 / number2)
        break
    except SyntaxError:
        print("Separate the numbers with a comma! Try again")
    except ZeroDivisionError:
        print("The second number cannot be zero. Try again!")
    except:
        print("Something is wrong with the numbers")


