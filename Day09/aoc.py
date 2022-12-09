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
    # mtx = []
    # viz = []
    # i=-1
    # for d in data:
    #     mtx.append([])
    #     viz.append([])
    #     i += 1
    #     for e in d:
    #         mtx[i].append(int(e))
    #         viz[i].append(0)

    prt_red(0)

    # Part 2

    prt_grn("Part 2:")
    prt_red(0)

    fp.close()  

############################################################ PART 2 ############################################

def part2():
    fp = open("input.txt","r")
    text = fp.read()
    data = text.split("\n")
    fp.close()

    #print(sizes)

def part2_naive():
    fp = open("input.txt","r")
    text = fp.read()

    return

    fp.close()

prt_grn("\nPart 1:")
part1()
part1_naive()
# prt_grn("\nPart 2:")
# part2()
# part2_naive()
# print("")