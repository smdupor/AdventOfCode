dbg_enable = False

def prt_grn(input):
    # colors = dict()
    # colors ['HEADER'] = '\033[95m',
    # 'OKBLUE' = '\033[94m',
    # 'OKCYAN' = '\033[96m',
    # 'OKGREEN' = '\033[92m',
    # 'WARNING' = '\033[93m',
    # 'FAIL' = '\033[91m',
    # 'ENDC' = '\033[0m',
    # 'BOLD' = '\033[1m',
    # 'UNDERLINE' = '\033[4m']

    print('\033[92m' + input + '\033[0m')

def prt_red(input):
    # colors = dict()
    # colors ['HEADER'] = '\033[95m',
    # 'OKBLUE' = '\033[94m',
    # 'OKCYAN' = '\033[96m',
    # 'OKGREEN' = '\033[92m',
    # 'WARNING' = '\033[93m',
    # 'FAIL' = '\033[91m',
    # 'ENDC' = '\033[0m',
    # 'BOLD' = '\033[1m',
    # 'UNDERLINE' = '\033[4m']

    print('\033[91m' + input + '\033[0m')

def prt_nocrlf_red(input):
    # colors = dict()
    # colors ['HEADER'] = '\033[95m',
    # 'OKBLUE' = '\033[94m',
    # 'OKCYAN' = '\033[96m',
    # 'OKGREEN' = '\033[92m',
    # 'WARNING' = '\033[93m',
    # 'FAIL' = '\033[91m',
    # 'ENDC' = '\033[0m',
    # 'BOLD' = '\033[1m',
    # 'UNDERLINE' = '\033[4m']

    print('\033[91m' + input + '\033[0m', end="")

def char_to_val(ch):
    offset_lowcase = 0
    offset_upcase = 26

    j = ord(ch)
    if(j > 96):
        return (j-96) + offset_lowcase
    else:
        return (j-64) + offset_upcase

def p(st):
    if(dbg_enable):
        print(st)