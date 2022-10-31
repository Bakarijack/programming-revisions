#Prompt user for input
seconds = eval(input("Enter an integer for seconds: "))

#converts it to integer by trancating
#seconds = int(seconds)

#Test augmented assignment Operators
seconds += seconds

#rounds the seconds to the nearest whole number
seconds = round(seconds)

#Get minutes and remaining seconds
minutes = seconds // 60
remainingSeconds = seconds % 60

#Display the results
print(seconds," seconds is ",minutes," minutes and ",remainingSeconds," seconds")