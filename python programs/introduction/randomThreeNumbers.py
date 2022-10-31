import random

#generate three single-digit random numbers
number1 = random.randint(0,9)
number2 = random.randint(0,9) 
number3 = random.randint(0,9)

sum =   number1 + number2 + number3

answer = -1
while sum !=answer:
    #prompt the user to enter the answer for the  sum of the three numbers
    answer = eval(input("What is "+str(number1)+" + "+str(number2)+" + "+str(number3)+" ? "))
    
    if sum == answer:
        print("You are correct!")
    else:
        print("Wrong answer.Tray again.",end="")

    