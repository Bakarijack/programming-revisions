import numbers
import random

number = random.randint(0, 9)

guess = -1
continuation = 'y'
while guess != number and continuation == "y":
    guess = eval(input("Enter yor guess number : "))

    if guess == number:
        print("Yes ! The number is ",number)
    elif guess > number:
        print("Your guess is too high")
        continuation = input("Enter \"y\" to continue with the guessing or any letter to stop : ").lower()
    else:
        print("Your guess is too low")
        continuation = input("Enter \"y\" to continue with the guessing or any letter to stop : ").lower()
    
