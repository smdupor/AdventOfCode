from aocutils import *
from printed_parsing import *
import os

def aoc_day11():
    fp = open("input.txt","r")
    text = fp.read()
    fp.close() 
    data=text[:-1].split("\n")

    mtx = setup_mtx(175,1000, ".")
    start_sand = [0,500]
    mtx[0][500] = "+"
    mtx = draw(data,mtx)
    [qty,mtx] = drop_sand(start_sand,mtx)
    for m in mtx:
        for n in m:
            print(n,end="")
        print("")
    prt_red(qty-1)

    data=text[:-1].split("\n")

    mtx = setup_mtx(175,1000, ".") 
    start_sand = [0,500]
    mtx[0][500] = "+"
    mtx = draw(data,mtx)
    [qty,mtx] = drop_sand(start_sand,mtx)
    for m in mtx:
        for n in m:
            print(n,end="")
        print("")
    prt_red(qty-1)

def prt_mtx(mtx):
    os.system("clear")
    for m in mtx:
        for n in m:
            print(n,end="")
        print("")

def get_adj_list(mtx, r, c):
    l = []
    ind = []
    for i in range(-1,2,1):
        l.append(mtx[r+1][c+i])
        if mtx[r+1][c+i] == ".":
            ind.append(True)
        else:
            ind.append(False)
    return [l,ind]


def drop_sand(entry,mtx):
    count = 0
    while(True):
        count += 1
        coord = entry.copy()
        while True:
            # prt_mtx(mtx)
            #coord[0] += 1
            if coord[0] == 174:
                print(count)
                return [count,mtx]
            [l,ind] = get_adj_list(mtx, coord[0], coord[1])
            # print(ind)
            if ind.count(True) == 0:
                mtx[coord[0]][coord[1]] = "O"
                # prt_mtx(mtx) if count % 100 == 0 else 1+1

                if coord == entry:
                    prt_red(count)
                    return [count,mtx]
                # print("lol")
                break
            
            if ind[1]:
                coord[0] += 1
            elif ind[0]:
                coord[0] += 1
                coord[1] -= 1
            elif ind[2]:
                coord[0] += 1
                coord[1] += 1          
    return [count,mtx]

def draw(data,mtx):
    imin = 1000
    imax = 0
    jmin = 1000
    jmax = 0
    for d in data:
        tuples = d.replace(" ","").split("->")
        for i in range(0, len(tuples)-1):
            l = tuples[i]
            r = tuples[i+1]
            L=str(l).split(",")
            R=str(r).split(",")
            L.reverse()
            R.reverse()
            if int(L[0]) >= int(R[0]):
                jlow = int(R[0])
                jhi = int(L[0])
            else:
                jlow = int(L[0])
                jhi = int(R[0])
            if int(L[1]) >= int(R[1]):
                ilow = int(R[1])-0
                ihi = int(L[1])-0
            else:
                ilow = int(L[1])-0
                ihi = int(R[1])-0
            
            if ilow < imin:
                imin=ilow
            if ihi > imax:
                imax = ihi
            if jlow < jmin:
                jmin = jlow
            if jhi > jmax:
                jmax = jhi
                

            for j in range(jlow, jhi+1):
                for i in range(ilow, ihi+1):
                    print(i)
                    print(j)
                    mtx[j][i] = "#"
    for m in mtx:
        for n in m:
            print(n,end="")
        print("")
    print(imin)
    print(imax)
    print(jmin)
    print(jmax)
    for k in range(0, len(mtx[jmax])):
        mtx[jmax+2][k] = "#"
    # prt_mtx(mtx)
    # exit()
    return mtx

# prt_grn("\nPart 1:")
aoc_day11()
