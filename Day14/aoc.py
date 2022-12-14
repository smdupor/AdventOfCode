from aocutils import *
from printed_parsing import *
def aoc_day11():
    fp = open("input.txt","r")
    text = fp.read()
    fp.close() 
    data=text[:-1].split("\n")

    mtx = setup_mtx(200,200, ".")
    start_sand = [0,100]
    mtx[0][100] = "+"
    draw(data,mtx)

        
    prt_grn(passes)

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
                ilow = int(R[1])-450
                ihi = int(L[1])-450
            else:
                ilow = int(L[1])-450
                ihi = int(R[1])-450
            
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

# prt_grn("\nPart 1:")
aoc_day11()
