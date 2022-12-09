from aocutils import *

# Define constants
NECK = ROW = NECKPTR = 0
TAIL = COL = 1
TAILPTR = 8

def is_direct_adjacent(h,t):
    if h == t:
        return True
    if (h[ROW] == t[ROW] and (t[COL] == h[COL] - 1 or t[COL] == h[COL]+1)) or (h[COL] == t[COL] and (t[ROW] == h[ROW]-1 or t[ROW] == h[ROW] + 1)):
        return True
    return False

def is_diagonal_adjacent(h,t):
    if (t[ROW] == h[ROW] - 1 or t[ROW] == h[ROW] + 1) and (t[COL] == h[COL]-1 or t[COL] == h[COL] + 1):
        return True
    return False

def move_hptr(dir, hptr):
    if dir == "U":
        hptr[ROW] += 1
    elif dir == "D":
        hptr[ROW] -= 1
    elif dir == "L":
        hptr[COL] -= 1
    elif dir == "R":
        hptr[COL] += 1
    return hptr

def move_tptr(h,t):
    if not (is_direct_adjacent(h,t) or is_diagonal_adjacent(h,t)):
        diff = [0,0]
        diff[ROW] = h[ROW] - t[ROW]
        diff[COL] = h[COL] - t[COL]

        # Left or right move
        if diff[ROW] == 0:
            t[COL] = t[COL] - 1 if diff[COL] < 0 else t[COL] + 1 
        # Up or Down Move
        elif diff[COL] == 0:
            t[ROW] = t[ROW] - 1  if diff[ROW] < 0 else  t[ROW] + 1 
        # Diagonal Dn/Rt
        elif diff[ROW] > 0 and diff[COL] > 0:
            t[ROW] += 1
            t[COL] += 1
        # Diagonal Up/Rt
        elif diff[ROW] < 0 and diff[COL] > 0:
            t[ROW] -= 1
            t[COL] += 1
        # Diagonal Dn/Lft
        elif diff[ROW] > 0 and diff[COL] < 0:
            t[ROW] += 1
            t[COL] -= 1
        # Diagonal Up/Lft
        elif diff[ROW] < 0 and diff[COL] < 0:
            t[0] -= 1
            t[COL] -= 1
    return t

def aoc_day_09():
    fp = open("input.txt","r")
    text = fp.read()
    data = text.split("\n")
    data = data[:-1]
    
    #Init Breadcrumb matrices
    tail_breadcrumbs = [[],[]]
    for j in range(0,1000):
        tail_breadcrumbs[NECK].append([])
        tail_breadcrumbs[TAIL].append([])
        for i in range(0,1000):
            tail_breadcrumbs[NECK][j].append(0)
            tail_breadcrumbs[TAIL][j].append(0)
    
    # Init head/neck/tail pointers
    hptr = [500,500]
    tptr_list = []
    for n in range(0,9):
        tptr_list.append([500,500])

    # And mark their location in the breadcrumb map
    tail_breadcrumbs[NECK][tptr_list[NECKPTR][ROW]][tptr_list[NECKPTR][COL]] = 1
    tail_breadcrumbs[TAIL][tptr_list[TAILPTR][ROW]][tptr_list[TAILPTR][COL]] = 1
    
    # Traverse the flatfile
    for d in data:
        directions = d.split(" ")
        distance = int(directions[1])

        while(distance > 0):
            #  Move the head pointer
            hptr = move_hptr(directions[0],hptr)
            distance -=1

            # Move the first tail pointer
            tptr_list[NECK] = move_tptr(hptr,tptr_list[NECKPTR])

            # Move the rest of the tail pointers
            for n in range(1,9):
                tptr_list[n] = move_tptr(tptr_list[n-1], tptr_list[n])
            
            # Update the breadcrumbs map
            tail_breadcrumbs[NECK][tptr_list[NECKPTR][ROW]][tptr_list[NECKPTR][COL]] = 1
            tail_breadcrumbs[TAIL][tptr_list[TAILPTR][ROW]][tptr_list[TAILPTR][COL]] = 1
    
    prt_grn("PART 1:")
    
    visited_qty = 0
    for tptr_list in tail_breadcrumbs[NECK]:
        for t in tptr_list:
            visited_qty += t
    
    prt_red(visited_qty)


    prt_grn("PART 2:")

    visited_qty = 0
    for tptr_list in tail_breadcrumbs[TAIL]:
        for t in tptr_list:
            visited_qty += t
    
    prt_red(visited_qty)

    fp.close()  

aoc_day_09()
