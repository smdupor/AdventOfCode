from math import floor, ceil
from aocutils import *
from collections import deque
from itertools import *

############################################################ PART 1 ############################################
def part1():
    fp = open("input.txt","r")
    text = fp.read()
    
    for i in range(0,len(text)):
        uniq = []
        for j in range(i, i+4):
            if text[j] not in uniq:
                uniq.append(text[j])

        if len(uniq) == 4:
            prt_red(i+4)
            return

def part1_naive():
    fp = open("input.txt","r")
    text = fp.read()
    data = text.split("\n")
    
    fp.close()
    

############################################################ PART 2 ############################################

def part2():
    fp = open("input.txt","r")
    text = fp.read()

    for i in range(0,len(text)):
        uniq = []
        for j in range(i, i+14):
            if text[j] not in uniq:
                uniq.append(text[j])

        if len(uniq) == 14:
            prt_red(i+14)
            return

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