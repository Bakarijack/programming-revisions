import string
print("...........1st method(importing string class)...........")
ltrs = string.ascii_lowercase

print(ltrs)
print(len(ltrs))


for i in range(0,len(ltrs)):
    print(ltrs[i],end=", ")

print()
print("..........2nd method (using chr() function)...........")
y = chr(65)

print(type(y),y)

for i in range(65,65+25):
    print(chr(i).lower(),end=', ')  #lower() returns the lowercase
    
print()
print("..........3rd method(using ord() function................")
y = ord('A')
print(type(y),y)

alphabet_list = string.ascii_uppercase

for i in alphabet_list:
    print(ord(i),end=', ')
print() 