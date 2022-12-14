from aocutils import *
from printed_parsing import *
def aoc_day11():
    fp = open("input.txt","r")
    text = fp.read()
    fp.close() 
    data=text[:-1].split("\n")

    mtx = setup_mtx(175,175, ".")
    start_sand = [0,25]
    mtx[0][25] = "+"
    mtx = draw(data,mtx)
    mtx = drop_sand(start_sand,mtx)
    for m in mtx:
        for n in m:
            print(n,end="")
        print("")
    prt_grn(passes)

def drop_sand(entry,mtx):
    count = 0
    while(True):
        count += 1
        coord = entry
        while(mtx[coord[0]+1][coord[1]] == "."):
            coord[0] += 1
            if coord[0] == 175:
                return mtx
        if mtx[coord[0]+1][coord[1]] == "#":
            mtx[coord[0]+1][coord[1]] = "O"
        elif mtx[coord[0]+1][coord[1]] == "O":
            if mtx[coord[0]+1][coord[1]-1] == ".":
                mtx[coord[0]+1][coord[1]-1] = "O"
            elif mtx[coord[0]+1][coord[1]+1] == ".":
                mtx[coord[0]+1][coord[1]+1] = "O"
            elif mtx[coord[0]+1][coord[1]-2] == ".":
                mtx[coord[0]+1][coord[1]-2] = "O"
            elif mtx[coord[0]+1][coord[1]+2] == ".":
                mtx[coord[0]+1][coord[1]+2] = "O"
        
        if count == 50:
            return mtx
            


def draw(data,mtx):
    imin = 1000
    imax = 0
    jmin = 1000
    jmax = 0
    for d in data:
        tuples = d.replace(" ","").split("->")
        for i in range(0, len(tuples)-1,2):
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
                ilow = int(R[1])-475
                ihi = int(L[1])-475
            else:
                ilow = int(L[1])-475
                ihi = int(R[1])-475
            
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

    return mtx

# prt_grn("\nPart 1:")
aoc_day11()
