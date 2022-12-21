from aocutils import *
from printed_parsing import *
import os
import numpy as np
from multiprocessing import Process

SENS = X = 0
BEAC = Y = 1

def aoc_day16():
    fp = open("testinput.txt","r")
    text = fp.read()
    fp.close() 
    data=text[:-1].split("\n")
    [tupl,key] = parse_input(data)
    #part1(tupl,key)
    p1(tupl,key)
   
def p1(tupl,key):
    ptr = "AA"
    tick = 1
    max = -1
    sum = 0
    num_on = 0
    for key in tupl.keys():
        if tupl[key]["rate"] == 0:
            num_on += 1


    prt_red(recur(tupl, key, ptr, tick, sum, num_on))

def recur(tupl, key, ptr, tick, sum, num_on):
    max = -1

    if num_on == len(tupl.keys()):
        boost = 0
        for k in range(tick, 31):
            boost += sum
        return boost
    if tick > 30:
        return 0
    if tupl[ptr]["rate"] == 0:
       tupl[ptr]["status"] = True
       num_on += 1

    if tupl[ptr]["status"] == True:
        for k in tupl[ptr]["child"]:
            deep = sum + recur(tupl.copy(), key, k, tick+1, sum, num_on)
            if max < deep:
                max = deep
    else:
        tupl[ptr]["status"] = True
        tick += 1
        num_on += 1
        sum += tupl[ptr]["rate"]
        for k in tupl[ptr]["child"]:
            deep = sum + recur(tupl.copy(), key, k, tick+1, sum, num_on)
            if max < deep:
                max = deep
    if tick < 10:
        print (tick)
        print("\t " + str(max))
    return max



def part1(tupl,keys):
    ptr = "AA"
    flow = 0
    for i in range(1,31):
        prt_nocrlf_red(str(i)+": ")
        for key in keys:
            if tupl[key]["status"] == True:
                flow += tupl[key]["rate"]
        
        choice = max_choice(tupl, keys, ptr, 1, "")

        if choice[0] == ptr:
            tupl[ptr]["status"] = True
            prt_grn("Turn on valve " + ptr)
            continue
        elif len(ptr) >0:
            ptr = choice[0]
            prt_grn("Move to valve " + choice[0])
        

        
        # for key in tupl[ptr]["child"]:
        # #    print(key)
        # #    print(tupl[key]["rate"])
        #     if tupl[key]["rate"] > max and tupl[key]["status"] == False:
        #         maxkey = key
        #         max = tupl[key]["rate"]
        # prt_grn("Move to valve " + maxkey)
        # if len(maxkey) >0:
        #     ptr = maxkey
    prt_red(flow)


def max_choice(tupl, keys, ptr, divisor, last):
        max = -1
        maxkey = ""
        costs = dict()
        move = ""
        # for i in range(1,divisor):
        #     prt_nocrlf_red("   ")
        # prt_red("Examine valve " + ptr)
        if tupl[ptr]["status"] == False:
            costs[ptr] = tupl[ptr]["rate"] / divisor
            move = ptr
        else:
            costs[ptr] = 0

        if divisor > 5:
            # prt_grn("return 0")
            return [ptr, costs[ptr] if len(costs.items())> 0 else 0]        
        divisor += 1
        for key in tupl[ptr]["child"]:
            if key != last:
                [a,b] = max_choice(tupl, keys, key, divisor, ptr)
                if b > 0.1:
                    costs[key] = b
                    # costs[key] -= divisor        
        if len(costs.items())>0:
            for key in costs.keys():
                if max < costs[key]:
                    # print(key)
                    maxkey = key
                    max = costs[key]
            # prt_grn("return max")
            return [maxkey, max+costs[ptr]]
        else:
            return[ptr,costs[ptr]]

   
   
   
def parse_input(data):
    tupl = dict()
    di = dict()
    keys = []
    for i,d in enumerate(data):
        key = d.split(" ")[1]
        di[d.split(" ")[1]] = i
        rate = d[d.find("=")+1:d.find(";")]
        
        d = d[d.find(";")+1:]
        d = d[d.find("ve")+3:]
        grp = d.replace(" ","").split(",")
        tupl[key]=dict()

        tupl[key]["rate"] = int(rate)
        tupl[key]["child"] = grp
        tupl[key]["status"] = False
        keys.append(key)
    # print(keys)
    return [tupl,keys]
   
   
   
   
    # tupl = parse_input(data)

    # num_thr = 12
    # thr = []
    # block = (len(tupl) // num_thr) + 1
    # for i in range(0,num_thr):
    #     if i*block < len(tupl):
    #         t = Process(target=part2, args=(tupl,np.array([0,0]), 4000000, i*block, (i+1)*block))
    #         thr.append(t)
    #         t.start()
aoc_day16()
