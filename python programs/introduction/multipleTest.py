import random
import time

correctCount = 0 #count the number of correct answers
count = 0  #count the number of questions
NUMBER_OF_QUESTIONS = 5 #contant

startTime = time.time() #get start time

while count < NUMBER_OF_QUESTIONS:
    #generate two random single-integer digits
    number1 = random.randint(0,9)
    number2 = random.randint(0,9)
    
    #if number1 < number2, swap the numbers
    if number1 < number2 :
        number1,number2 = number2,number1
    
    #prompt the user to answer the question
    answer = eval(input("What is "+str(number1)+" - "+str(number2)+" ? "))
    
    #grade the answeer and display the results
    if number1 - number2 == answer:
        print("You are correct!")
        correctCount += 1
    else:
        print("Your ansewer is wrong\n",number1," - ",number2," is ",number1-number2)
    
    #increase the count
    count += 1

endTime = time.time()
testTime = int(endTime - startTime)
print("Correct count is ",correctCount," out of ",NUMBER_OF_QUESTIONS,"\nTest time is ",testTime," seconds")