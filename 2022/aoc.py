#!/usr/bin/python3

from aocutils import *
from printed_parsing import *

def aoc():
    fp = open("input","r")
    text = fp.read()
    fp.close()
    strings = parse_input(text[:-1])
    p1(strings)

def p1(strings):
    answer = ""

    prt_grn("Part 1: ")
    prt_red(answer)

def parse_input(data):
    out = []
    txt = data.split("\n")
    for line in txt:
        out.append(line)
    return out
aoc()
