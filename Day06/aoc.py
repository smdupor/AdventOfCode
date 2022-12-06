from math import floor, ceil
from aocutils import *
from collections import deque

############################################################ PART 1 ############################################
def part1():
    fp = open("input.txt","r")
    result = []
    i = int(0)
    j = int(0)

    lines = fp.readlines()
    val = []
    j=0
    for k in range(7,-1,-1):
        continue

    #prt_red(str(i))
    fp.close()

def part1_naive():
    # Open file
    fp = open("input.txt","r")
    text = fp.read()
    data = text.split("\n")
    stack = deque()
    


    fp.close()
    

############################################################ PART 2 ############################################

def part2():
    fp = open("input.txt","r")
    i = int(0)
    
    inp = fp.readlines()
    numstr = len(inp)
    
    for t in range(0,numstr//3):
        continue

    #prt_red(str(i))
    fp.close()

def part2_naive():
    fp = open("input.txt","r")
    text = fp.read()
    data = text.split("\n")
    stack = deque()

    fp.close()

prt_grn("\nPart 1:")
part1()
part1_naive()
prt_grn("\nPart 2:")
part2()
part2_naive()
print("")