import  time

currentTme = time.time()  #get the current time

#Obtain the total seconds since midnight Jan 1 1970
totalSecods =int(currentTme)

#get the current seconds
currentSeconds = totalSecods % 60

#obtain the total minutes
totalMinutes =  totalSecods // 60

#compute the current minutes in hour
cuurentMinutes = totalMinutes % 60

#obtain the total hours
totalHours = totalMinutes // 60

#compute the current hour
cuurentHour = totalHours % 24

#Display the results
print("Current time is ",cuurentHour,":",cuurentMinutes,":",currentSeconds," GMT")
