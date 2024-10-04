import re
import heapq
from collections import deque
def parse(input):
    with open(input,"r") as f:
        data = f.readlines()

    return list(map(str.strip, data))

def get_module_type(module):
# 0: Broadcaster, 1: Flip-flop, 2: Conjunction
    
    module_types = {"b":0,"%":1,"&":2}
    return module_types.get(module[0])

def get_module_id(module):
    return re.findall(r"\w+",module)[0]

def get_module_destinations(module):
    return re.findall(r"\w+",module)[1:]


def flip(modules, id):
    modules[id][2] = not modules[id][2]

def send_pulse(input, id, modules, queue):
    lows = 0
    highs = 0
    #if button
    if id == "button":
        lows += 1
        queue.append("broadcaster")
        return highs,lows


    type = modules[id][0]
    destinations = modules[id][1]

    #if a broadcaster
    if type == 0:
        for destination in destinations:
            print(f"Broadcaster {input} -> {destination}")
            try:
                destination_type = modules[destination][0]
            except(KeyError):
                destination_type = -1
            if input == 0:
                lows += 1
                if destination_type == -1:
                    return -1,-1
                if destination_type == 1: #destination is a fliflop
                    flip(modules,destination)
                    queue.append(destination)

                if destination_type == 2: #destination is a conjunction
                    modules[destination][2][id] = 0
                    queue.append(destination)

            if input == 1:
                highs += 1
                if modules[destination][0] == 2: #destination is a conjunction
                    modules[destination][2][id] = 1
                    queue.append(destination)

        return highs,lows

    #if a Flip flop
    elif type == 1:
        if not modules[id][2]:
            for destination in destinations:
                print(f"{id} low -> {destination}")
                try:
                    destination_type = modules[destination][0]
                except(KeyError):
                    destination_type = -1
                lows += 1
                if destination_type == -1:
                    return -1,-1
                if destination_type == 1:#destination is a fliflop
                    flip(modules,destination)
                    queue.append(destination)
                elif destination_type == 2: #destination is a conjunction
                    modules[destination][2][id] = 0
                    queue.append(destination)
        else:
            for destination in destinations:
                print(f"{id} high -> {destination}")
                try:
                    destination_type = modules[destination][0]
                except(KeyError):
                    destination_type = -1
                highs += 1
                if destination_type == 2: #destination is a conjunction
                    modules[destination][2][id] = 1
                    queue.append(destination)

        return highs, lows

    #if a Conjunction
    elif type == 2:
        state = modules[id][2]
        all_high = True
        for pulse in state.values():
            if pulse == 0:
                all_high = False
        for destination in destinations:
            try:
                destination_type = modules[destination][0]
            except(KeyError):
                destination_type = -1
            if all_high:
                lows += 1
                if destination_type == -1:
                    return -1,-1
                print(f"{id} low -> {destination}")
                if destination_type == 1:#destination is a fliflop
                    flip(modules,destination)
                    queue.append(destination)
                elif destination_type == 2: #destination is a conjunction
                    modules[destination][2][id] = 0
                    queue.append(destination)
            else:
                highs +=1
                print(f"{id} high -> {destination}")
                if destination_type == 2: #destination is a conjunction
                    modules[destination][2][id] = 1
                    queue.append(destination)
        return highs,lows


    
def push_button(modules):
    highs = 0
    lows = 1
    queue = deque()

    
    send_pulse(0,"button",modules,queue)
    print("Button low -> broadcaster")

    while len(queue) > 0:
        next = queue.popleft()
        if next == "output" : continue
        #print(f"Activating {next}")
        added_highs, added_lows = send_pulse(0,next,modules,queue)

        highs += added_highs
        lows += added_lows
        x = 0

    return highs,lows


def find_all_inputs_for_conjunction(conj, lines):
    inputs = []
    for line in lines:
        if f"-> {conj}" in line:
            inputs.append(get_module_id(line))
    return inputs



#def get_module

def solve1(input):
    highs_sent = 0
    lows_sent = 0
    parsed = parse(input)
    modules = {"output": [3,[]]}
    


    for line in parsed:
        # valueindex: 0: type, 1: destinations, 2: state/memory
        if get_module_type(line) == 1:
            state = False
        elif get_module_type(line) == 2:
            state = {}
            for input in find_all_inputs_for_conjunction(get_module_id(line),parsed):
                state[input] = 0
        else:
            state = "broadcaster"
        modules[get_module_id(line)] = [get_module_type(line),get_module_destinations(line),state]

    for i in range(1000):
        highs, lows = push_button(modules)
        highs_sent += highs
        lows_sent += lows

    print(highs_sent*lows_sent)

        
def solve2(input):
    highs_sent = 0
    lows_sent = 0
    parsed = parse(input)
    modules = {"output": [3,[]]}
    


    for line in parsed:
        # valueindex: 0: type, 1: destinations, 2: state/memory
        if get_module_type(line) == 1:
            state = False
        elif get_module_type(line) == 2:
            state = {}
            for input in find_all_inputs_for_conjunction(get_module_id(line),parsed):
                state[input] = 0
        else:
            state = "broadcaster"
        modules[get_module_id(line)] = [get_module_type(line),get_module_destinations(line),state]

    i = 0
    while(True):
        i+=1
        highs, lows = push_button(modules)
        if highs == -1 and lows == -1:
            print(i)
            break
        highs_sent += highs
        lows_sent += lows

    print(highs_sent*lows_sent)



if __name__ == "__main__":
    solve2("input.txt")