import pickle

def main():
    #open a file for writing
    outfile = open("pickle.dat","wb")
    pickle.dump(45, outfile)
    pickle.dump(56, outfile)
    pickle.dump("Programming", outfile)
    pickle.dump([1,2,3,4,5], outfile)
    outfile.close()

    infile = open("pickle.dat","rb")

    end_of_file = False
    while not end_of_file:
        try:
            print(pickle.load(infile), end=" ")
        except EOFError:
            end_of_file = True
    print()
    infile.close()

    '''infile = open("pickle.dat","rb")
    print(pickle.load(infile))
    print(pickle.load(infile))
    print(pickle.load(infile))
    print(pickle.load(infile))
    infile.close()
'''
main() #calling the main function