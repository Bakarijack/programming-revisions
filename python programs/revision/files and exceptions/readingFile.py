inputContent = open("Cities.txt", "r")
print("1. Using read()")
print(inputContent.read())  #reads all the content
print(inputContent.read().splitlines()) #test
inputContent.close()

inputContent = open("Cities.txt","r")
print("2. Using read(number)")
s1 = inputContent.read(4)
print(s1)
s2 = inputContent.read(10)
print(repr(s2))
inputContent.close()

inputContent = open("Cities.txt","r")
print("3. Using readline()")
line1 = inputContent.readline()
line2 = inputContent.readline()
line3 = inputContent.readline()
line4 = inputContent.readline()
print(repr(line1))
print(repr(line2))
print(repr(line3))
print(repr(line4))
inputContent.close()

inputContent = open("Cities.txt","r")
print("4. Using readlines()")
print(inputContent.readlines())
inputContent.close()