import  random

#1.Generate random single-digit integers
number1 = random.randint(0,9)
number2 = random.randint(0,9)

#2. if number1 < number2, swap number1 with number2
if number1 < number2 :
    number1,number2 = number2,number1
    
#3.prompt student to answer
answer = eval(input("What is "+str(number1)+" - "+str(number2)+" ? "))

#4. check the answer and display result
if number1 - number2 == answer:
    print("You are correct")
    
else:
    print("You are wrong.\n",number1," - ",number2," is ",number1-number2," .")