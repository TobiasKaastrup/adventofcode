import re
f = open("8-input.txt", "r")
data = f.read()

instructions = data.split('\n\n')[0]
map_lines = data.split('\n\n')[1].split('\n')

def find_positions(line):
    return line.split(" =")[0]

map_positions = list(map(find_positions,map_lines))


def find_start_indices(search_list, search_item):
    indices = []
    for i, value in enumerate(search_list):
        if re.match(search_item, value):
            indices.append(i)
    return indices

start_indexes = find_start_indices(map_positions, r"\w\wA")

def find_lines_from_indixes(index):
    return map_lines[index]

start_lines = list(map(find_lines_from_indixes, start_indexes))




def move_to_next_positions(lines, direction):

    new_positions = []
    for line in lines:
        left = re.search(r'\w+,', line).group().replace(",","")
        right = re.search(r' \w+', line).group().strip()

        if direction == "L":
            new_positions.append(map_lines[map_positions.index(left)])
        else:
            new_positions.append(map_lines[map_positions.index(right)])
    return new_positions

def check_if_all_lines_end_z(lines):
    for line in lines:
        if line[2:3] != "Z":
            return False
    return True

def check_instructions(start_lines):
    count_1000 = 0
    steps = 0
    end_found = False
    current_lines = start_lines
    while(not end_found):
        for instruction in instructions:
            steps += 1
            current_lines = move_to_next_positions(current_lines, instruction)
            if steps%1000 == 0:
                print(f"{count_1000*1000} position sets checked")
                count_1000 += 1
            if check_if_all_lines_end_z(current_lines):
                print("Found the end!")
                end_found = True
                return steps

#print(start_lines)

#testlines= ["TTZ = (CBF, GXB)","GRZ = (NJG, MPZ)"]

#print(check_if_all_lines_end_z(testlines))

print(check_instructions(start_lines))