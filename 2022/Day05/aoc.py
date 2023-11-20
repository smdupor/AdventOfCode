from math import floor, ceil
from aocutils import *

############################################################ PART 1 ############################################
def part1():
    fp = open("input.txt","r")
    result = []
    i = int(0)
    j = int(0)

    lines = fp.readlines()
    val = []
    j=0
    for k in range(7,-1,-1):
        continue

    prt_red(str(i))

def part1_naive():
    # Open file
    fp = open("input.txt","r")

    # Load flatfile and init values matrix
    lines = fp.readlines()
    stacks = []
    
    # Read the initial stacks state, in reverse order, such that the matrix can grow downward
    j=0
    for k_reverse in range(7,-1,-1):
        # Allocate space and grab the next line to parse
        stacks.append([])
        line = lines[k_reverse]

        # Grab the values directly like a c-string.
        for m in range(1, 34, 4):
            stacks[j].append(line[m])
        j += 1
    
    # Read the operations one at a time, and do the actions within
    for k_reverse in range(10,len(lines)):
        # Read the operations and get number blocks to move, where from and to
        operation_values = lines[k_reverse].split(" ")
        qty = int(operation_values[1])
        from_col = int(operation_values[3]) - 1 # Subtract 1 so that indexing is zero-indexed
        to_col = int(operation_values[5]) - 1   # Subtract 1 so that indexing is zero-indexed
        
        # For number of blocks to be moved by this operation, do
        for n in range(0,qty):
            
            # Find the destination block in the regrettably still-vertical stacks
            to_row=0
            for m in range(len(stacks)-1,-1,-1):
                to_row = m
                if stacks[to_row][to_col] != " ":
                    to_row += 1
                    break
            
            # Find the source block in the regrettably still-vertical stacks
            from_row=0
            for m in range(len(stacks)-1,-1,-1):
                from_row = m
                if stacks[from_row][from_col] != " ":
                    break
            
            # If the matrix is full, grow it by a new empty row
            if to_row > len(stacks)-1 or stacks[to_row][to_col] != " ":
                stacks.append([" "," "," "," "," "," "," "," "," "])
                
            # Copy the block
            stacks[to_row][to_col] = stacks[from_row][from_col]

            # Zero the source (effectively, turning copy into move)
            stacks[from_row][from_col] = " "

    # Reverse the matrix to grow-upward so it looks like the examples          
    stacks.reverse()

    # Print the finished matrix in compact form
    for v in stacks:
        if v != [" "," "," "," "," "," "," "," "," "]: # Not printing the empty rows
            for u in v:
                print(u, end="")
            print(" ")

    # Print the items at the top of each stack (the submitted answer) in RED
    to_row=0
    for n in range(0,9):
        for m in range(0,len(stacks)):
            if stacks[m][n] != " ":
                prt_nocrlf_red(stacks[m][n])
                break

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

        
    # Reverse the matrix to grow-upward            
    val.reverse()

    # Print the finished matrix in compact form
    for v in val:
        
        if v != [" "," "," "," "," "," "," "," "," "]: # Not printing the empty rows
            for u in v:
                print(u, end="")
            print(" ")

    # Print the items at the top of each stack in RED
    to_row=0
    for n in range(0,9):
        for m in range(0,len(val)):
            if val[m][n] != " ":
                prt_nocrlf_red(val[m][n])
                break

prt_grn("\nPart 1:")
part1()
part1_naive()
prt_grn("\nPart 2:")
part2()
part2_naive()
print("")