from sympy import symbols, Eq, solve


def parse(input):
    with open(input,"r") as f:
        lines = f.readlines()
    return list(map(str.strip,lines))

def line_to_dict(line):
    p, v = line.split("@")
    px,py,pz = p.split(",")
    vx, vy, vz = v.split(",")
    h_dict = {
        "px":int(px),
        "py":int(py),
        "pz":int(pz),
        "vx":int(vx),
        "vy":int(vy),
        "vz":int(vz),
    }
    return h_dict

def future_hailstone(h):
    h["px"] += h["vx"]
    h["py"] += h["vy"]
    h["pz"] += h["vz"]
    return h

def crosses_test_area(h,start,end):
    crosses = False
    while not crosses:
        h = future_hailstone(h)
        if start <= h["px"] <= end and start <= h["py"] <= end and start:
            crosses = True
        if h["py"] == 0:
            break

    return crosses

def get_intersection(a,b):
    a_eq = get_equation(a)
    b_eq = get_equation(b)
    x, y = symbols('x y')

    intersection_point = solve((a_eq,b_eq),(x,y))

    return intersection_point

def intersect_in_future(a,b):
    x, y = symbols('x y')
    intersection = get_intersection(a,b)
    if not intersection:
        return False
    a_negative_dir_x = a["vx"] < 0
    b_negative_dir_x = b["vx"] < 0
    if a_negative_dir_x and b_negative_dir_x:
        return intersection[x] < a["px"] and intersection[x] < b["px"]
    elif a_negative_dir_x and not b_negative_dir_x:
        return intersection[x] < a["px"] and intersection[x] > b["px"]
    elif not a_negative_dir_x and b_negative_dir_x:
        return intersection[x] > a["px"] and intersection[x] > b["px"]
    else:
        return intersection[x] > a["px"] and intersection[x] > b["px"]
        
def intersection_in_test_area(intersection, start, end):
    if not intersection:
        return False
    x, y = symbols('x y')
    return start <= intersection[x] <= end and start <= intersection[y] <= end

def get_equation(h):
    m = h["vy"]/h["vx"]
    #print(m)
    x, y = symbols('x y')
    equation = Eq(y - h["py"], m*(x - h["px"]))

    return equation

def solve1(input, start, end):
    total = 0
    checked = 0
    lines = parse(input)
    hail_stones = list(map(line_to_dict,lines))



    for i in range(0,len(hail_stones)-1):
        for j in range(i+1,len(hail_stones)):
            checked += 1
            print(checked)
            #print(get_intersection(hail_stones[i],hail_stones[j]))
            #print(intersect_in_future(hail_stones[i],hail_stones[j]))
            if intersect_in_future(hail_stones[i],hail_stones[j]):
                intersection = get_intersection(hail_stones[i],hail_stones[j])
                #print(intersection)
                if intersection_in_test_area(intersection,start,end):
                    total += 1
    print(total)


if __name__ == "__main__":
    solve1("input.txt",200000000000000,400000000000000)