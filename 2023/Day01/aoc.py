#!/usr/bin/python3

from aocutils import *
from printed_parsing import *
import re

def aoc():
    fp = open("debug","r")
    text = fp.read()
    fp.close()
    strings = parse_input(text[:-1])
    # p1(strings)
    p2(strings)

def p1(strings):

    result = 0
    for s in strings:
        vals = re.findall("[0-9]", s)
        temp = "" + str(vals[0])+str(vals[-1])
        result += int(temp)

    answer = str(result)

    prt_grn("Part 1: ")
    prt_red(answer)

CONV = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "1":1,
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9
}

def p2(strings):

    result = 0
    for s in strings:
        vals = re.findall("[0-9]|one|two|three|four|five|six|seven|eight|nine", s)
        print(vals)
        for k in vals: print(str(CONV[k])+"  ", end="")
        print("")
        temp = "" + str(CONV[vals[0]])+str(CONV[vals[-1]])
        print(temp)
        result += int(temp)

    answer = str(result)

    prt_grn("Part 2: ")
    prt_red(answer)

def parse_input(data):
    out = []
    txt = data.split("\n")
    for line in txt:
        out.append(line)
    return out
aoc()
