import random

#generate two random numbers
number1 = random.randint(0,9)
number2 = random.randint(0,9)

#prompt the user to enter an answer
answer = eval(input("What is "+str(number1)+" + "+str(number2)+" ? "))

#Display the answer
print(number1," + ",number2," = ",answer," is ",number1 + number2 == answer)