#using continue to control the loop
sum = 0
number = 0

while number < 100:
    number += 1
    sum += number
    if sum >= 100:
        continue
    
print(f"The sum of {number} is ",sum)