from math import floor, ceil
from aocutils import *

############################################################ PART 1 ############################################
def part1():
    # fp = open("input.txt","r")
    # i = int(0)
    # subval = 0

    # for st in fp:
    #     continue

    # prt_red(str(i))
    return

def part1_naive():
    fp = open("input.txt","r")
    result = []
    i = int(0)
    j = int(0)

    t = [0,0,0,0]
    lines = fp.readlines()
    for k in range(0, 8):
        print(str(k))

    prt_red(str(i))

############################################################ PART 2 ############################################

def part2():
    fp = open("input.txt","r")
    i = int(0)
    
    inp = fp.readlines()
    numstr = len(inp)
    
    for t in range(0,numstr//3):
        continue

    prt_red(str(i))

def part2_naive():
    fp = open("input.txt","r")
    
    result = []
    i = int(0)
    j = int(0)

    t = [0,0,0,0]

    for l in fp:
        k = l[0:-1].split(",")
        t[0] = int(k[0].split("-")[0])
        t[1] = int(k[0].split("-")[1])
        t[2] = int(k[1].split("-")[0])
        t[3] = int(k[1].split("-")[1])

        a = set()
        for p in range(t[0], t[1]+1):
            a.add(p)
        
        b = set()
        for p in range(t[2], t[3]+1):
            b.add(p)
        
        a.intersection_update(b)

        if(len(a) >0):
            i+= 1


    prt_red(str(i))

prt_grn("\nPart 1:")
part1()
part1_naive()
prt_grn("\nPart 2:")
part2()
part2_naive()
print("")