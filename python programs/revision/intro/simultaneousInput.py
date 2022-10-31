from numpy import average


number1, number2, number3 = eval(input("Enter three numbers separeted with comma : "))

average = (number1 + number2 + number3 ) / 3

print("The average of ",number1," ,",number2," and ",number3," is ",average)