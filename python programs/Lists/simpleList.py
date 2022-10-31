numbers = [1,2,3,4,5,6,7,8,9]
print(numbers[0])

#list can contaion many things
mixture = [1,2.4,'bakari',[1,2,3]]

#check the element
if 2 in mixture:
    print("The list contains 2")
    

if 0 not in mixture:
    print("The list contains no zeros")
    
#mixture[:3] returns the first 3 element in the list

#loop through the list
#for in range(len(mixture)):
 #   print(mixture[i])

#the other loop
for item in mixture:
    print(item)
    
