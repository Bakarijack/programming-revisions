def main():
    n = eval(input("Enter a number: "))
    print("Factorial of ",n," is ", factorial(n))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)   #recursive call

main() #calling the main function