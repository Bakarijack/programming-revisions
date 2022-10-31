def main():
    while True:
        try:
            number1, number2 = eval(input("Enter two numbers separated by comma : "))
            answer = divideNumbers(int(number1), int(number2))
            print(number1," / ",number2," is ",answer)
            break
        except IOError:
            print("Please provide integer inputs. Try again.")
        except SyntaxError:
            print("Please separate the number with a comma. Try again.")
        except ZeroDivisionError:
            print("Second number should not be 0. Try again")
        except:
            print("Check the numbers properly. Try again.")

def divideNumbers(num1, num2):
    result = num1 / num2
    return result

main()  #calling the main function