from cgi import print_directory


s1 = "Welcome"
s2 = "Welcome"

print(id(s1) == id(s2))
print(id(s2))

num1 = 45
num2 = 45

print(id(num1) == id(num2))
print(id(num1))

n = 5.5
n2 = 5.5 

print(id(n) == id(n2))
print(id(n))

print(len("Welcome"))

print(s1 * 3)
print("Wel" in s1)

for ch in s1:
    print(ch)