from math import floor, ceil
from aocutils import *
from collections import deque
from itertools import *

############################################################ PART 1 ############################################
def part1():
    fp = open("input.txt","r")
    text = fp.read()
    data = text.split("\n")

    dirs = deque()

    sizes = dict()

    curr = ""
    data = data[:-1]
    n=0
    for d in data:
        n+=1
        if d[0:7] == "$ cd ..":
            print(d)
            dirs.pop()
            currsz = sizes[curr]
            curr = ""
            for d in dirs:
                curr = curr + d 
                sizes[curr] += currsz
        elif d[0:5] == "$ cd ":
            print(d)
            dirs.append(d[5:])
            print(dirs)
            curr = ""
            for d in dirs:
                curr = curr + d 
            sizes[curr] = 0
            

        elif d[0:4] == "dir " or d[0:4]=="$ ls":
            t=0
        else:
            print(d)
            sizes[curr] += int(d.split(" ")[0])

    n=0
    m=0
    for s in sizes:
        if sizes[s] < 100000:
            n += 1
            m += sizes[s]

    prt_red(n)
    prt_red(m)



def part1_naive():
    fp = open("input.txt","r")
    text = fp.read()

    return

    fp.close()  
############################################################ PART 2 ############################################

def part2():
    fp = open("input.txt","r")
    text = fp.read()
    data = text.split("\n")

    dirs = deque()

    sizes = dict()

    sizes_uniq = dict()
    curr = ""
    data = data[:-1]
    n=0
    prevdd = False
    for d in data:
        n+=1
        if d[0:7] == "$ cd ..":
            #print(d)
            dirs.pop()
            #if not prevdd:
            currsz = sizes[curr]
            sizes_uniq[curr] = sizes[curr]
             #   prevdd = True
                #for d in dirs:
                    #sizes[curr] += currsz
            
            curr = ""
            for d in dirs:
                curr = curr + d 
            sizes[curr] += currsz
                
        elif d[0:5] == "$ cd ":
            prevdd = False
            #print(d)
            dirs.append(d[5:])
            #print(dirs)
            curr = ""
            for d in dirs:
                curr = curr + d 
            sizes[curr] = 0
            

        elif d[0:4] == "dir " or d[0:4]=="$ ls":
            t=0
        else:
            #print(d)
            sizes[curr] += int(d.split(" ")[0])
    


    while len(dirs) > 1:
        dirs.pop()
        
        currsz = sizes[curr]
        sizes_uniq[curr] = sizes[curr]
    
    
        curr = ""
        for d in dirs:
            curr = curr + d 
    
        sizes[curr] += currsz

    
    n=0
    m=2**32

    print(70000000 - sizes["/"])

    cnst = 30000000 - (70000000 - sizes["/"])
            
    prt_grn(cnst)

    for s in sizes:
        
        if sizes[s] > cnst:
            print(sizes[s])
            if sizes[s]<m:
                m = sizes[s]
                

    prt_red(n)
    prt_red(m)

    #print(sizes)

def part2_naive():
    fp = open("input.txt","r")
    text = fp.read()

    return

    fp.close()

prt_grn("\nPart 1:")
part1()
part1_naive()
prt_grn("\nPart 2:")
part2()
part2_naive()
print("")