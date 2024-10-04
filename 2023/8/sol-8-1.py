import re
f = open("8-input.txt", "r")
data = f.read()

instructions = data.split('\n\n')[0]
map_lines = data.split('\n\n')[1].split('\n')

def find_positions(line):
    return line.split(" =")[0]

map_positions = list(map(find_positions,map_lines))

start_index = map_positions.index("AAA")

def move_to_next_pos(line, direction):
    left = re.search(r'\w+,', line).group().replace(",","")
    right = re.search(r' \w+', line).group().strip()

    if direction == "L":
        return map_lines[map_positions.index(left)]
    else:
        return map_lines[map_positions.index(right)]

def check_instructions(start):
    steps = 0
    end_found = False

    current_line = start
    while(not end_found):
        for instruction in instructions:
            steps += 1
            current_line = move_to_next_pos(current_line, instruction)
            if current_line[0:3] == "ZZZ":
                print("Found the end!")
                end_found = True
                return steps


#print(move_to_next_pos(test_position,"r"))
print(check_instructions(map_lines[start_index]))