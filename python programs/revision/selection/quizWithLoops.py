import numbers
import random

number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

answer = input("What is "+str(number1)+" + "+str(number2)+" ? ")

while answer.isspace() == True and len(answer) == 0:
    answer = input("A value is required! \nWhat is "+str(number1)+" + "+str(number2)+" ? ")
    
while answer.isdigit() == False:
    answer = input("Integer number is required! \nWhat is "+str(number1)+" + "+str(number2)+" ? ")

while number1 + number2 != eval(answer):
    answer = input("Wrong answer! Try again. What is "+str(number1)+" + "+str(number2)+" ? ")

    while answer.isdigit() == False:
        answer = input("Integer number is required! \nWhat is "+str(number1)+" + "+str(number2)+" ? ")

print("Good work! You got it")