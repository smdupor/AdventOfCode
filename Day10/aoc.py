from aocutils import *

def aoc_day10():
    fp = open("input.txt","r")
    text = fp.read()
    fp.close() 
    data = text.split("\n")
    data = data[:-1]

    reg0 = 1
    cycles = 1
    crt_monitor = setup_mtx(6,40," ")         
    
    signal_samples = dict()
    sampling_period = 20

    # PREFETCH
    a = data[0].split(" ")
    stall = 1 if a[0] == "noop" else 2
    data = data[1:]

    # One cycle per iteration
    while True:
        # EXECUTE
        [signal_samples, sampling_period] = sample_signal_level(cycles, signal_samples, sampling_period, reg0)
        crt_monitor = draw(reg0,crt_monitor,cycles)
        cycles += 1
        stall -= 1
        
        # Normal retire + Fetch Next PC
        if stall == 0 and len(data) > 0:
            # RETIRE
            if a[0] == "addx":
                reg0 += int(a[1]) #Commit / Retire
            
            # FETCH
            a = data[0].split(" ")
            stall = 1 if a[0] == "noop" else 2
            data = data[1:]
        
        # Instruction trace is ending, retire if necessary and exit
        elif stall == 0:
            # RETIRE
            if a[0] == "addx":
                reg0 += int(a[1]) #Commit / Retire
            break
        
    # Part 1
    total = sum(signal_samples.values())
    prt_red(total)

    # Part 2
    prt_grn("Part 2:")
    for i in range(0,6):
        for j in range(0,40):
            print(crt_monitor[i][j], end="")
        print(" ")

def draw(r, crt, cycles):
    row = (cycles-1) // 40
    col = (cycles-1) % 40
    if col == r - 1 or col == r or col == r+1:
        crt[row][col] = "#"
    else:
        crt[row][col] = "."
    return crt

def sample_signal_level(cycles, signal,target,r):
    if cycles == target:
        signal[cycles] = (cycles * r)
        target += 40
    return [signal, target]

prt_grn("\nPart 1:")
aoc_day10()
