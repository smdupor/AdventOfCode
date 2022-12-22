from aocutils import *
from printed_parsing import *
import os
import numpy
from multiprocessing import Process

SENS = X = 0
BEAC = Y = 1

#1963 is TOO LOW

def aoc_day17():
    fp = open("testinput.txt","r")
    text = fp.read()
    fp.close() 
    ops = parse_input(text[:-1].split("\n"))
    blocks = make_blocks()

    part1(ops,blocks)

def part1(ops, blocks):
    optr = 0
    bptr = 0
    fptr = 0
    bcount = 0
    floor = [1,1,1,1,1,1,1]

    while bcount <= 2:
        # prevblock = currblock
        
        currblock = blocks[bptr].copy()
        print(currblock)
        print(floor)
        print(fptr)
        bptr = bptr + 1 if bptr < 4 else 0
        # prt_grn(bptr)
        insert = fptr+7
        for j in range(0, len(currblock[0])):
            for i in range(0,len(currblock)):
                if currblock[i][j] == 1:
                    currblock[i][j] = insert - i
        stop = False
        while not stop:
            currblock = lsh(currblock) if ops[optr] else rsh(currblock)
            optr = optr + 1 if optr < len(ops)-1 else 0
            if sum(currblock[len(currblock)-1])>0:
                stop =  False
                for i,b in enumerate(currblock[len(currblock)-1]):
                    if b > 0 and  floor[i] > 0:
                        stop = True
                        break
                if stop:
                    cont = True
                    for i in range(0, len(currblock)):
                        if cont:
                            for j in range(0, len(currblock[0])):
                                if currblock[i][j] != 0:
                                    fptr = currblock[i][j]
                                    break
        bcount += 1
        # print(bcount)
        print(currblock)
    print(currblock)

def rsh(blk):
    for i in range(0, len(blk)-1):
        if blk[i][len(blk[0])-1] != 0:
            return blk
    for j in range(len(blk[0])-1, -1, -1):
        for i in range(0, len(blk)):
            blk[i][j] = blk[i][j-1]
    return blk

def lsh(blk):
    for i in range(0, len(blk)-1):
        if blk[i][0] != 0:
            return blk
    for j in range(0,len(blk[0])-1):
        for i in range(0, len(blk)):
            blk[i][j] = blk[i][j+1]
    return blk

def make_blocks():
    blocks = []
    bk = numpy.array(
         [[0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,1,1,1,1,0]])
    blocks.append(bk)
    bk = numpy.array([
          [0,0,0,0,0,0,0],
          [0,0,0,1,0,0,0],
          [0,0,1,1,1,0,0],
          [0,0,0,1,0,0,0]])
    blocks.append(bk)
    bk = numpy.array([ 
          [0,0,0,0,0,0,0],
          [0,0,0,0,1,0,0],
          [0,0,0,0,1,0,0],
          [0,0,1,1,1,0,0]])
    blocks.append(bk)
    bk = numpy.array([
          [0,0,1,0,0,0,0],
          [0,0,1,0,0,0,0],
          [0,0,1,0,0,0,0],
          [0,0,1,0,0,0,0]])
    blocks.append(bk)
    bk = numpy.array([
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,1,1,0,0,0],
          [0,0,1,1,0,0,0]])
    blocks.append(bk)
    return blocks

   
def parse_input(data):
    out = []
    data = data[0]
    for d in data:
        if d == "<":
            out.append(-1)
        elif d == ">":
            out.append(1)
    return out
aoc_day17()
