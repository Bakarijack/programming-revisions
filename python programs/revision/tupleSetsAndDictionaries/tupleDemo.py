tuple1 = ("green","red", "blue")
print(tuple1)
tuple2 = tuple([1,2,3,4,5])
print(tuple2)

print("Length is : ",len(tuple2))
print("max is : ",max(tuple2))
print("min is : ",min(tuple2))
print("sum is : ",sum(tuple2))

print("The first element is : ",tuple2[0])

tuple3 = tuple1 + tuple2
print(tuple3)

tuple3 = 2 * tuple1
print(tuple3)