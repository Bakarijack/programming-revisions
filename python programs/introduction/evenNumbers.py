'''for i in range(50,0,-1):
    if i % 2 == 0:
        print(i," ",end='');
        
print();'''

#using for loop
sum = 0
for i in range(1001):
    sum += i

print(sum)

#using while loop
sum = 0
i = 0
while i < 1001:
    sum += i
    i += 1
print(sum)
