from math import floor, ceil
from aocutils import *
from collections import deque
from itertools import *

############################################################ PART 1 ############################################
def part1():
    return


def part1_naive():
    fp = open("input.txt","r")
    text = fp.read()
    data = text.split("\n")
    data = data[:-1]
    
    dirs = deque()
    sizes = dict()
    curr = ""
    
    n=0
    for d in data:
        n+=1

        # State: Exiting a directory upward. Commit the counted bytes to this directory and its direct parent only.
        if d[0:7] == "$ cd ..":
            dirs.pop()
            currsz = sizes[curr]
            curr = ""
            for d in dirs:
                curr = curr + d 
            sizes[curr] += currsz
        
        # State: Entering a subdirectory. Initialize size and full-path name of the subdirectory
        elif d[0:5] == "$ cd ":
            dirs.append(d[5:])
            curr = ""
            for d in dirs:
                curr = curr + d 
            sizes[curr] = 0
        
        # State: Swallow "ls" commands and "dir" listings
        elif d[0:4] == "dir " or d[0:4]=="$ ls":
            t=0
        
        # State: Found a file. Capture number of bytes into current working directory total.
        else:
            sizes[curr] += int(d.split(" ")[0])

    # Because we can stop without committing upwards all the way to root, for the last branch searched
    # Pop all directories up to root, committing the last set of byte counts
    while len(dirs) > 1:
        dirs.pop()
        currsz = sizes[curr]
        curr = ""
        for d in dirs:
            curr = curr + d 

        sizes[curr] += currsz

    # Part 1: Compile sum of sizes of dirs < 100k bytes
    n=0
    m=0
    for s in sizes:
        if sizes[s] < 100000:
            n += 1
            m += sizes[s]

    prt_red(m)

    # Part 2: Figure out  the smallest directory to free, to have 3mm Bytes, or more, available
    prt_grn("Part 2:")
    n=0
    m=2**32

    cnst = 30000000 - (70000000 - sizes["/"])

    for s in sizes:
        if sizes[s] > cnst and sizes[s]<m:
                m = sizes[s]

    prt_red(m)
    fp.close()

############################################################ PART 2 ############################################

def part2():
    return


def part2_naive():
    fp = open("input.txt","r")
    text = fp.read()

    fp.close()

prt_grn("\nPart 1:")
part1()
part1_naive()
# prt_grn("\nPart 2:")
# part2()
# part2_naive()
# print("")