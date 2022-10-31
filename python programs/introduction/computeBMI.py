#prompt user to enter weight in pounds
weight = eval(input("Enter weight in pounds: "))

#prompt user to enter height in inches
height = eval(input("Enter your height in inches: "))

KILOGRAMS_PER_POUND = 0.45359297     #constant
METERS_PER_INCH = 0.0254            #constant

#compute BMI
weightInKilograms = weight * KILOGRAMS_PER_POUND
heightInMeters = height * METERS_PER_INCH
bmi = weightInKilograms / (heightInMeters * heightInMeters)

#Display the results
print("MBI is ",format(bmi,".2f"))

if bmi < 18.5 :
    print("Underweight")
elif bmi < 25 :
    print("Normal")
elif  bmi < 30 :
    print("Overweight")
else:
    print("Obese")