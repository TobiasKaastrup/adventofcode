import re
def parse(input):
    f = open(input,"r")
    lines = f.readlines()

    def strip_line(line):
        return line.strip()

    cleaned = list(map(strip_line,lines))
    return cleaned

def tilt_north(input):
    output = []
    num_of_cols = len(input[0])
    for column_i in range(num_of_cols):
        column_chars = ''
        for row in input:
            column_chars = column_chars + (row[column_i])
        column_list = column_chars.split("#")
        tilted_column_list = []
        for part in column_list:
            for i in range(part.count("O")):
                tilted_column_list.append("O")
            for i in range(part.count(".")):
                tilted_column_list.append(".")
            tilted_column_list.append("#")
        tilted_column_list.pop()
        output.append(tilted_column_list)
    
    result_lists = [[output[j][i] for j in range(len(output))] for i in range(len(output[0]))]
    result_joined = []
    for list in result_lists:
        result_joined.append("".join(list))

    return result_joined

def tilt_south(input):
    output = []
    num_of_cols = len(input[0])
    for column_i in range(num_of_cols):
        column_chars = ''
        for row in input:
            column_chars = column_chars + (row[column_i])
        column_list = column_chars.split("#")
        tilted_column_list = []
        for part in column_list:
            for i in range(part.count(".")):
                tilted_column_list.append(".")
            for i in range(part.count("O")):
                tilted_column_list.append("O")
            tilted_column_list.append("#")
        tilted_column_list.pop()
        output.append(tilted_column_list)
    
    result_lists = [[output[j][i] for j in range(len(output))] for i in range(len(output[0]))]
    result_joined = []
    for list in result_lists:
        result_joined.append("".join(list))

    return result_joined

def tilt_west(input):
    result = []
    for row in input:
        splitted = row.split("#")
        tilted_row = ""
        for part in splitted:
            for i in range(part.count("O")):
                tilted_row = tilted_row + "O"
            for i in range(part.count(".")):
                tilted_row = tilted_row + "."
            tilted_row = tilted_row + "#"
        tilted_row = tilted_row[:-1]
        result.append(tilted_row)
    return result

def tilt_east(input):
    result = []
    for row in input:
        splitted = row.split("#")
        tilted_row = ""
        for part in splitted:
            for i in range(part.count(".")):
                tilted_row = tilted_row + "."
            for i in range(part.count("O")):
                tilted_row = tilted_row + "O"
            tilted_row = tilted_row + "#"
        tilted_row = tilted_row[:-1]
        result.append(tilted_row)
    return result

def sum_weight(input):
    total = 0
    for i,line in enumerate(reversed(input)):
        for char in line:
            if char == "O":
                total += i+1
    return total

def do_cycle(input):
    north = tilt_north(input)
    west = tilt_west(north)
    south = tilt_south(west)
    east = tilt_east(south)

    #print(south == input)

    return east


def solve_1(input):
    parsed = parse(input)
    print(sum_weight(tilt_north(parsed)))

def solve_2(input):
    parsed = parse(input)
    current = parsed.copy()
    #print(tilt_east(parsed))

    intermediates = [current]

    for i in range(1000):
        cycled = do_cycle(intermediates[-1])
        print("---------")
        print(f'result after {i+1} cycles:\t{sum_weight(cycled)}')
        # for line in cycled:
        #     print(line)
        if cycled in intermediates:
            print(f"Iteration {i} gave a match")
            offset = intermediates.index(cycled)
            cycle_length = (i+1)-offset
            print(f'Cycle length: {cycle_length}')
            print(f'Offset: {offset}')
            print(f'Equivalent to billion iterations: {offset + (1000000000-offset)%cycle_length}')
            break
        current = cycled
        intermediates.append(cycled)


solve_2("input.txt")
