fp = open("input.txt","r")
result = []
i = int(0)
j = int(0)
X=1
Y=2
Z=3
lose = 0
draw = 3
win = 6

for l in fp:
    me = 0
    if(l[2] == 'X'):
        me += lose
        if(l[0] == 'C'):
            me += Y
        elif(l[0] == 'A'):
            me += Z
        else:
            me += X
    elif(l[2] == 'Y'):
        me += draw
        if(l[0] == 'A'):
            me += X
        elif(l[0] == 'B'):
            me += Y
        else:
            me += Z
    elif(l[2] == 'Z'):
        me += win
        if(l[0] == 'B'):
            me += Z
        elif(l[0] == 'C'):
            me += X
        else:
            me += Y
    i += me

print(str(i))
