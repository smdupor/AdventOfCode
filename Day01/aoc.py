fp = open("input.txt","r")
result = []
i = int(0)
for l in fp:
    if(len(l) > 1):
        i += int(l)
    else:
        result.append(i)
        i = int(0)

result.sort()

print(result[-1])
print(result[-1] + result[-2] + result[-3])

fp.close()