#iterate over a list
print("List Iteration")
l = ["Bakari","Mtua","Kilu"]
for i in l:
    print(i)


print("\nTuple Iteration")
t = ("Hello","World")
for i in t:
    print(i)


print("\nString Iteration")
s = "Bakari"
for i in s:
    print(i)


print("\nDictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 456
for i in d:
    print("%s %d" %(i, d[i]))