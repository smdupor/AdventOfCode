from aocutils import *
from printed_parsing import *
def aoc_day11():
    fp = open("input.txt","r")
    text = fp.read()
    fp.close() 
    data=text[:-1].split("\n")

    data = load_lists(data)
    #test_loaded_data(data)


    
    


# prt_grn("\nPart 1:")
aoc_day11()
