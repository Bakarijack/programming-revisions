#recieve an integer
num = eval(input("Enter an integer : "))

if (num > 1 and num < 100) or num < 1:
    print(num, " is between 1 and 100, or negative number")

if num > 100:
    print(num," is beyond the set limit")

'''if num < 1:
    print(num," is a negative number")'''