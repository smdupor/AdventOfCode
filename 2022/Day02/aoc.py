def part2_orig():
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

def part2_improved():
    fp = open("input.txt","r")
    result = []
    i = int(0)
    j = int(0)

    # The base point values
    X=1 # Rock / (Lose)
    Y=2 # Paper / (Draw)
    Z=3 # Scissor / (Win)
    
    lose = 0 # X in flatfile
    draw = 3 # Y in flatfile
    win = 6 # Z in flatfile

    # Points basis for rock / paper / scissor
    lookup = dict()
    lookup['X'] = dict()
    lookup['X']['C'] = Y
    lookup['X']['A'] = Z
    lookup['X']['B'] = X

    lookup['Y'] = dict()
    lookup['Y']['C'] = Z
    lookup['Y']['A'] = X
    lookup['Y']['B'] = Y
    
    lookup['Z'] = dict()
    lookup['Z']['C'] = X
    lookup['Z']['A'] = Y
    lookup['Z']['B'] = Z

    # Win / lose / draw lookup table
    wld = dict()
    wld['X'] = lose
    wld['Y'] = draw
    wld['Z'] = win

    for l in fp:
        i += wld[l[2]]
        i += lookup[l[2]][l[0]]

    print(str(i))

part2_orig()
part2_improved()