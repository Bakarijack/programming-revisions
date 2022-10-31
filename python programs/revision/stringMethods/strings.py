#creating strings
st1 = str()
st2 = str("Welcome to strings")
print(st2)

name = "Bakari"
print(name)

x = 10
y = 10     
print(id(x))
print(id(y))

s = input("Enter a string : ")
print("max ",max(s))
print("min ",min(s))
print(s[3])
print(s[0 : 3])
print(s * 3)

print("aka" in s)
print("aka" not in s)

if len(s) % 2 == 0:
    print("even number characters")
else:
    print("odd number characters")