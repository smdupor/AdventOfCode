from aocutils import *

def aoc_day11():
    fp = open("test_input.txt","r")
    text = fp.read()
    fp.close() 
    

class Monkey:
    items = []
    def __init__(self, items, operation, boolean, t, f, div = 1):
        self.items = items
        self.op = operation
        self.test = boolean
        self.t = t
        self.f = f
        self.inspections = 0
        self.divisor = div

    def process(self, monkeys):
        for item in self.items:
            self.inspections += 1
            temp = self.op(item)
            temp //= 3
            if self.test(temp):
                monkeys[self.t].items.append(temp)
            else:
                monkeys[self.f].items.append(temp)
        self.items = []

    def process_p2(self, monkeys):
        for item in self.items:
            self.inspections += 1
            temp = self.op(item)
            temp %= 9699690
            if self.test(temp):
                monkeys[self.t].items.append(temp)
            else:
                monkeys[self.f].items.append(temp)
        self.items = []
                

    def __str__(self):
        val = "(" + str(self.inspections) +") Mnk: "
        for i in self.items:
            val += str(i) + ", "
        
        return val


    

prt_grn("\nPart 1:")
aoc_day11()
