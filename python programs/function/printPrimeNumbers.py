#chack whether number is prime or not
def isPrime(number):
    divisor = 2  
    while divisor <= number/2:
        if number % divisor == 0:
            return False #the number is not prime
        divisor += 1
    return True

def  printPrimeNumbers(numberOfPrimes):
    NUMBER_OF_PRIME = 50   
    NUMBER_OF_PRIME_PER_LINE = 10  
    counter = 0
    number =2   
    while counter < numberOfPrimes:
        if isPrime(number):
            counter += 1
            print(number,end=' ')
            if counter % NUMBER_OF_PRIME_PER_LINE == 0:
                print() #print on a new line
        number +=1
        
def main():
    print("The first 50 prime numbers are ")
    printPrimeNumbers(50)


main()