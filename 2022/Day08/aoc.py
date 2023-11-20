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


    # Search Eastward from edge (to the right)
    for i in range(1, len(viz[0])-1):
        vmax = mtx[0][i]
        for j in range(1,len(viz)-1):
            if mtx[j][i] > vmax:
                vmax =  mtx[j][i]
                viz[j][i] = 1

    # Search Westward from edge (to the left)
    for i in range(len(viz[0])-2,0, -1):
        vmax = mtx[len(viz[0])-1][i]
        for j in range(len(viz)-2,0,-1):
            if mtx[j][i] > vmax:
                vmax =  mtx[j][i]
                viz[j][i] = 1

    # Search Southward from Edge
    for j in range(1, len(viz)-1):
        rmax = mtx[j][0]
        for i in range(1,len(viz[0])-1):
            if mtx[j][i] > rmax:
                rmax =  mtx[j][i]
                viz[j][i] = 1

    # Search Northward from edge
    for j in range(len(viz)-2,0, -1):
        rmax = mtx[j][len(viz)-1]
        for i in range(len(viz[0])-2,0,-1):
            if mtx[j][i] > rmax:
                rmax =  mtx[j][i]
                viz[j][i] = 1

    # Part 1 Soln
    sum=0
    for v in viz:
        for u in v:
                sum += u
    prt_red(sum)

    # Part 2
    viewmax = 0
    for i in range(1, len(viz[0])-1):
        for j in range(1,len(viz)-1):
            view = search_views(i,j,mtx)
            if viewmax < view:
                viewmax = view
    prt_grn("Part 2:")
    prt_red(viewmax)

    fp.close()  

def search_views(i,j,mtx):
    # South
    s=0
    for k in range(j+1, len(mtx)):
       s += 1 
       if mtx[k][i] >= mtx[j][i]:
            break

    # North
    n=0
    for k in range(j-1, -1, -1):
        n += 1        
        if mtx[k][i] >= mtx[j][i]:
            break
    
    # East
    e=0
    for k in range(i+1, len(mtx[0])):
        e += 1
        if mtx[j][k] >= mtx[j][i]:
            break

    # West
    w=0
    for k in range(i-1, -1,-1):
        w += 1
        if mtx[j][k] >= mtx[j][i]:
            break

    return (s*n*e*w)

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