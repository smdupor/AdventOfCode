from aocutils import *
from printed_parsing import *
def aoc_day11():
    fp = open("testinput.txt","r")
    text = fp.read()
    fp.close() 
    data=text[:-1].split("\n")

    data = load_lists(data)
    # test_loaded_data(data)
    passes = 0
    for i in range(0,len(data),2):
        if i > 1:
            break
        if comparator(data[i],data[i+1]):
            passes += 1
        
    prt_grn(passes)

def comparator(left, right):
    print(type(left))
    print(type(right))
    if type(left) == list and type(right) == list:
        yes = True
        if len(left) <= len(right):
            #STOP HERE
            pass
        # return comparator(left[])
    return True
    
    


# prt_grn("\nPart 1:")
aoc_day11()
