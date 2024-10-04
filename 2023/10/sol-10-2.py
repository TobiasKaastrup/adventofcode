f = open("10-input.txt","r")
data = f.read()

lines = data.split()

s = (0,0)

for i, line in enumerate(lines):
    if "S" in line:
        s = (i,line.index("S"))

def get_tile_froom_coords(tile):
    tile_dir = lines[tile[0]][tile[1]]
    return tile_dir

def go_to_next_tile(tile,dir):
    r = tile[0]
    c = tile[1]

    if dir == 0: # UP
        ntc = (r-1,c)
        ntv = get_tile_froom_coords(ntc)
        if ntv == "|":
            return ntc,0
        if ntv == "F":
            return ntc,1
        if ntv == "7":
            return ntc,3
        if ntv == "S":
            return ("end","end"),"end"
        else:
            return -1, -1

    if dir == 1: # RIGHT
        ntc = (r,c+1)
        ntv = get_tile_froom_coords(ntc)
        if ntv == "-":
            return ntc,1
        if ntv == "7":
            return ntc,2
        if ntv == "J":
            return ntc,0
        if ntv == "S":
            return ("end","end"),"end"
        else:
            return -1, -1

    if dir == 2: # DOWM
        ntc = (r+1,c)
        ntv = get_tile_froom_coords(ntc)
        if ntv == "|":
            return ntc,2
        if ntv == "L":
            return ntc,1
        if ntv == "J":
            return ntc,3
        if ntv == "S":
            return ("end","end"),"end"
        else:
            return -1, -1

    if dir == 3: # LEFT
        ntc = (r,c-1)
        ntv = get_tile_froom_coords(ntc)
        if ntv == "-":
            return (r,c-1),3
        if ntv == "F":
            return (r,c-1),2
        if ntv == "L":
            return (r,c-1),0
        if ntv == "S":
            return ("end","end"),"end"
        else:
            return -1, -1
        

def find_loop(tile):
    #Check each direction
    # directions: 0 (up), 1 (right), 2 (down), 3 (left)
    for dir in range(4):
        loop_length = 0
        loop_coords = []
        next_dir = dir
        next_tile = tile
        while next_tile != -1 and next_dir != "end":
            loop_coords.append(next_tile)
            #print("Checking new next")
            loop_length += 1
            next_tile, next_dir = go_to_next_tile(next_tile,next_dir)
        if next_tile == -1:
            print("that was not the loop!")
        if next_tile == ("end","end"):
                print("Loop detected!")
                return loop_coords
                #get_result(loop_length)



loop_coords = find_loop(s)

lines_as_coords = []
for i, line in enumerate(lines):
    line_of_coords = []
    for j in range(len(line)):
        line_of_coords.append((i,j))
    lines_as_coords.append(line_of_coords)

total = 0

for line in lines_as_coords:
    inside = False
    last_loop_tile_index = 9999999999
    for tile in line:
        if tile in loop_coords:
            loop_tile_index = loop_coords.index(tile)
            #print(last_loop_tile_index)
            if get_tile_froom_coords(tile) not in ['-','L','J']:
                inside = not(inside)
            last_loop_tile_index = loop_tile_index
            continue
        if inside:
            total += 1

print(total)
#print(len(loop_coords))

#print(lines_as_coords[-1])