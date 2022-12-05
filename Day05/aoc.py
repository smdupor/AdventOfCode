from math import floor, ceil
from aocutils import *

############################################################ PART 1 ############################################
def part1():
    fp = open("input.txt","r")
    i = int(0)
    subval = 0

    for st in fp:
        continue

    prt_red(str(i))

def part1_naive():


    fp = open("input.txt","r")
    result = []
    i = int(0)
    j = int(0)

    t = [0,0,0,0]
    lines = fp.readlines()
    val = []
    j=0
    for k in range(7,-1,-1):
        val.append([])
        line = lines[k]
        for m in range(1, 34,4):
            # print(line[m] + str(k) + str(m))
            val[j].append(line[m])
        j += 1
    #val.reverse()

    # print(val)

    for k in range(10,len(lines)):
        values = lines[k].split(" ")
        qty = int(values[1])
        frm = int(values[3])-1
        to = int(values[5])-1
        # print(lines[k])
        # for x in val:
        #     for y in x:
        #         print(y, end="")
        #     print(" ")
        # print(qty)
        # print(frm)
        # print(to)
        sw = 0
        for n in range(0,qty):
            j=0
            for m in range(len(val)-1,-1,-1):
                j=m
                if val[m][to] != " ":
                    j += 1
                    break
            # print("j = " + str(j))
            t=0
            for m in range(len(val)-1,-1,-1):
                t=m
                if val[m][frm] != " ":
                    break
           # print("t = " + str(t))
            switch = 0
            
            if j > len(val)-1 or val[j][to] != " ":
                val.append([" "," "," "," "," "," "," "," "," "])
                

            val[j][to] = val[t][frm]
            val[t][frm] = " "
            
            
            # if sw >10:
            #     return
        #     for x in val:
        #         for y in x:
        #             print(y, end="")
        #         print(" ")
        # sw += 1
        # for x in val:
        #     for y in x:
        #         print(y, end="")
        #     print(" ")
            

            
            
        
    val.reverse()
    for v in val:
        for u in v:
            print(u, end="")
        print(" ")

    prt_red(str(i))


############################################################ PART 2 ############################################

def part2():
    fp = open("input.txt","r")
    i = int(0)
    
    inp = fp.readlines()
    numstr = len(inp)
    
    for t in range(0,numstr//3):
        continue

    prt_red(str(i))

def part2_naive():
    fp = open("input.txt","r")
    result = []
    i = int(0)
    j = int(0)

    t = [0,0,0,0]
    lines = fp.readlines()
    val = []
    j=0
    for k in range(7,-1,-1):
        val.append([])
        line = lines[k]
        for m in range(1, 34,4):
            # print(line[m] + str(k) + str(m))
            val[j].append(line[m])
        j += 1
    #val.reverse()

    # print(val)

    for k in range(10,len(lines)):
        values = lines[k].split(" ")
        qty = int(values[1])
        frm = int(values[3])-1
        to = int(values[5])-1
        # print(lines[k])
        # for x in val:
        #     for y in x:
        #         print(y, end="")
        #     print(" ")
        # print(qty)
        # print(frm)
        # print(to)
        sw = 0
        for n in range(qty,0,-1):
            j=0
            for m in range(len(val)-1,-1,-1):
                j=m
                if val[m][to] != " ":
                    j += 1
                    break
            # print("j = " + str(j))
            t=0
            for m in range(len(val)-1,-1,-1):
                t=m
                if val[m][frm] != " ":
                    t -= (n-1)
                    break
           # print("t = " + str(t))
            switch = 0
            
            if j > len(val)-1 or val[j][to] != " ":
                val.append([" "," "," "," "," "," "," "," "," "])
                

            val[j][to] = val[t][frm]
            val[t][frm] = " "
            
            
            # if sw >10:
            #     return
            # for x in val:
            #     for y in x:
            #         print(y, end="")
            #     print(" ")
        # sw += 1
        # for x in val:
        #     for y in x:
        #         print(y, end="")
        #     print(" ")
        
    val.reverse()
    for v in val:
        for u in v:
            print(u, end="")
        print(" ")
    prt_red(str(i))

prt_grn("\nPart 1:")
part1()
part1_naive()
prt_grn("\nPart 2:")
part2()
part2_naive()
print("")