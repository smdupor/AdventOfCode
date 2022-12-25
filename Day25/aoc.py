from aocutils import *
from printed_parsing import *

def aoc_day25():
    fp = open("input.txt","r")
    text = fp.read()
    fp.close() 
    
    strings = parse_input(text[:-1])
    p1(strings)

def p1(strings):
    lookup = dict()
    lookup["="] = -2
    lookup["-"] = -1
    lookup["0"] = 0
    lookup["1"] = 1
    lookup["2"] = 2
    sum = 0
    for s in strings:
        add = from_snafu(s, lookup)
        sum += add
    prt_grn("Merry Christmas! Day 25 Part 1: ")
    prt_red(to_snafu(sum, lookup))

def from_snafu(string, lookup):
    value = 0
    for i,s in enumerate(string):
        value += 5**i * lookup[s]
    return value

def to_snafu(value, lookup):
    subtotal = 0
    i = 0

    # Grow subtotal until it overshadows total, to find the MostSigDig
    while(subtotal < value):
        subtotal += 2*(5**i)
        i += 1
    i -= 1

    rlookup = dict()
    rlookup[-2] = "="
    rlookup[-1] = "-"
    rlookup[0] = "0"
    rlookup[1] = "1"
    rlookup[2] = "2"

    # Assume each digit is maxed out at 2 x 5 ** digit
    digits_totaled = []
    digits_multiplier = []
    for subtotal in range(i,-1,-1):
        digits_totaled.append(2*(5**subtotal))
        digits_multiplier.append(2)
    
    ptr = 0
    digit = i
    qty = 0

    #Traverse the digit array
    while sum(digits_totaled) != value:

        # Removing one of this digit
        if sum(digits_totaled) > value:
            digits_totaled[ptr] -= 5**digit
            qty -= 1
            digits_multiplier[ptr] -= 1
        
        # And checking for overshoot. On overshoot, move on to next digit
        elif sum(digits_totaled) < value: 
            digits_totaled[ptr] += 5**digit
            qty = -1
            digit -= 1
            digits_multiplier[ptr] += 1
            ptr += 1
    
    # Turn back into a string
    string_version = ""
    for r in digits_multiplier:
        string_version += rlookup[r]
    return string_version

def parse_input(data):
    out = []
    txt = data.split("\n")
    for line in txt:

        list_version=[]
        for char in line:
            list_version.append(char)
        
        list_version.reverse()
        
        string_reversed_version = ""
        for char in list_version:
            string_reversed_version = string_reversed_version+char
        
        out.append(string_reversed_version)
    return out
aoc_day25()
