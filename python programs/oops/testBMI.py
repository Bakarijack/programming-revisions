from BMI import BMI

def main():
    bmi1 = BMI("Bakari",27,55,70)
    print("The BMI for ",bmi1.getName()," is ",\
        bmi1.getBMI(),bmi1.getStatus())
    
    bmi2 = BMI("Kilu",20,215,80)
    print("The BMI for ",bmi2.getName()," is ",\
        bmi2.getBMI(),bmi2.getStatus())
    
    
main() #call the main method