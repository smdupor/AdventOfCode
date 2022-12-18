from aocutils import *
from printed_parsing import *
import os
import numpy as np
from multiprocessing import Process

SENS = X = 0
BEAC = Y = 1

def aoc_day15():
    fp = open("input.txt","r")
    text = fp.read()
    fp.close() 
    data=text[:-1].split("\n")
    tupl = parse_input(data)
    # for t in tupl:
    #     print(t)
    # print(get_manh_dist(tupl[0][0][0], tupl[0][0][1]))
    # print(tupl[0])
    
    
    # part2(tupl, np.array([0,0]), 4000000)
    num_thr = 12
    thr = []
    block = (len(tupl) // num_thr) + 1
    # print(block)
    # print(len(tupl))
    # exit()
    for i in range(0,num_thr):
        if i*block < len(tupl):
            t = Process(target=part2, args=(tupl,np.array([0,0]), 4000000, i*block, (i+1)*block))
            thr.append(t)
            t.start()

def part2(tupl, coord, dist, start, end):
    ring = []
    # mtx = setup_mtx(75 ,150,".")
  
    count_lo = 1
    count = len(tupl)
    for z in range(start, end):
        t = tupl[z]
        c = t[0][0].copy()
        c[0] -= (t[1]+1)
        # print(c)
        # print(t)
        prt_grn("testing tuple " + str(z) + " out of " + str(end))
        count_lo += 1
        while c[0] < t[0][0][0]:
            
            # ring.append(c.copy())
            #print(get_manh_dist(c,t[0][0]))
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
            # ring.append(c.copy())
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
            # ring.append(c.copy())
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
            # ring.append(c.copy())
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

    prt_red(ring)
    


    # for r in ring:
    #     if r[0] > 0 and r[1] > 0:
    #         test = True
    #         for t in tupl:
    #             mtx[t[0][0][1]+40][t[0][0][0]+40]="o"
    #             if get_manh_dist(r,t[0][0]) < t[1]:
    #                 test=False
    #         if test:
    #             prt_red(r)
    #             exit()
                    
    #    # print(ring)
    #     # mtx = setup_mtx(150,150,".")
    #     for r in ring:
    #         mtx[r[1]+40][r[0]+40] = "x"
    #     mtx[t[0][0][1]+40][t[0][0][0]+40]="o"
    #     for m in mtx:
    #         for n in m:
    #             print(n, end="")
    #         print("")
    #     exit()
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
