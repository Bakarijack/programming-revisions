#Print grades for the scores
def printGrade(score):
    '''if score < 0 or score > 100:
        print("Invalide score")
        return #same as return None'''
    
    if score >= 90.0:
        print('A')
    elif score >= 80.0:
        print('B')
    elif score >= 70.0:
        print('C')
    elif score >= 60.0:
        print('D')
    else:
        print('F')

def main():
    score = eval(input("Enter a score: "))
    
    while score < 0 or score > 100:
        print("Invalide score ")
        score = eval(input("Enter a score: "))
        
    print("The grade is ",end='')
    printGrade(score)


main() #Invoking the main function