import numbers
from random import random


from random import randint

def main():
    #open a file for write
    outfile = open("Numbers.txt","w")
    for i in range(10):
        outfile.write(str(randint(0, 9)) + " ")
    outfile.close()

    #test exceptions o file name
    while True:
        try:
            filename = input("Enter the file name: ").strip()

            infile = open(filename,"r")
            s = infile.read()
            numbers = [eval(x) for x in s.split()]
            for number in numbers:
                print(number, end=" ")
            infile.close()
            print()
            break
        except IOError:
            print(filename+" does not exist. Try again!")
    '''
    #open a file for reading 
    infile = open("Numbers.txt", "r")
    s = infile.read()  #read all content as a single string
    numbers = [eval(x) for x in s.split()]
    for number in numbers:
        print(number, end=" ")
    infile.close()
    print()
    '''

main() #calling the main function