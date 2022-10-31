from random import randint

nums = []

for i in range(20):
    nums.append(randint(1, 100))


print(nums)
print(sum(nums))
print(sum(nums) / len(nums))

nums.sort()

print("The largest number is the list is ",nums[-1])
print("The smallest number is the list is ",nums[0])

print("The second largest in the list is ",nums[-2])
print("The second smallest in the list is ", nums[1])

countEven = 0
for i in nums:
    if i % 2 == 0:
        countEven = countEven + 1

print("The number of eve numbers in the list is ",countEven)