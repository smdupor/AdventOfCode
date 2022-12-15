from aocutils import *
from printed_parsing import *
import os
import numpy as np

SENS = X = 0
BEAC = Y = 1

def aoc_day15():
    fp = open("testinput.txt","r")
    text = fp.read()
    fp.close() 
    data=text[:-1].split("\n")
    tupl = parse_input(data)
    # for t in tupl:
    #     print(t[1])
    # print(get_manh_dist(tupl[0][0][0], tupl[0][0][1]))
    # print(tupl[0])
    part2(tupl, np.array([0,0]), 4000000)

def part2(tupl, coord, dist):
    ring = []
    # mtx = setup_mtx(20,20,".")
    for t in tupl:
        c = t[0][0].copy()
        # print(c)
        c[0] -= (t[1]+1)
        # print(c)
        # print(t[0][0][1])
        while c[0] < t[0][0][0]:
            c[0] += 1
            c[1] -= 1
            # print(c)
            ring.append(c.copy())
        while c[1] < t[0][0][1]:
            c[0] += 1
            c[1] += 1
            ring.append(c.copy())
        while c[0] > t[0][0][0]:
            c[0] -= 1
            c[1] += 1
            ring.append(c.copy())
        while c[1] > t[0][0][1]:
            c[0] -= 1
            c[1] -= 1
            ring.append(c.copy())

    print(len(ring))
    for r in ring:
        if r[0] > 0 and r[1] > 0:
            test = True
            for t in tupl:
                if get_manh_dist(r,t[0][0]) < t[1]:
                    test=False
            if test:
                prt_red(r)
                exit()
                    
        # print(ring)
        # for r in ring:
        #     mtx[r[1]][r[0]] = "x"
        # mtx[t[0][0][1]][t[0][0][0]]="o"
        # for m in mtx:
        #     for n in m:
        #         print(n, end="")
        #     print("")
        # exit()
def part1(tupl):
    coord = np.array([0,10])
    gap = 0
    count = 0
    cand = []
    while (gap < 10000):
        for t in tupl:
            # print(t)
            if get_manh_dist(t[0][0], coord) <= t[1]:
                
                gap = 0
                count += 1
                break
        gap += 1
        coord[0] -= 1
    print(count)
    print(coord)
    gap = 0
    coord = np.array([1,10])
    while (gap < 10000):
        for t in tupl:
            # print(t)
            if get_manh_dist(t[0][0], coord) <= t[1]:
                
                gap = 0
                if coord[1] != 3719980:
                    count += 1
                break
        gap += 1
        coord[0] += 1
    print(count)
    print(coord)

def get_manh_dist(root,tst):
    dist = tst - root
    dist = [abs(dist[X]), abs(dist[Y])]
    return dist[X] + dist[Y]




def parse_input(data):
    tupl = []

    for d in data:
        s = d.split(":")
        a = s[SENS][s[SENS].find("x="):]
        b = s[BEAC][s[BEAC].find("x="):]
        a = a.split(",")
        b = b.split(",")
        npa = np.array([[int(a[SENS][a[SENS].find("=")+1:]),
                    int(a[BEAC][a[BEAC].find("=")+1:])], 
                    [int(b[SENS][b[SENS].find("=")+1:]),
                    int(b[BEAC][b[BEAC].find("=")+1:])]])
        mh = get_manh_dist(npa[0], npa[1])
        tupl.append([npa, mh])

    return tupl

# prt_grn("\nPart 1:")
aoc_day15()
