age = 14

if not(age > 18):
    print("young")

number = eval(input("Enter a number : "))

if number % 2 == 0 and number % 3 == 0:
    print(number, " is divisible by both 2 and 3")

if number % 2 == 0 or number % 3 == 0:
    print(number, " is divisible by 2 or 3")

if (number % 2 == 0 or number % 3 == 0) and not (number % 2 == 0 and number % 3 == 0):
     print(number," is divisible by 2 or 3, but not both")

#conditional expression
number1 = 10
number2 = 20    

maximumNumber = number1 if number1 > number2 else number2
print(maximumNumber)