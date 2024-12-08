with open("data", "r") as fd:
    lines = fd.readlines()

a = []
b = []

for line in lines:
    values = line.split("   ")
    a.append(int(values[0]))
    b.append(int(values[1]))

a.sort()
b.sort()

tot = 0
for i, v in enumerate(a):
    tot += abs(a[i]-b[i])

print(tot)
