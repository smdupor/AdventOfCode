class Node:
    def __init__(self,row, col, uid, value):
        self.dist = 2**32
        self.parent = -1
        self.row = row
        self.col = col
        self.value = value
        self.v = ord(value)
        if self.v < 91:
            self.v += 58
        self.uid = uid
        self.edges = []

    def __lt__(self,other):
        return self.dist < other.dist

    def __str__(self) -> str:
        stval = str(self.value) + " At r: " + str(self.row) + ", c: " 
        stval += str(self.col) + " uid: " + str(self.uid)+ " dist: " + str(self.dist)
        stval += " Out_Deg: " + str(len(self.edges))
        return stval

def find_by_value(li, value):
    for i, x in enumerate(li):
        if x.value == value:
            return i
    return -1

def test_nodes():
    nodes = []
    nodes.append(Node(1,2,3, "a"))
    nodes.append(Node(4,5,6, "b"))
    nodes.append(Node(7,8,9, "E"))
    nodes.append(Node(10,12,13, "s"))
    nodes[0].dist = 82
    nodes[1].dist = 12
    nodes[2].dist = 0

    print(str(find_by_value(nodes,"E")))
    
    nodes.sort()
    for node in nodes:
        print(node)
    
    print(str(find_by_value(nodes,"E")))

