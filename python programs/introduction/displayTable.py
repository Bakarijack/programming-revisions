
print("                   Multiplication Table")

print("     ",end='')
#display the header numbers
for i in range(1,10):
    print(format(i,"6d"),end='')
print()
print("...........................................................")

#display the rows
for i in range(1,10):
    print(i," | ",end='')
    for j in range(1,10):
        print(format(i*j,"6d"),end='')
    print("\n")