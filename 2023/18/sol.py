def parse(input):
    f = open(input,"r")
    lines = f.readlines()
    return list(map(str.strip,lines))

def get_polygon_area(dirs, values):
    x = 0
    y = 0
    x_list = [0]
    y_list = [0]
    trenches_outside = 0
    going_up = True
    going_left = True
    outside = False
    for i, dir in enumerate(dirs):
        if dir == "R":
            if not going_up:
                outside = not outside
            x += int(values[i])
            going_left = False
        if dir == "U":
            if going_left:
                outside = not outside
            y += int(values[i])
            going_up = True
        if dir == "D":
            if not going_left:
                outside = not outside
            y -= int(values[i])
            going_up = False
        if dir == "L":
            if going_up:
                outside = not outside
            x -= int(values[i])
            going_left = True
        if outside:
            trenches_outside += int(values[i])
        y_list.append(y)
        x_list.append(x)
    left = 0
    right = 0
    for i in range(len(x_list)-1):
        left += (x_list[i] * y_list[i+1])
        right += (y_list[i] * x_list[i+1])
    inside = abs(right-left)/2
    outside = trenches_outside+1
    return inside+outside

def solve1(input):
    plan = parse(input)
    dirs = []
    values = []

    for order in plan:
        dir,value,color = order.split(" ")
        dirs.append(dir)
        values.append(value)

    print(f"Part 1 answer: {int(get_polygon_area(dirs,values))}")

def solve2(input):
    plan = parse(input)
    directions = ["R","D","L","U"]
    dirs = []
    values = []
    for order in plan:
        hexa = order.split("#")[1]
        dir_int = int(hexa[-2])
        values.append(int(hexa[:-2],16))
        dirs.append(directions[dir_int])

    print(f"Part 2 answer: {int(get_polygon_area(dirs,values))}")


if __name__ == "__main__":
    solve1("input.txt")
    solve2("input.txt")