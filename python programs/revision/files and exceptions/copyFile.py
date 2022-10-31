from itertools import count
import  os.path
import sys

def main():
    f1 = input("Enter a source file: ").strip()
    f2 = input("Enter the target file: ").strip()

    #check if the target file exist
    if os.path.isfile(f2):
        print(f2," already exists")
        sys.exit()

    infile = open(f1,"r")
    outfile = open(f2,"w")

    #copy from input file to output file
    countLines = countChars = 0
    for line in infile:
        countLines += 1
        countChars += len(line)
        outfile.write(line)
    
    print(countLines, " lines and ", countChars," chars copied")

    infile.close()
    outfile.close()


main() #calling the main function