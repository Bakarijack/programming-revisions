from GCDFunction import gcd #import the gcd function

#prompt the user to enter two numbers
n1 = eval(input("Enter the first integer: "))
n2 = eval(input("Enter the second integer: "))

print("The greatest common divisor for ",n1," and ",n2," is ",gcd(n1,n2))