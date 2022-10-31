from this import d


d1 = {'A':100,'B':200}

key = input("Enter the key: ")

if key in d1:
    print(f"The value of {key} is : ",d1[key])
else:
    print(f"{key} is not in the dictionary!")
    print("The keys available are : ")

    for i in d1:
        print(i, end=" ")
print()
print(list(d1))
print(list(d1.values()))
print(list(d1.items()))