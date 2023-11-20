from aocutils import *
from printed_parsing import *
import os
import numpy as np
import re
from multiprocessing import Process

EAST = np.array([0,1])
WEST = np.array([0,-1])
NORTH = np.array([-1, 0])
SOUTH = np.array([1, 0])

def aoc_day21():
    fp = open("input.txt","r")
    text = fp.read()
    fp.close() 
    
    [mtx, moves] = parse_input(text[:-1])
    p1(mtx, moves)

def p1(mtx, moves):
    coord = np.array([0,0])
    for t in mtx[0]:
        if t != " ":
            break
        coord[1] += 1
    dir = EAST
    count = 1
    for m in moves:
        move_l(mtx, coord, dir, int(m[0]))
        dir = turn(dir, m[1])
        count += 1
        print(coord)
        print(dir)
        if count > 5:
            break

        # print(coord)
def turn(dir, key):
    if key == "R":
        if dir.all() == EAST.all():
            dir = SOUTH
        elif dir.all() == SOUTH.all():
            dir = WEST
        elif dir.all() == WEST.all():
            dir = NORTH
        elif dir.all() == NORTH.all():
            dir  = EAST
        else:
            prt_red("LOGIC FAILURE")
    elif key == "L":
        if dir.all() == EAST.all():
            dir = NORTH
        elif dir.all() == NORTH.all():
            dir  = WEST
        elif dir.all() == SOUTH.all():
    
            dir = EAST
        elif dir.all() == WEST.all():
            dir = SOUTH
        else:
            prt_red("LOGIC FAILURE")
    return dir

def move_l(mtx, coord, dir, qty):
    while qty > 0:
        coord += dir
        qty -= 1
        if mtx[coord[0]][coord[1]] == " ":
            [coord, stop] = wrap(mtx, coord, dir)
            if stop:
                qty = 0
        elif mtx[coord[0]][coord[1]] == "#":
            coord -= dir
        return coord

def wrap(mtx, coord, dir):
    backup = coord.copy()
    if dir.all() == EAST.all():
        coord[1] = 0
        while (mtx[coord[0]][coord[1]] == " "):
            coord[1] += 1
        if mtx[coord[0]][coord[1]] == ".":
            return [coord, False]
        else:
            return [backup, True]

    if dir.all() == WEST.all():
        coord[1] = len(mtx[0])-1
        while (mtx[coord[0]][coord[1]] == " "):
            coord[1] -= 1
        if mtx[coord[0]][coord[1]] == ".":
            return [coord, False]
        else:
            return [backup, True]

    if dir.all() == NORTH.all():
        coord[0] = len(mtx)-1
        while (mtx[coord[0]][coord[1]] == " "):
            coord[0] -= 1
        if mtx[coord[0]][coord[1]] == ".":
            return [coord, False]
        else:
            return [backup, True]

    if dir.all() == SOUTH.all():
        coord[0] = 0
        while (mtx[coord[0]][coord[1]] == " "):
            coord[0] += 1
        if mtx[coord[0]][coord[1]] == ".":
            return [coord, False]
        else:
            return [backup, True]

def parse_input(data):
    out = []
    txt = data.split("\n\n")
    # print(txt)
    mat = txt[0].split("\n")
    for i,m in enumerate(mat):
        out.append([])
        for c in m:
            out[i].append(c)
        while len(out[i])< 150:
            out[i].append(" ")
    dist  = re.split("[L,R]", txt[1])
    dir = re.split("[0-9]+", txt[1])
    dir = dir[1:]
    directions = []
    # prt_red("asdf")
    
    for i in range(0, len(dist)):
        directions.append([])
        directions[i] = [dist[i], dir[i]]
        # print(directions[i][0]+directions[i][1], end="")
    # print(out)
    return [out, directions]
aoc_day21()
