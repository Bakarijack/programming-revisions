myList = [14, 4, 2, 4, 5, 6]

for u in myList:
    print(u, end=", ")
print()

myList.append(8)
print(myList)

print(myList.count(4))

list1 = [9, 10]
myList.extend(list1)
print(myList)

print(myList.index(5))

myList.insert(1, 11)
print(myList)
print(myList.pop(1))

myList.remove(14)
print(myList)

myList.reverse()
print(myList)

myList.sort()
print(myList)

items = "Bakari Mtua Kilu".split()
print(items)

#copying list
l1 = [1,2,3]
l2 = [4,5,6]

print(id(l1))
print(id(l2))

l1 = l2
print(id(l1))

l3 = [3,4,5]
l4 = [6,4,2]

print(id(l3))
print(id(l4))

l3 = [x for x in l4]  # you can also use l3 = [] + l4
print(id(l3))
print(id(l4))

#anonymous list is the one that has ot name eg passingListToFunction([1,2,3,4,5,6])