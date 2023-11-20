from aocutils import *

def aoc_day11():
    fp = open("test_input.txt","r")
    text = fp.read()
    fp.close() 
    data = text.split("\n\n")

    monkeys = test2()

    for i in range(0,20):
        print("Round: " + str(i))
        for m in monkeys:
            m.process(monkeys)
    
    max = [0,0]
    for m in monkeys:
        if m.inspections > max[0]:
            max[1] = max[0]
            max[0] = m.inspections
        elif m.inspections > max[1]:
            max[1] = m.inspections
    print(max)
    prt_red(max[0] * max[1])

    monkeys = test2()

    for i in range(0,10000):
        print("Round: " + str(i))
        for m in monkeys:
            m.process_p2(monkeys)
    
    max = [0,0]
    for m in monkeys:
        if m.inspections > max[0]:
            max[1] = max[0]
            max[0] = m.inspections
        elif m.inspections > max[1]:
            max[1] = m.inspections
    print(max)
    prt_red(max[0] * max[1])



def setup_monkeys(data):
    monkeys = []
    for d in data:
        lines = d.split("\n")
        items = []
        for i in lines[1].split(":")[1].strip(" ").split(","):
            items.append(int(i))
        
        opcode = lines[2].split(" ")[-2]
        print(opcode)
        targ = lines[2].split(" ")[-1]
        print(targ)
        if opcode == "*":
            if targ == "old":
                op = lambda i : i * i
            else:
                targ = int(targ)
                op = lambda i : i * targ
        elif opcode == "+":
            if targ == "old":
                op = lambda i : i + i
            else:
                targ = int(targ)
                op = lambda i : i + targ
        testdiv = int(lines[3].split(" ")[-1])
        test = lambda i : i % testdiv == 0
        tru = int(lines[4].split(" ")[-1])
        fls = int(lines[5].split(" ")[-1])
        monkeys.append(Monkey(items, op, test, tru, fls))
    return monkeys

def test():
    monkeys = []
    monkeys.append(Monkey([79,98], lambda i : i*19, lambda i : (i % 96577) % 23 == 0, 2, 3, 23)) 
    monkeys.append(Monkey([54, 65, 75, 74], lambda i : i + 6, lambda i : (i % 96577) % 19 == 0, 2, 0, 19))
    monkeys.append(Monkey([79, 60, 97], lambda i : i*i, lambda i : (i % 96577) % 13 == 0, 1, 3, 13))  
    monkeys.append(Monkey([74], lambda i : i + 3, lambda i : (i % 96577) % 17 == 0, 0, 1, 17) ) 
    return monkeys

def test2():
    monkeys = []
    monkeys.append(Monkey([74, 64, 74, 63, 53],             lambda i : i*7, lambda i : i % 5 == 0, 1, 6)) 
    monkeys.append(Monkey([69, 99, 95, 62],                 lambda i : i * i, lambda i : i % 17 == 0, 2, 5))  
    monkeys.append(Monkey([59, 81],                         lambda i : i + 8, lambda i : i % 7 == 0, 4, 3))  
    monkeys.append(Monkey([50, 67, 63, 57, 63, 83, 97],     lambda i : i + 4, lambda i : i % 13 == 0, 0, 7))  
    monkeys.append(Monkey([61, 94, 85, 52, 81, 90, 94, 70], lambda i : i + 3, lambda i : i % 19 == 0, 7, 3))  
    monkeys.append(Monkey([69],                             lambda i : i + 5, lambda i : i % 3 == 0, 4, 2))  
    monkeys.append(Monkey([54, 55, 58],                     lambda i : i + 7, lambda i : i % 11 == 0, 1, 5))  
    monkeys.append(Monkey([79, 51, 83, 88, 93, 76],         lambda i : i * 3, lambda i : i % 2 == 0, 0, 6))  

    return monkeys

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
