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
    fp.close()
    data = text.split("\n")[:-1]
    
    dirs = deque()
    sizes = dict()
    curr_path = ""
    
    # Use an implied state machine, where state transitions are triggered by cd commands.
    for d in data:

        # STATE: Entering a subdirectory. 
        #        Initialize size and full-path name of the subdirectory
        if d[0:5] == "$ cd ":
            dirs.append(d[5:])
            curr_path = get_full_path(dirs)
            sizes[curr_path] = 0

        # STATE: Exiting a directory upward. 
        #        Commit the counted bytes to this directory and its direct parent only.
        elif d[0:7] == "$ cd ..":
            dirs.pop()
            curr_size = sizes[curr_path]
            curr_path = get_full_path(dirs)
            sizes[curr_path] += curr_size
        
        # STATE: Swallow "ls" commands and "dir" listings
        elif d[0:4] == "dir " or d[0:4]=="$ ls":
            pass
        
        # STATE: Found a file. 
        #        Capture number of bytes into current working directory total.
        else:
            sizes[curr_path] += int(d.split(" ")[0])

    # Because the program trace ends in the middle of a branch or on a leaf, so there are 
    # uncommitted sums, we need to do the tail-end of committing the summations up to root.
    while len(dirs) > 1:
        dirs.pop()
        curr_size = sizes[curr_path]
        curr_path = get_full_path(dirs)
        sizes[curr_path] += curr_size

    # Part 1: Compile sum of sizes of dirs < 100k bytes
    n=0
    min_file_size=0
    for s in sizes:
        if sizes[s] < 1e5:
            n += 1
            min_file_size += sizes[s]

    prt_red(min_file_size)

    # Part 2: Figure out  the smallest directory to free, to have 3mm Bytes, or more, available
    prt_grn("Part 2:")

    min_file_size = 2**32
    bytes_requested = 3e7 - (7e7 - sizes["/"])

    for s in sizes:
        if sizes[s] > bytes_requested and sizes[s] < min_file_size:
                min_file_size = sizes[s]

    prt_red(min_file_size)
    

def get_full_path(dirs):
    path = ""
    for d in dirs:
        path = path + d 
    return path

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