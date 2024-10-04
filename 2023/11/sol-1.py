import re
def parse(input):
    f = open(input,'r')
    parsed = f.readlines()

    def strip_line(line):
        return line.strip()

    cleaned = list(map(strip_line,parsed))
    return cleaned

def expand(space):
    expanded_rows = []
    #add rows
    for row in space:
        expanded_rows.append(row)
        if '#' not in row:
            expanded_rows.append(row)
    #check columns
    columns_to_duplicate = []
    for i in range(len(space[0])):
        column = []
        for row in expanded_rows:
            column.append(row[i])
        if '#' not in column:
            columns_to_duplicate.append(i)
    columns_to_duplicate.reverse()
    #add columns
    expanded_rows_cols = []
    #for column in columns_to_duplicate:
    for row in expanded_rows:
        #print(row)
        splitted = list(row)
        for col in columns_to_duplicate:
            splitted.insert(col,".")
        expanded_rows_cols.append(''.join(splitted))
        #print(".".join(splitted))

    return expanded_rows_cols

def expand_v2(space):
    expansion_rows = []
    #add rows
    print('Starting expansion vertically ...')
    for i, row in enumerate(space):
        if '#' not in row:
            expansion_rows.append(i)
    #check columns
    #print("Checking which columns to duplicate ...")
    expansion_columns = []
    for i in range(len(space[0])):
        column = []
        for row in space:
            column.append(row[i])
        if '#' not in column:
            expansion_columns.append(i)

    return expansion_rows, expansion_columns

def find_galaxies(space):
    galaxies = []
    for i, row in enumerate(space):
        for j,char in enumerate(row):
            if char == "#":
                galaxies.append((i,j))
    return galaxies

def get_pairs(galaxies):
    pairs = []
    stop = len(galaxies)
    for i,g in enumerate(galaxies):
        for j in range(i+1,stop):
            pairs.append((g,galaxies[j]))
    return pairs

def get_distance(pair):
    ver = abs(pair[0][0] - pair[1][0])
    hor = abs(pair[0][1] - pair[1][1])
    return ver + hor

def get_distance_v2(pair,ex_rows, ex_cols):
    distance = 0

    r1 = pair[0][0]
    r2 = pair[1][0]
    c1 = pair[0][1]
    c2 = pair[1][1]

    for i in range(min(r1,r2),max(r1,r2)):
        if i in ex_rows:
            distance += 1000000
        else:
            distance += 1

    for i in range(min(c1,c2),max(c1,c2)):
        if i in ex_cols:
            distance += 1000000
        else:
            distance += 1
    
    return distance

def sum_distances(pairs):
    total = 0
    for pair in pairs:
        total += get_distance(pair)
    return total

def sum_distances_v2(pairs,ex_rows,ex_cols):
    total = 0
    for pair in pairs:
        total += get_distance_v2(pair, ex_rows,ex_cols)
    return total

def solve_1(input):
    expanded = expand(parse(input))
    galaxy_coords = find_galaxies(expanded)
    pairs = get_pairs(galaxy_coords)
    print(sum_distances(pairs))

def solve_2(input):
    galaxy_coords = find_galaxies(parse(input))
    ex_rows, ex_cols = expand_v2(parse(input))
    #print(ex_rows)
    #print(ex_cols)

    pairs = get_pairs(galaxy_coords)
    print(sum_distances_v2(pairs,ex_rows,ex_cols))

    #print(expanded)
    #galaxy_coords = find_galaxies(expanded)
    #pairs = get_pairs(galaxy_coords)
    #print(sum_distances(pairs))

solve_2("input.txt")

