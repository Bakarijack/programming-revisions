import random
from turtle import st

number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

answer = eval(input("What is "+str(number1)+" + "+str(number2)+" ? "))

if answer == (number1 + number2):
    print("Your answer is correct!")
else:
    print(number1," + ",number2," = ",answer," is ", (number1 + number2) == answer)
    print("The correct answer is ",(number1 + number2))

digit = eval(input("Enter a number between 1 and 5 : "))

if digit >= 1 and digit <= 5:
    print("Correct!")
elif digit < 1:
    print("The digit is below the range ")
else:
    print("The digit is above the the range")