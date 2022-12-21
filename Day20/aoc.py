from aocutils import *
from printed_parsing import *
import os
import numpy
from multiprocessing import Process

SENS = X = 0
BEAC = Y = 1

#1963 is TOO LOW

def aoc_day19():
    fp = open("testinput.txt","r")
    text = fp.read()
    fp.close() 
    vec = parse_input(text[:-1].split("\n"))
    part1b(vec)

def part1b(vec):
    test=[
    
    [2, 1, -3, 3, -2, 0, 4],
    [1, -3, 2, 3, -2, 0, 4],
    [1, 2, 3, -2, -3, 0, 4],
    [1, 2, -2, -3, 0, 3, 4],
    [1, 2, -3, 0, 3, 4, -2],
    [1, 2, -3, 0, 3, 4, -2],
    [1, 2, -3, 4, 0, 3, -2]]
    out = vec.copy()
    for z,v in enumerate(vec):
        dist = v
        k = out.index(v)
        k2 = k + dist
        while k2 < 0:
            k2 += len(out)
        if k2 > len(out): 
            k2 += 1
        while k2 > len(out):
            k2 -= len(out)-1
        
        # out.remove(v)
        # print(out)
        # out = lrot(out, abs(v)) if v > 0 else rrot(out, abs(v))
        # print(out)
        # out.insert(k,v)
        # out = rrot(out, abs(v)) if v > 0 else lrot(out, abs(v))
        if v > 0:
            
            out.remove(v)
            out.insert(k2,v)
        if v < 0:
            if k2 == 0:
                k2 = len(out)
            out.remove(v)
            out.insert(k2,v)
        
        print(out)
        prt_grn(test[z])
        print("")
    k = out.index(0)
    sum = 0
    for i in range(1,4):
        k2 = k + (1000*i)
        while k2 > len(out):
            k2 -= len(out)
        print(k2)
        print(len(out))
        sum += out[k2]
    prt_red(sum)

def lrot(out, dist):
    while dist > 0:
        out.append(out.pop(0))
        dist -= 1
    return out

def rrot(out,dist):
    while dist > 0:
        out.insert(0, out.pop())
        dist -= 1
    return out

def part1(vec):
    out = vec.copy()
    for v in vec:
        moves = v
        k = out.index(v)
        print(out)
        while moves != 0:
            if moves > 0 and k+1 < len(out)-1:
                out[k] = out[k+1]
                out[k+1] = v
                k +=1
            elif moves > 0:
                for i in range(len(out)-2, 0):
                    out[i+1] = out[i]
                
                out [1] = v
                k = 1
            elif moves < 0 and k - 1 > 0:
                out[k] = out[k-1]
                out[k-1] = v
                k -= 1
            # elif moves == -1 and k-1 == 0:
            #     for i in range(1,len(out)):
            #         out[i-1] = out[i]
            #     out[len(out)-1] = v
            #     k = len(out)-1
          
            elif moves < 0:
                for i in range(1,len(out)-1):
                    out[i-1] = out[i]
                out[len(out)-2] = v
                k = len(out)-2
            
            moves = moves - 1 if moves > 0 else moves + 1
    print(out)
    
   
def parse_input(data):
    out = []
    for d in data:
        out.append(int(d))
    return out
aoc_day19()
