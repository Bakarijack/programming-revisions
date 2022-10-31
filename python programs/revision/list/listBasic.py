#creating list using list()
from turtle import clear
from numpy import identity


import random
list1 = list()
print(type(list1))
list2 = list([1,2,3])
print(list2)
print(list2[1])
list3 = list(range(3, 7))
print(list3)
list4 = list("abcd")
print(list4)
list5 = list("1234")
print(list5)

#another way of creafting list
numbers = []        
number2 = [1,2,3]
print(number2)

#mixing elements in a list
personalData = ["bakari",26,"male"]
print(personalData)
print(type(personalData[0]))
print(type(personalData[1]))
print(number2[1 : 2])
print(number2)

print(len(list1))
random.shuffle(list2)
print(list2)
random.shuffle(list2)
print(list2)

#adding list variable
print(list2[0] + list2[1])