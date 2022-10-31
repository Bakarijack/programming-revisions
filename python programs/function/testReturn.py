#testing function
def test(num):
    if num < 0:
        return None #return can also be used
    else:
        return num

def  main():
    num = eval(input("Enter a number: "))
    value = test(num) 
    
    if value == None:
        print("number can not be a negative")
    else:
        print("your number is ",value)
           
main()  #calling the main function