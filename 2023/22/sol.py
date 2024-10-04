from collections import deque
def parse(input):
    with open(input,"r") as f:
        lines = f.readlines()
    return list(map(str.strip, lines))

def sort_by_z(bricks):
    def find_low_z(b):
        return int(b.split("~")[0].split(",")[-1])
    bricks.sort(key=find_low_z)

def get_coords(brick):
    start, end  = brick.split("~")
    x0,y0,z0 = list(map(int,start.split(",")))
    x1,y1,z1 = list(map(int,end.split(",")))

    return x0,y0,z0,x1,y1,z1

def get_all_coords(brick):
    area = set()
    x0,y0,z0,x1,y1,z1 = get_coords(brick)

    for x in range(x0,x1+1):
        for y in range(y0,y1+1):
            for z in range(z0,z1+1):
                area.add(f'{x},{y},{z}')
    return area

def let_fall(bricks):
    occupied_cords = set()
    for i,brick in enumerate(bricks):
        x0,y0,z0,x1,y1,z1 = get_coords(brick)
        for j in range(z0,1,-1):
            if i == 0:
                z0 -= 1
                z1 -= 1
            else:
                coords_by_moving = get_all_coords(f"{x0},{y0},{z0-1}~{x1},{y1},{z1-1}")
                if coords_by_moving.isdisjoint(occupied_cords):
                    z0 -= 1
                    z1 -= 1
                else:
                    break
            bricks[i] = f"{x0},{y0},{z0}~{x1},{y1},{z1}"
        for coord in get_all_coords(bricks[i]):
            occupied_cords.add(coord)

def get_supporters_for_all(bricks):
    supporters_dict = {}
    rev_bricks = list(reversed(bricks))
    for brick in rev_bricks:
        supporters = set()
        x0,y0,z0,x1,y1,z1 = get_coords(brick)
        coords_below = get_all_coords(f"{x0},{y0},{z0-1}~{x1},{y1},{z1-1}")
        for j in range(1,len(rev_bricks)):
            if not coords_below.isdisjoint(get_all_coords(rev_bricks[j])):
                supporters.add(rev_bricks[j])
        if len(supporters) > 0:
            supporters_dict[brick] = supporters
        else:
            supporters_dict[brick] = set([-1])
    return supporters_dict

def get_supporting(bricks):
    supporting_dict = {}
    rev_bricks = list(reversed(bricks))
    for brick in rev_bricks:
        supporting = []
        x0,y0,z0,x1,y1,z1 = get_coords(brick)
        coords_above = get_all_coords(f"{x0},{y0},{z0+1}~{x1},{y1},{z1+1}")
        for j in range(1,len(rev_bricks)):
            if not coords_above.isdisjoint(get_all_coords(rev_bricks[j])):
                supporting.append(rev_bricks[j])
        supporting_dict[brick] = supporting
    return supporting_dict

def find_lone_supporters(bricks):
    lone_supporters = set()
    falling_bricks = {}
    reversed_bricks = list(reversed(bricks))
    for i,brick in enumerate(reversed_bricks):
        supporters = []
        x0,y0,z0,x1,y1,z1 = get_coords(brick)
        coords_below = get_all_coords(f"{x0},{y0},{z0-1}~{x1},{y1},{z1-1}")
        for j in range(i+1,len(reversed_bricks)):
            if not coords_below.isdisjoint(get_all_coords(reversed_bricks[j])):
                supporters.append(reversed_bricks[j])
        if len(supporters) == 1:
            print(f"{i} only has one supporter ({supporters[0]}) which cannot be disintegrated")
            lone_supporters.add(supporters[0])
    return lone_supporters


def solve1(input):
    bricks = parse(input)
    sort_by_z(bricks)
    #print(bricks)
    let_fall(bricks)
    #print(bricks)
    sort_by_z(bricks)
    lone_supporters = find_lone_supporters(bricks)

    print(f"Solution 1: {len(bricks)-len(lone_supporters)} can be safely disintegrated")
    


def solve2(input):
    sum = 0
    bricks = parse(input)
    sort_by_z(bricks)
    let_fall(bricks)
    sort_by_z(bricks)
    supporters = get_supporters_for_all(bricks)
    lone_supporters = find_lone_supporters(bricks)
    ls_list = list(lone_supporters)
    sort_by_z(ls_list)
    #print(lone_supporters)
    for ls in ls_list:
        print(ls)

    # f2 = open("fallenbricks.txt","w")
    # for line in bricks:
    #     f2.write(line+"\n")
    # f2.close()
    for s in ls_list:
        bricks_falling = []

        #print(f"Now checking {s}")
        falling = set([s])
        sup_copy = supporters.copy()
        for brick in bricks:
            if sup_copy[brick].issubset(falling) and brick != s:
                falling.add(brick)
                bricks_falling.append(brick)
                #print("This one is also falling")
        print(f'{s} caused {len(bricks_falling)} to fall:')
        for bf in bricks_falling:
            print('\t'+bf)
        sum += len(falling) -1

    print(f"Part 2: Sum of falling bricks is {sum}")
    

def solve2_rec(input):
    bricks = parse(input)
    sort_by_z(bricks)
    let_fall(bricks)
    sort_by_z(bricks)
    supporters = get_supporters_for_all(bricks)
    
    print(get_supporting(bricks))


if __name__ == "__main__":
    #solve1("input.txt")
    solve2("input.txt")
    #solve2_rec("test.txt")