import time

seconds = eval(input("Enter the total seconds : "))

minutes = seconds // 60

remainSeconds = seconds % 60

print(minutes," minutes ",remainSeconds," seconds")

value = 5.6
print("original value ", value)
print("after convert it to integer ",int(value))
print("using the round function ",round(value))

totalSeconds = int(time.time())
print("total seconds ",totalSeconds)

totalMinutes = totalSeconds // 60
print("total minutes ",totalMinutes)

currentMinutes = totalMinutes % 60
print("Current minutes ",currentMinutes)

totalHours = totalMinutes // 60
print("total hours ",totalHours)

currentHours = totalHours % 24
print("current hours ",currentHours) 