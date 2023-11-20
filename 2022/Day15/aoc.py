from aocutils import *
from printed_parsing import *
import os
import numpy as np
from multiprocessing import Process
from multiprocessing import Condition
SENS = X = 0
BEAC = Y = 1

def aoc_day15():
    fp = open("input.txt","r")
    text = fp.read()
    fp.close() 
    data=text[:-1].split("\n")
    tupl = parse_input(data)

    num_thr = 12
    thr = []
    block = (len(tupl) // num_thr) + 1
    killall = Condition();
    killall.acquire()
    for i in range(0,num_thr):
        if i*block < len(tupl):
            t = Process(target=part2, args=(tupl,np.array([0,0]), 4000000, i*block, (i+1)*block, killall))
            thr.append(t)
            t.start()

def part2(tupl, coord, dist, start, end, killall):
    ring = []
    count_lo = 1
    for z in range(start, end):
        t = tupl[z]
        c = t[0][0].copy()
        c[0] -= (t[1]+1)
        prt_grn("testing tuple " + str(z) + " out of " + str(end))
        count_lo += 1
        while c[0] < t[0][0][0]:
            if  0<=c[0] <= dist and 0<= c[1] <= dist:
                test = True
                for tau in tupl:
                    if get_manh_dist(c,tau[0][0]) < tau[1]:
                        test = False
                        break
                if test == True:
                    ring.append(c.copy())
            c[0] += 1
            c[1] += 1
        while c[1] >= t[0][0][1]:
            if  0<=c[0] <= dist and 0<= c[1] <= dist:
                test = True
                for tau in tupl:
                    if get_manh_dist(c,tau[0][0]) < tau[1]:
                        test = False
                        break
                if test == True:
                    ring.append(c.copy())
            c[0] += 1
            c[1] -= 1
        while c[0] > t[0][0][0]:
            if  0<=c[0] <= dist and 0<= c[1] <= dist:
                test = True
                for tau in tupl:
                    if get_manh_dist(c,tau[0][0]) < tau[1]:
                        test = False
                        break
                if test == True:
                    ring.append(c.copy())
            c[0] -= 1
            c[1] -= 1
        while c[1] < t[0][0][1]:
            if  0<=c[0] <= dist and 0<= c[1] <= dist:
                test = True
                for tau in tupl:
                    if get_manh_dist(c,tau[0][0]) < tau[1]:
                        test = False
                        break
                if test == True:
                    ring.append(c.copy())            
            c[0] -= 1
            c[1] += 1
        
    if len(ring) > 0:
        prt_red("Tuning Frequency: " + str((ring[0][0]*4000000) + ring[1][1]))
        exit()

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
    dist = np.array(tst) - np.array(root)
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
