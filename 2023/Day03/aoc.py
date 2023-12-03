#!/usr/bin/python3

from aocutils import *
from printed_parsing import *
import re

def aoc():
    fp = open("input","r")
    text = fp.read()
    fp.close()
    strings,asdf = parse_input(text[:-1])
    t = p1(strings,asdf)
    # p2(strings, t)

def p1(asdf,strings):
    answer = ""
    total = 0
    total2 = 0
    va=[]
    vb=[]
    for s in asdf:
        num = int(re.findall('[0-9]+', s)[0])
        # print(re.sub("[0-9]|\.", '', s))
        if len(re.sub("[0-9]|\.", '', s.replace("\n", "").replace(" ", "")))>0:
            # print(num)
            total += num
            va.append(num)

    starlist = dict()
    for i, l in enumerate(strings):
        for j, coord in enumerate(l[1]):
            result = False
            if coord[0]-1 >=0:
                coord[0] -= 1
            if coord[1]+1 < len(l[0]):
                coord[1] += 1
            # print(coord)
            sk=[0,0]
            for k in range(coord[0], coord[1]):
                # print(str(k) + " " + strings[i-1][0][k])
                # print(str(k) + " " + strings[i+1][0][k]) if i < len(strings) -1 else None
                if  not re.match("\d|\.", strings[i][0][k]):
                    result=True
                    if  strings[i][0][k] == "*":
                        sk=[i,k]
                if i>0 and not re.match("\d|\.", strings[i-1][0][k]):
                    result=True
                    if  strings[i-1][0][k] == "*":
                        sk=[i-1,k]
                if i < len(strings)-1 and not re.match("\d|\.", strings[i+1][0][k]):
                    # print("match")
                    result=True
                    if  strings[i+1][0][k] == "*":
                        sk=[i+1,k]

            if result:
                if sk != [0,0]:
                    if (sk[0], sk[1]) not in starlist:
                        starlist[sk[0], sk[1]] = [1, l[2][j]]
                    else:
                        starlist[sk[0], sk[1]] = [starlist[sk[0], sk[1]][0] + 1, starlist[sk[0], sk[1]][1] * l[2][j]]
            

                # print(l[2][j])
                # if l[2][j] == 318:
                #     prt_red(l[2][j])
                # else:
                #     print(l[2][j])
                total2 += l[2][j]
                vb.append(l[2][j])

    prt_grn("Part 1: ")
    prt_red(total)
    prt_grn(total2)
    # print(starlist)
    total3 = 0
    for star in starlist:
        if starlist[star][0] == 2:
            total3 += starlist[star][1]
    prt_red(total3)
    # for i, k in enumerate(vb):
    #     print( f"{va[i]}-{vb[i]} ")

def p2(vec, s):
    answer = ""

    prt_grn("Part 2: ")
    prt_red(answer)

def parse_input(data):
    out = []
    out2 = []
    txt = data.split("\n")
    # txt = txt[:-1]
    for j,line in enumerate(txt):
        txt[j] = "." + txt[j] + "."
    txt.append("    ")
    for j,line in enumerate(txt):
        # print(line)
        out.append([])
        out[-1].append(line)
        out[-1].append([])
        out[-1].append([])
        out[-1].append([])
        dig = False
        coord = [0,0]
        for i, k in enumerate(line):
            if re.match('\d', k) and not dig:
                dig = True
                coord[0] = i
            elif (not re.match('\d', k) or i == len(line)-1 )and dig:
                dig = False
                coord[1] = i if  i != len(line) else len(line)-1
                out[-1][1].append(coord.copy())
                out[-1][2].append(int(line[coord[0]:coord[1]]))
                coord[0] -= 1 if coord[0] != 0 else 0
                if coord[1]+1 < len(line):
                    tmp = txt[j-1][coord[0] : coord[1]+1]  + "\n" + txt[j][coord[0]:coord[1]+1] + "\n"
                    # tmp += txt[j][coord[1]+1]
                    if j < len(txt):
                        tmp += txt[j+1][coord[0] : coord[1]+1]
                else:
                    tmp = txt[j-1][coord[0] : coord[1]] + "\n" +txt[j][coord[0] : coord[1]] + "\n"
                    # tmp += txt[j][coord[1]]+"\n"
                    if j < len(txt):
                        tmp += txt[j+1][coord[0] : coord[1]]
                print(tmp + "\n")
                out2.append(tmp)



    return out2,out
aoc()
