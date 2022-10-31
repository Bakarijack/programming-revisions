import  random

#generate two single-digit numbers
number1 = random.randint(0,9)
number2 = random.randint(0,9)

#if number1 < number2, swap number1 with number2
if number1 < number2:
    number1,number2 = number2,number1
    
#prompt student to answer
answer = eval(input("What is "+str(number1)+" - "+str(number2)+" ? "))

#repeate ask the question until answer is correct
while number1 - number2 != answer:
    answer = eval(input("Wrong answer. Try again. What is "+str(number1)+" - "+str(number2)+" ? "))

print("You got it!")