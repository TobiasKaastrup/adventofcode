import re
from collections import deque
def parse(input):
    with open(input,"r") as f:
        lines = f.readlines()
    return list(map(str.strip,lines))

def make_one_directional_dict(connections):
    con_1d = {}
    for c in connections:
        nodes = re.findall("\w+",c)
        for n in nodes:
            if n not in con_1d.keys():
                con_1d[n] = []
        for i in range(1,len(nodes)):
            con_1d[nodes[0]].append(nodes[i])
            con_1d[nodes[i]].append(nodes[0])

    return con_1d

def list_wires(connections):
    wires = []
    for c in connections:
        nodes = re.findall("\w+",c)
        for i in range(1,len(nodes)):
            wires.append(f"{nodes[0]}/{nodes[i]}")
    return wires

def is_divided_in_two(con_1d):
    divided = False
    left = set()
    all = set()

    q = deque()
    checked = set()

    for k,v in con_1d.items():
        contents = set(v)
        contents.add(k)

        #Add the very first elem to left
        if len(left) == 0:
            left.add(k)
            for x in v:
                q.append(x)
                #checked.add(x)
        
        for c in contents:
            all.add(c)
    
    while len(q) > 0:
        x = q.popleft()
        checked.add(x)

        for k, v in con_1d.items():
            if x in v:
                left.add(k)
                if k not in checked:
                    q.append(k)

    return not len(left) == len(all)
    
def get_combinations(w):
    combinations = []
    num_of_nodes = len(w)
    list_of_nodes = list(w)
    for i in range(1,num_of_nodes):
        for j in range(i+1,num_of_nodes):
            for k in range(j+1,num_of_nodes):
                #print(f"{list_of_nodes[i]} - {list_of_nodes[j]} - {list_of_nodes[k]} ") 
                combinations.append([list_of_nodes[i],list_of_nodes[j],list_of_nodes[k]])
    return combinations

def try_removing_combination(con_1d, combination):
    connections = con_1d.copy()
    for c in combination:
        a,b = c.split("/")
        if b in connections[a]:
            connections[a].remove(b)
        if a in connections[b]:
            connections[b].remove(a)
    #print(connections)
    print(combination)
    print(is_divided_in_two(connections))
        

def solve1(input):
    connections = parse(input)
    con_1d = make_one_directional_dict(connections)
    wires = list_wires(connections)
    combinations = get_combinations(wires)


    print(con_1d)
    print("\n")
    #print(combinations[0])
    #print(is_divided_in_two(con_1d))

    for comb in combinations:
        try_removing_combination(con_1d,comb)


if __name__ == "__main__":
    solve1("test.txt")