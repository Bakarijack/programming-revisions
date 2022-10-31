def sort(number1,number2):
    if number1 < number2:
        return number1,number2
    else:
        return number2,number1

n1,n2 = sort(3,2)
print("n1 is ",n1)
print("n2 is ",n2)

print(format(0.53457,"<10.2%")) #multi by 100 and display answer with % sign