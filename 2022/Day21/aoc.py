from aocutils import *
from printed_parsing import *
import os
import numpy as np
from multiprocessing import Process

def aoc_day21():
    fp = open("input.txt","r")
    text = fp.read()
    fp.close() 
    vec = parse_input(text[:-1].split("\n"))
    p1(vec)
    p2(vec)

def p1(vec):
    prt_nocrlf_red("Part 1: The root value is:  ")
    prt_red(recur(vec,"root"))

def p2(vec):
    
    a = recur(vec, vec["root"][0])
    b = recur(vec, vec["root"][1])
    diff=a-b
    shift = 10000000000
    
    while int(diff) != 0:

        # Search forward until we pass the answer
        while diff > 0:
            vec["humn"] = vec["humn"] + shift
            a = recur(vec, vec["root"][0])
            diff = a-b
        
        # Reduce the size of the search block by half
        shift //= 2

        # Search backward until we pass the answer
        while diff < 0:
            vec["humn"] = vec["humn"] - shift
            a = recur(vec, vec["root"][0])
            diff = a-b

    prt_grn("Part 2: The value for human is:")
    prt_grn(vec["humn"])

def recur(vec, key):
    if type(vec[key]) == int:
        return vec[key]
    elif vec[key][2] == "+":
        return recur(vec, vec[key][0]) + recur(vec, vec[key][1])
    elif vec[key][2] == "-":
        return recur(vec, vec[key][0]) - recur(vec, vec[key][1])
    elif vec[key][2] == "/":
        return recur(vec, vec[key][0]) / recur(vec, vec[key][1])
    elif vec[key][2] == "*":
        return recur(vec, vec[key][0]) * recur(vec, vec[key][1])

def parse_input(data):
    out = dict()
    for d in data:
        # print(d)
        t = d.split(":")
        key = t[0]
        val = t[1].replace(" ", "")
        if len(val) == 9:
            val = [val[0:4], val [5:], val [4]]
            # print(val)
        else:
            val = int(val)
        out[key] = val
    return out
aoc_day21()
