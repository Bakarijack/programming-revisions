integerNumbers = []

for i in range(10):
    num = eval(input("Enter the "+str(i + 1)+" integer : "))
    integerNumbers.append(num)
    
print(integerNumbers)

print("The total number of items is the list are ",len(integerNumbers))
print("The last item in the list is ",integerNumbers[-1])
integerNumbers.reverse()
print("The reversed list is ",integerNumbers)
if 5 in integerNumbers:
    print("Yes")
else:
    print("No")
    
count = 0
for i in integerNumbers:
    if i == 5:
        count = count + 1  


print("5 occurences in the list is ",count," times")

#integerNumbers.remove(integerNumbers[0])   #using the lement itself
#integerNumbers.remove(integerNumbers[-1])
integerNumbers.pop(0)          #using the index of the lement
integerNumbers.pop(-1)

print(integerNumbers)

integerNumbers.sort()

print(integerNumbers)

lessThan5Items = 0
for i in integerNumbers:
    if i < 5:
        lessThan5Items = lessThan5Items + 1 

print("The number of items less than 5 are ",lessThan5Items)    