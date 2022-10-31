from unittest import result


def sumDigits(i1, i2):
    result = 0

    for i in range(i1, i2 + 1):
        result += i

    return result


def main():
    print("The sum of 1 to 10 is ", sumDigits(1, 10))
    print("The sum of 10 to 20 is ", sumDigits(10, 20))
    print("The sum of 20 to 30 is ", sumDigits(20, 30))

main()  #calling the main function