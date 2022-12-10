from math import floor, ceil
from aocutils import *
from collections import deque
from itertools import *

############################################################ PART 1 ############################################
def part1():
    fp = open("input.txt","r")
    text = fp.read()
    data = text.split("\n")

    
    fp.close()

def part1_naive():
    fp = open("input.txt","r")
    text = fp.read()
    data = text.split("\n")
    data = data[:-1]

    # Set up both a matrix of the treemap, and a visibility matrix (Initialize as all-invisible)
    mtx = []
    viz = []
    i=-1
    for d in data:
        mtx.append([])
        viz.append([])
        i += 1
        for e in d:
            mtx[i].append(int(e))
            viz[i].append(0)


    # Make all four edges visible
    for i in range(0, len(viz[0])):
        viz[0][i] = 1
        viz[len(viz)-1][i] = 1
    for i in range(0, len(viz)):
        viz[i][0] = 1
        viz[i][len(viz[0])-1] = 1


    
    # Part 1 Soln
    sum=0
    for v in viz:
        for u in v:
                sum += u
    prt_red(sum)

    # Part 2
    
    prt_grn("Part 2:")
    

    fp.close()  
############################################################ PART 2 ############################################

def part2():
    fp = open("input.txt","r")
    text = fp.read()


    fp.close()


prt_grn("\nPart 1:")
part1()
part1_naive()
# prt_grn("\nPart 2:")
part2()
# part2_naive()
# print("")