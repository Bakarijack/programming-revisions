import  random

#assign random numbers to the following variables
number1 = random.randint(0,9)
number2 = random.randint(0,9)

#check if number1 is less than number2 the switch the numbers
if number1 < number2 :
    number1,number2 = number2,number1 
    
#promt the user with the question
answer = eval(input("What is "+str(number1)+" - "+str(number2)+" ? "))

if (number1 - number2) == answer:
    print("Correct answer ! ")
else:
    print("Wrong answer!")
    print(number1," - ",number2," is ",(number1-number2))