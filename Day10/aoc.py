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

    r = 1
    cycles = 1
    signal = dict()

    target = 20

    crt = []
    for i in range(0,6):
        crt.append([])
        for j in range(0,40):
            crt[i].append(" ")            

    for d in data:

        a = d.split(" ")
        if a[0] == "addx":
            # print(str(int(a[1])) + " and r = " + str(r))
            [signal, target] = signal_level(cycles, signal, target, r)
            crt = draw(r,crt,cycles)
            cycles += 1
            [signal, target] = signal_level(cycles, signal, target, r)
            crt = draw(r,crt,cycles)
            cycles += 1
            r += int(a[1])
        else:
            [signal, target] = signal_level(cycles, signal, target, r)
            crt = draw(r,crt,cycles)
            cycles += 1
        
    
    sum = signal[20]
    # print(signal)
    for i in range(1,6):
        # print(20+(i*40))
        sum += signal[20+(i*40)]


    prt_red(sum)

    # Part 2
    
    prt_grn("Part 2:")

    print(cycles)

    for i in range(0,6):
        for j in range(0,40):
            print(crt[i][j], end="")
        print(" ")
    

    fp.close()  

def draw(r, crt, cycles):
    row = (cycles-1) // 40
    col = (cycles-1) % 40
    if col == r - 1 or col == r or col == r+1:
        crt[row][col] = "#"
    else:
        crt[row][col] = "."
    return crt

def signal_level(cycles, signal,target,r):
    if target == 20 and cycles == 20:
        # print(cycles)
        signal[cycles] = (cycles * r)
        target += 40
    elif target > 20 and cycles == target:
        # print(cycles)
        signal[cycles] = (cycles * r)
        target += 40
    return [signal, target]
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