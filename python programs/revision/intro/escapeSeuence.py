print("\"This is \n the quote\"")

print("Bakari"," ", end="")
print("Kilu")

s = str(56)
print(s)

name = "\tBakari " + "Mtua"
print(name)
print("My name is "+name)
print(id(name))
print(type(name))

print(name.upper().strip())  #strip() is used to remove the whitespace from a word

city = input("Enter your currrent city : ").strip().upper()
print(city)

#formatting the numbers
print(format(5.45764653535,"10.2f"))
print(format(5.45764653535,"<10.2f"))
print(format(5.45764653535,".2f"))
print(format(5.45764653535,".2e"))