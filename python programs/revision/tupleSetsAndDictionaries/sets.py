s1 = set() #empty set
print(s1)
s2 = {1,2,3,4}
print(s2)
s3 = set([1,26,4])
print(s3)
s4 = set([x * 2 for x in range(1, 10)])
print(s4)
s3.add(67)
print(s3)
s2.remove(1)
print(s2)
print(4 in s3)
print(s2.issubset(s3))
print(s2.intersection(s3))

s5 = {1,2,3,4,5}
s6 = {1,2,6}
print(s5.union(s6))