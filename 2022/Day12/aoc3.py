from aocutils import *
from dijkstra import *
import threading
from multiprocessing import Process

def aoc_day12():
    [mtx, G,pq, maxrow, maxcol] = load_graph()
    load_edges(mtx, maxrow, maxcol)
    while(len(pq) > 0):
        blk = pq[0]
        pq = pq[1:]
        for e in blk.edges:
            if e.dist > blk.dist + 1:
                e.dist = blk.dist + 1
        pq.sort()
    print(G[find_by_value(G, "A")])
    
    thr = []
    for i in range(0,10):
        Gc = G.copy()
        pqc = pq.copy()
        mtxc = mtx.copy()
        t = Process(target=dij_thr, args=(Gc,pqc,mtxc,[i*4,(i*4+4)]))
        thr.append(t)
        t.start()



    prt_red(min)

def dij_thr(G, pq, mtx, rows):
    min = 2**32
    for i in range(rows[0],rows[1], 1):
        for j in range(131, -1, -1):
            g=mtx[i][j]
            if g.value == "a" or g.value == "S":
                g.dist = 0
                for n in G:
                    pq.append(n)
                pq.sort()
                
                print("\t" + str(i) + "," +str(j))

                while(len(pq) > 0):
                    blk = pq[0]
                    pq = pq[1:]
                    for e in blk.edges:
                        if e.dist > blk.dist + 1:
                            e.dist = blk.dist + 1
                    pq.sort()
                
                if G[find_by_value(G, "A")].dist < min:
                    min = G[find_by_value(G, "A")].dist
                    print(min, end = " uid: ")
                    prt_grn(g.uid)
    prt_red(min)

def reset_dist(G):
    for g in G:
        g.dist = 2**32

def load_edges(mtx, mx_r, mx_c):
#   print(mx_r)
 #   print(mx_c)
    for i, r in enumerate(mtx):
        for j, c in enumerate(r):
            # Up
  #          print(c.v)
            if i > 0 and is_edge(mtx[i-1][j], c):
                c.edges.append(mtx[i-1][j])
            # Dn
            if i < mx_r and is_edge(mtx[i+1][j], c):
                c.edges.append(mtx[i+1][j])
            # L
            if j > 0 and is_edge(mtx[i][j-1], c):
                c.edges.append(mtx[i][j-1])
            # Dn
            if j < mx_c and is_edge(mtx[i][j+1], c):
                c.edges.append(mtx[i][j+1])          
    return

def is_edge(v,u):
   # print(u.v, end = " - v")
#    # print(v.v, end = " :")
#     if u.v == v.v-1 or u.v >= v.v:
#         print("T")
#     else:
#          print("F")
    return u.v == v.v-1 or u.v >= v.v



def load_graph():
    fp = open("input.txt","r")
    text = fp.read()
    fp.close() 

    G = []
    mtx = []
    data = text[:-1].split("\n")

    for i,d in enumerate(data):
        mtx.append([])
        mult = len(d)
        for j,c in enumerate(d):
            if c == "E":
                c = "A"
            G.append(Node(i,j, (i*mult) + j, c))
            mtx[i].append(G[(i*mult) + j])
    pq = []
    for n in G:
        pq.append(n)
    pq[find_by_value(pq, "S")].dist = 0
    pq.sort()

    return [mtx,G, pq, i, j]

def ztest_print(G):
    row = G[0].row
    # for i,n in enumerate(G):
    #     if row != n.row:
    #         print("")
    #         row = n.row
    #     print(str(i) + n.value, end="")
    # print("")

    for i,n in enumerate(G):
        print(i,end=" ")
        print( n)
        


# prt_grn("\nPart 1:")
aoc_day12()
