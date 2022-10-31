import random

def createMatrix(totalRows, totalColumns):
    matrix = [] #create an empty matrix
    for row in range(totalRows):
        matrix.append([])
        for col in range(totalColumns):
           # value = eval(input("Enter the number in row "+str(row + 1)+" column "+str(col + 1)+" : "))
           # matrix[row].append(value)
           matrix[row].append(random.randint(0, 99))

    return matrix

def main():
    numberOfRows = eval(input("Enter the number of rows: "))
    numberOfColumns = eval(input("Enter the number of columns: "))

    matrixCopy = createMatrix(numberOfRows, numberOfColumns)
    print(matrixCopy)
    printMatrix(matrixCopy)
    print("Sum of the matrix is :", sumMatrix(matrixCopy))
    matrixCopy.sort()
    print(matrixCopy)

    
def printMatrix(mtx):
    for row in mtx:
        for value in row:
            print(value, end=" ")
        print() #line break

def sumMatrix(mtx):
    sum = 0
    for row in mtx:
        for value in row:
            sum += value
        
    return sum

main() #calling the main function
