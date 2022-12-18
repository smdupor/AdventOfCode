from aocutils import *
from printed_parsing import *
import os
import numpy as np
from multiprocessing import Process

SENS = X = 0
BEAC = Y = 1

def aoc_day16():
    fp = open("input.txt","r")
    text = fp.read()
    fp.close() 
    data=text[:-1].split("\n")
   
   
   
   
   
   
   
   
def parse_input(data):
    tupl = []

    for d in data:
        pass
    return tupl
   
   
   
   
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
