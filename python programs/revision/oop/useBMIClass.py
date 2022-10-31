from BMI import BMI

def main():
    bmi1 = BMI("Bakari Kilu", 26, 50, 90)

    print("The BMI for ",bmi1.getName()," is ",bmi1.getBMI()," ",bmi1.getStatus())

main() #calling the main function