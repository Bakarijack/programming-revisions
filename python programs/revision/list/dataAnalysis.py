import numbers

from numpy import average


NUMBER_OF_ELEMENTS = 5
numbers = [] #create an empty list

sum = 0

for i in range(NUMBER_OF_ELEMENTS):
    value = eval(input("Enter a number: "))
    numbers.append(value)
    sum += value

average = sum / NUMBER_OF_ELEMENTS

count = 0
for i in range(NUMBER_OF_ELEMENTS):
    if numbers[i] > average:
        count += 1


print("Sum of ", NUMBER_OF_ELEMENTS," is ", sum)
print("The average of ",NUMBER_OF_ELEMENTS," is ",average)
print(count," numbers are above the average" if count > 1 else " number is above the average")