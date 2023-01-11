from aocutils import *
from printed_parsing import *
import os
import numpy as np
from multiprocessing import Process

SENS = X = 0
BEAC = Y = 1

#1963 is TOO LOW

def aoc_day16():
    fp = open("input.txt","r")
    text = fp.read()
    fp.close() 
    [qty, data] = parse_input(text[:-1].split("\n"))

    
    p1 = part1(qty, data)
    part2(qty,data,p1)



def part2(qty, data,p1):
    mtx = []
    for i in range(0, 22):
        mtx.append([])
        for j in range(0, 22):
            mtx[i].append([])
            for k in range(0, 22):
                mtx[i][j].append(" ")

    for d in data:
        mtx[d[0]+1][d[1]+1][d[2]+1] = "X"
    
    subtr = 0
   
    to_visit = [[0,0,0]]
    
    visited = []
    while len(to_visit) > 0:
        next = to_visit.pop()
        empty = empty_neighbors(next,mtx)
        for mt_neighbor in empty:
            if mt_neighbor not in visited:
                to_visit.append(mt_neighbor)

        if next not in visited and 6 - len(empty) - edge_neighbors(next, mtx) >0:
            subtr += 6 - len(empty) - edge_neighbors(next, mtx)
        visited.append(next)
                    
    print(subtr)

def empty_neighbors(d,mtx):
    to_visit = []
    if d[2]>0 and mtx[d[0]][d[1]][d[2]-1] == " ":
        to_visit.append([d[0],d[1],d[2]-1])
    if d[2]<21 and mtx[d[0]][d[1]][d[2]+1] == " ":
        to_visit.append([d[0],d[1],d[2]+1])
    if d[1] > 0 and mtx[d[0]][d[1]-1][d[2]] == " ":
        to_visit.append([d[0],d[1]-1,d[2]])
    if d[1]<21 and mtx[d[0]][d[1]+1][d[2]] == " ":
        to_visit.append([d[0],d[1]+1,d[2]])
    if d[0]>0 and mtx[d[0]-1][d[1]][d[2]] == " ":
        to_visit.append([d[0]-1,d[1],d[2]])
    if d[0]<21 and mtx[d[0]+1][d[1]][d[2]] == " ":
        to_visit.append([d[0]+1,d[1],d[2]])
    return to_visit

def edge_neighbors(d,mtx):
    edges = 0
    if d[2] == 0 or d[2] == 21:
        edges += 1
    if d[1] == 0 or d[1] == 21:
        edges += 1
    if d[0] == 0 or d[0] == 21:
        edges += 1
    return edges

def search_out(d, mtx):
    pass

def num_sides_touch_k(d,mtx):
    q = 0
    q += 1 if d[0]>0 and mtx[d[0]-1][d[1]][d[2]] == "X" else 0
    q += 1 if d[0]<19 and mtx[d[0]+1][d[1]][d[2]] == "X" else 0
    q += 1 if d[1]>0 and mtx[d[0]][d[1]-1][d[2]] == "X" else 0
    q += 1 if d[1]<19 and mtx[d[0]][d[1]+1][d[2]] == "X" else 0
    # q += 1 if d[2]>0 and mtx[d[0]][d[1]][d[2]-1] == "X" else 0
    # q += 1 if d[2]<19 and mtx[d[0]][d[1]][d[2]+1] == "X" else 0
    return q

def num_sides_touch_j(d,mtx):
    q = 0
    q += 1 if d[0]>0 and mtx[d[0]-1][d[1]][d[2]] == "X" else 0
    q += 1 if d[0]<19 and mtx[d[0]+1][d[1]][d[2]] == "X" else 0
    # q += 1 if d[1]>0 and mtx[d[0]][d[1]-1][d[2]] == "X" else 0
    # q += 1 if d[1]<19 and mtx[d[0]][d[1]+1][d[2]] == "X" else 0
    q += 1 if d[2]>0 and mtx[d[0]][d[1]][d[2]-1] == "X" else 0
    q += 1 if d[2]<19 and mtx[d[0]][d[1]][d[2]+1] == "X" else 0
    return q

def num_sides_touch_i(d,mtx):
    q = 0
    # q += 1 if d[0]>0 and mtx[d[0]-1][d[1]][d[2]] == "X" else 0
    # q += 1 if d[0]<19 and mtx[d[0]+1][d[1]][d[2]] == "X" else 0
    q += 1 if d[1]>0 and mtx[d[0]][d[1]-1][d[2]] == "X" else 0
    q += 1 if d[1]<19 and mtx[d[0]][d[1]+1][d[2]] == "X" else 0
    q += 1 if d[2]>0 and mtx[d[0]][d[1]][d[2]-1] == "X" else 0
    q += 1 if d[2]<19 and mtx[d[0]][d[1]][d[2]+1] == "X" else 0
    return q

def part1(qty, data):
    subtr = qty*6
    p2=qty*6
    p2cuts = 0
   # print(subtr)
    for d in data:
        axis_claimed = [False, False, False]
        for d2 in data:
            if ((d[0] == d2[0] and d[1] == d2[1] and (d[2] - d2[2] == 1 or d[2] - d2[2] == -1)) or
               (d[0] == d2[0] and d[2] == d2[2] and (d[1] - d2[1] == 1 or d[1] - d2[1] == -1)) or
               (d[1] == d2[1] and d[2] == d2[2] and (d[0] - d2[0] == 1 or d[0] - d2[0] == -1))):
                # prt_nocrlf_red(d)
                # prt_nocrlf_red("   ")
                # prt_grn(d2)
                subtr -= 1
                p2 -= 1
            # if (d[0] == d2[0] and d[1] == d2[1] and (d[2] - d2[2] > 1 or d[2] - d2[2] < -1) and not axis_claimed[2]):
            #     p2 -= 1
            #     axis_claimed[2] = True
            #     print (d)
            #     prt_grn(d2)
            #     prt_red(axis_claimed)

            # if (d[0] == d2[0] and d[2] == d2[2] and (d[1] - d2[1] > 1 or d[1] - d2[1] < -1) and not axis_claimed[1]):
            #     p2 -= 1
            #     axis_claimed[1] = True
            #     print (d)
            #     prt_grn(d2)
            #     prt_red(axis_claimed)
            # if (d[1] == d2[1] and d[2] == d2[2] and (d[0] - d2[0] > 1 or d[0] - d2[0] < -1) and not axis_claimed[0]):
            #     p2 -= 1
            #     axis_claimed[0] = True
            #     p2cuts += 1
            #     print (d)
            #     prt_grn(d2)
            #     prt_red(axis_claimed)
    
    # p2 += (p2cuts)
    prt_red(subtr)
    prt_grn(p2)
    return subtr
   
def parse_input(data):
    qty = len(data)
    out = []
    for d in data:
        out.append([int(i) for i in d.split(",")])
    return [qty, out]

   
   
   
    # tupl = parse_input(data)

    # num_thr = 12
    # thr = []
    # block = (len(tupl) // num_thr) + 1
    # for i in range(0,num_thr):
    #     if i*block < len(tupl):
    #         t = Process(target=part2, args=(tupl,np.array([0,0]), 4000000, i*block, (i+1)*block))
    #         thr.append(t)
    #         t.start()
aoc_day16()
