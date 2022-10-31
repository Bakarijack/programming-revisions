def sort(num1, num2):
    if num1 > num2:
        return num1, num2
    else:
        return num2, num1     #returning them using the conditianal expression produce error

n1, n2 = sort(3, 7)
print(n1,", ",n2)