def main():
    outfile = open("Cities.txt", "w")

    #writing data
    outfile.write("Mombasa\n")
    outfile.write("Nairobi\n")
    outfile.write("Kisumu")

    outfile.close() #close the file after writing

    outfile = open("Cities.txt","a")
    outfile.write("\nKilifi\n")
    outfile.write("Kwale")
    outfile.close()

main() #calling the main function