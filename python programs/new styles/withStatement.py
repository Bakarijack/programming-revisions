with open("myfile.txt","w") as file:
    file.write("Hello World!")

with open("myfile.txt","r") as outfile:
    print(outfile.read())