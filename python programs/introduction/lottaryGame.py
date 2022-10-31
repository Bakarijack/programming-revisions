import  random

#generate random lottery number between 10 and 99
lottery = random.randint(10,99)

#prompt user to enter a guess number
guess = eval(input("Enter your lottery pick number : "))

#get the digits of the lottery number
lotteryDigit1 = lottery // 10
lotteryDigit2 = lottery % 10 

#get guess digits
guessDigit1 = guess // 10
guessDigit2 = guess % 10

print("The lottery number is ",lottery)

#check the guess
if guess == lottery:
    print("Exact match: you win $10,000")
elif (guessDigit1 == lotteryDigit2 and \
    guessDigit2 == lotteryDigit1):
    print("Match all digits: you win $3,000")
elif (guessDigit1 == lotteryDigit1
      or guessDigit1 == lotteryDigit2
      or guessDigit2 == lotteryDigit1
      or guessDigit2 == lotteryDigit2):
    print("Match one digit : you win $1,000")
else:
    print("Sorry, no match")         