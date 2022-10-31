import math
for i in range(3):
    print("Hello", i + 1)

'''for i in range(3):
    while True:
        try:
            num = eval(input("Enter a number : "))
            print("The square of ",num," is : ",math.pow(num, 2))
            break
        except ValueError:
            print("Integer is required! Try again")
        except:
            print("Something went wrong! Try again")

print("The loop is now done")
'''
#shape
for i in range(10):
    print("*" * (i+1),"*" * (5 - i),"*" * (i + 1))
