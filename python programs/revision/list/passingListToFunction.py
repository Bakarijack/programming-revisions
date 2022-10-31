def main():
    x = 1 
    y = [1,2,3]

    m(x, y)
    print("x is : ",x)
    print("y[0] is : ",y[0])
    s1 = {1,2,3,4,5}
    s2 = {1,2,7,6}
    print(s1.union(s2))
    print(s1 | s2)
    print(s1 & s2)
    print(s2 - s1)
    print(s2 ^ s1)

def m(number, numbers):
    number = 45
    numbers[0] = 1000 


main() #caling the main function