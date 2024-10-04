import time
def parse(input):
    f = open(input,"r")
    lines = f.readlines()
    return list(map(str.strip, lines))

def move(tile, dir, layout):
    if dir == 0: #right
        try:
            next_tile = (tile[0],tile[1]+1)
            next_tile_content = layout[next_tile[0]][next_tile[1]]
        except:
            return (0,0), -1
        if layout[next_tile[0]][next_tile[1]] == '.':
            next_dir = 0
            return next_tile, next_dir
        if layout[next_tile[0]][next_tile[1]] == '-':
            next_dir = 0
            return next_tile, next_dir
        if layout[next_tile[0]][next_tile[1]] == '\\':
            next_dir = 1
            return next_tile, next_dir
        if layout[next_tile[0]][next_tile[1]] == '/':
            next_dir = 3
            return next_tile, next_dir
        if layout[next_tile[0]][next_tile[1]] == '|':
            next_dir = [1,3]
            return next_tile, next_dir
        
    if dir == 1: #down
        try:
            next_tile = (tile[0]+1,tile[1])
            next_tile_content = layout[next_tile[0]][next_tile[1]]
        except:
            return (0,0), -1
        if layout[next_tile[0]][next_tile[1]] == '.':
            next_dir = 1
            return next_tile, next_dir
        if layout[next_tile[0]][next_tile[1]] == '-':
            next_dir = [0,2]
            return next_tile, next_dir
        if layout[next_tile[0]][next_tile[1]] == '\\':
            next_dir = 0
            return next_tile, next_dir
        if layout[next_tile[0]][next_tile[1]] == '/':
            next_dir = 2
            return next_tile, next_dir
        if layout[next_tile[0]][next_tile[1]] == '|':
            next_dir = 1
            return next_tile, next_dir
            
    if dir == 2: #left
        try:
            next_tile = (tile[0],tile[1]-1)
            next_tile_content = layout[next_tile[0]][next_tile[1]]
        except:
            return (0,0), -1
        if layout[next_tile[0]][next_tile[1]] == '.':
            next_dir = 2
            return next_tile, next_dir
        if layout[next_tile[0]][next_tile[1]] == '-':
            next_dir = 2
            return next_tile, next_dir
        if layout[next_tile[0]][next_tile[1]] == '\\':
            next_dir = 3
            return next_tile, next_dir
        if layout[next_tile[0]][next_tile[1]] == '/':
            next_dir = 1
            return next_tile, next_dir
        if layout[next_tile[0]][next_tile[1]] == '|':
            next_dir = [1,3]
            return next_tile, next_dir
        
    if dir == 3: #up
        try:
            next_tile = (tile[0]-1,tile[1])
            next_tile_content = layout[next_tile[0]][next_tile[1]]
        except:
            return (0,0), -1
        if layout[next_tile[0]][next_tile[1]] == '.':
            next_dir = 3
            return next_tile, next_dir
        if layout[next_tile[0]][next_tile[1]] == '-':
            next_dir = [0,2]
            return next_tile, next_dir
        if layout[next_tile[0]][next_tile[1]] == '\\':
            next_dir = 2
            return next_tile, next_dir
        if layout[next_tile[0]][next_tile[1]] == '/':
            next_dir = 0
            return next_tile, next_dir
        if layout[next_tile[0]][next_tile[1]] == '|':
            next_dir = 3
            return next_tile, next_dir

def beam(layout, beams, unique_beams):
    new_beams = []
    for i,beam in enumerate(beams):
        current_tile = beam[0]
        current_dir = beam[1]
        next_tile, next_dir = move(current_tile,current_dir,layout)
        beam_id = f'{next_tile}-{next_dir}'
        if next_dir == -1 or next_tile[0] < 0 or next_tile[1] < 0: #AKA the beam terminated
            print("Terminated a beam ...")
            print(next_dir)
        elif beam_id in unique_beams:
            #Do something!
            print("already in set")
            
        elif isinstance(next_dir,list):
            new_beams.append((next_tile,next_dir[0]))
            new_beams.append((next_tile,next_dir[1]))
        else:
            new_beams.append((next_tile,next_dir))

    print(new_beams)
    return new_beams
    
def try_tile(tile, dir, layout):
    activated_tiles = set()
    beams = [(tile,dir)]
    #activated_tiles.add(f"{tile[0]}X{tile[1]}")
    unique_beams = set()
    #unique_beams.add(f"{tile[0]}X{tile[1]}-{dir}")
    while len(beams) > 0:
        beams = beam(layout,beams,unique_beams)
        for new_beam in beams:
            new_beam_row = new_beam[0][0]
            new_beam_column = new_beam[0][1]
            activated_tiles.add(f'{new_beam_row}X{new_beam_column}')
            unique_beams.add(f'{new_beam[0]}-{new_beam[1]}')
    #print(len(activated_tiles))
    return len(activated_tiles)

def solve(input):
    activated_tiles = set()
    layout = parse(input)
    beams = [((0,0),1)]
    activated_tiles.add("0X0")
    unique_beams = set()
    unique_beams.add("(0, 0)-1")

    while len(beams) > 0:
        beams = beam(layout, beams, unique_beams)
        for new_beam in beams:
            new_beam_row = new_beam[0][0]
            new_beam_column = new_beam[0][1]
            activated_tiles.add(f'{new_beam_row}X{new_beam_column}')
            unique_beams.add(f'{new_beam[0]}-{new_beam[1]}')
    print(len(activated_tiles))


def solve2(input):
    layout = parse(input)
    max_energized = 0

    #Check columns downwards
    for i,row in enumerate(layout[0]):
        dir = 1
        max_energized = max(max_energized, try_tile((-1,i),dir,layout))

    #check columns upwards
    for i,row in enumerate(layout[-1]):
        dir = 3
        max_energized = max(max_energized, try_tile((0,i),dir,layout))

    #Check rows going right
    for i, row in enumerate(layout):
        dir = 1
        max_energized = max(max_energized, try_tile((i,-1),dir,layout))

    #Check rows going left
    for i, row in enumerate(layout):
        dir = 2
        max_energized = max(max_energized, try_tile((i,0),dir,layout))
    print(max_energized)

if __name__ == "__main__":
    solve2("input.txt")
    
    startTime = time.time()

#####your python script#####

    executionTime = (time.time() - startTime)
    print('Execution time in seconds: ' + str(executionTime))
