from math import floor, ceil
from aocutils import *

############################################################ PART 1 ############################################
def part1():
    fp = open("input.txt","r")
    i = int(0)
    subval = 0

    for st in fp:
        lhs = st[0:len(st)//2]
        rhs = st[len(st)//2:]
        subval = set(lhs).intersection(rhs)
        i += char_to_val(subval.pop())

    prt_red(str(i))

def part1_naive():
    fp = open("input.txt","r")
    result = []
    i = int(0)
    j = int(0)
    subval = 0
    letters = dict()

    for l in fp:
        subval = '\0'
        length = len(l)-1
        for k in range (0,int((length/2) )):
            for m in range(int(length/2),length):
                if(l[k] == l[m]):
                    subval = l[k]
                    break
            if(subval != '\0'):
                break
        
        j = ord(subval)

        if(j > 96):
            i+= j-96
        else:
            i+= (j-64)+26

    prt_red(str(i))

############################################################ PART 2 ############################################

def part2():
    fp = open("input.txt","r")
    i = int(0)
    
    inp = fp.readlines()
    numstr = len(inp)
    
    for t in range(0,numstr//3):
        a = set(inp[(t*3)][0:-1])
        b = set(inp[((t*3)+1)][0:-1])
        c = set(inp[((t*3)+2)][0:-1])
        a.intersection_update(b)
        a.intersection_update(c)
        i+= char_to_val(a.pop())

    prt_red(str(i))

def part2_naive():
    fp = open("input.txt","r")
    result = []
    i = int(0)
    j = int(0)

    subval = 0
    letters = dict()
    
    inp = fp.readlines()
    numstr = len(inp)
    
    for t in range(0,int(numstr/3)):
        subval = '\0'
        for j in inp[(t*3)]:
            for k in inp[(t*3)+1]:
                for m in inp[(t*3)+2]:
                    if(j ==k and j == m):
                        subval = j
                        break
                if(subval != '\0'):
                    break
            if(subval != '\0'):
                    break
        j = ord(subval)

        if(j > 96):
            i+= j-96
        else:
            i+= (j-64)+26


    prt_red(str(i))

prt_grn("\nPart 1:")
part1()
part1_naive()
prt_grn("\nPart 2:")
part2()
part2_naive()
print("")