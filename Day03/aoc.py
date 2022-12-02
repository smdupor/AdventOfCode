from math import floor, ceil
from printing import prt_grn, prt_red

############################################################ PART 1 ############################################
def part1():
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

    prt_red(str(i))

############################################################ PART 2 ############################################

def part2():
    fp = open("input.txt","r")
    result = []
    i = int(0)
    j = int(0)



    for l in fp:
        continue


    prt_red(str(i))

prt_grn("\nPart 1:")
part1()
prt_grn("\nPart 2:")
part2()
print("")