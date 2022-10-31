from random import choice, sample


l = [1,2,4,5,7,8,0,8,76]
del l[0]
print(l)
for i in range(len(l)):
    l[i] = l[i] ** 2

print(l)
print(sample(l,2))
print(choice(l))
print(10000/24)