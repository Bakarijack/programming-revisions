def printArea(width = 1,height = 2):
    area = width * height
    print("Width : ",width,"\tHeight : ",height,"\tArea : ",area)

printArea() #use all default args
printArea(4,2.5) #positional args
printArea(height = 5,width = 3) #keyword args
printArea(width = 12) #default height
printArea(height = 6.2) #default width