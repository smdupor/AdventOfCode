#!/usr/bin/python3

from aocutils import *
from printed_parsing import *
import re

def aoc():
    fp = open("input","r")
    text = fp.read()
    fp.close()
    strings = parse_input(text[:-1])
    v,game = p1(strings)
    p2(v,game)

def p1(vec):
    answer = ""
    game = dict()
    for i,v in enumerate(vec):
        game[v[0]] = list()
        rounds = v[1].split(";")
        for r in rounds:
            round = r.replace(" ", "").replace("ed", "").replace("lue","").replace("reen","").split(",")
            game[v[0]].append(dict())
            for w in round:
                if w[-1] not in game[v[0]][-1]:
                    game[v[0]][-1][w[-1]] = 0
                game[v[0]][-1][w[-1]] = int(w[0:-1])
    rmax = 12
    gmax = 13
    bmax = 14
    p = dict()
    c = 0
    for v in vec:
        p[v[0]] = True
        for r in game[v[0]]:
            for k in r:
                if 'r' in k and r[k] > rmax: p[v[0]] = False
                if 'g' in k and r[k] > gmax: p[v[0]] = False
                if 'b' in k and r[k] > bmax: p[v[0]] = False
        if p[v[0]]:
            c += v[0]

    answer = str(c)
    prt_grn("Part 1: ")
    prt_red(answer)

    return vec,game

def p2(vec,game):
    c = 0
    for v in vec:
        rmax = 0
        gmax = 0
        bmax = 0
        for r in game[v[0]]:
            for k in r:
                if 'r' in k and r[k] > rmax: rmax = r[k]
                if 'g' in k and r[k] > gmax: gmax = r[k]
                if 'b' in k and r[k] > bmax: bmax = r[k]
        c += rmax * gmax * bmax

    answer = str(c)
    prt_grn("Part 2: ")
    prt_red(answer)

def parse_input(data):
    out = []
    txt = data.split("\n")
    for line in txt:
        vec = line.split(":")
        vec[0] = int(vec[0][5:])
        out.append(vec)
    return out
aoc()
