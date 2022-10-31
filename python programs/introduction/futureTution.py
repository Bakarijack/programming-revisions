year = 0
tution = 10000

while tution < 20000:
    year += 1
    tution *= 1.07


print("Tutin will be doubled in ",year," years")
print("Tution wil be $ ",format(tution,".2f")," in ",year," years")