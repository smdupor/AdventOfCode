def test_loaded_data(data):
    count = 0
    for d in data:
        print(str(d).replace(" ", ""))
        count += 1
        if count == 2:
            count = 0
            print("")

def load_lists(dat):
    data = []
    for d in dat:
        if len(d)>2:
            data.append(d)
    out = []
    # print(data[0])
    stmp = ""
    vec = []
    count = 1
    for d in data:
        
        [tmp,vec] = load_line(d[1:],0)
        # temp = [vec]
        # [tmp,vec] = load_line(tmp,0)
        # temp.append(vec)
        out.append(vec)
        count += 1
        if count == 5:
            out.append([])
        # if len(out) >0:
        #     break

        # print(out[0])

    # for o in out:
    #     print(o)
    return out

def load_line(d,level):
    vec = []
    subs = ""
            
    level += 1
    while(True):
        # print(d)
        # print(level)    
        if d[0] == "[":
            #vec = []
            d = d[1:]
            [d,temp] = load_line(d, level)
            vec.append(temp)
        elif d[0] == "]":
            # print(d[0])
            d = d[1:]
            if len(subs) > 0:
                vec.append(int(subs))
            # print(vec)
            return [d,vec]
        elif d[0] == ",":
            if(len(subs)>0):
                vec.append(int(subs))
            subs = ""
            d = d[1:]
            if level == 0:
                return [d,vec]
        else:
            subs += d[0]
            d = d[1:]
    if len(subs) > 0:
        vec.append(subs)
    #print(vec)
    return [d,vec]