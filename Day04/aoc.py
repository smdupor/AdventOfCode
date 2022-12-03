from math import floor, ceil
from printing import prt_grn, prt_red

############################################################ PART 1 ############################################
def part1():
    fp = open("input.txt","r")
    i = int(0)
    j = int(0)
    subval = 0

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
    result = []
    i = int(0)
    j = int(0)

    subval = 0
    letters = dict()
    
    inp = fp.readlines()
    numstr = len(inp)
    
    for t in range(0,int(numstr/3)):
        continue


    prt_red(str(i))

prt_grn("\nPart 1:")
part1()
prt_grn("\nPart 2:")
part2()
print("")