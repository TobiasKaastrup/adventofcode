from collections import deque
def parse(input):
    with open(input,"r") as f:
        lines = f.readlines()
    return list(map(str.strip,lines))

def check_directions(tile, trail, visited):
    possibilities = []
    
    for dir in range(0,4):
        if dir == 0: #up
            next = (tile[0]-1,tile[1])
        elif dir == 1: #right
            next = (tile[0],tile[1]+1)
        elif dir == 2: #down
            next = (tile[0]+1,tile[1])
        elif dir == 3: #left
            next = (tile[0],tile[1]-1)

        if next not in visited and trail[next[0]][next[1]] != "#":
            possibilities.append(next)
    return possibilities


def get_start_and_end(trail):
    final_row = len(trail) -1
    for i,t in enumerate(trail[0]):
        if t == ".":
            s = (0,i)
            break
    for i,t in enumerate(trail[-1]):
        if t == ".":
            e = (final_row,i)
            break
    return s,e

def check_route(route, trail,e):
    other_routes = []
    total = 0
    tile = route[0]
    total = route[1]
    visited = route[2].copy()
    reached_the_end = True

    while tile != e:
        print(f"Checking directions: {tile}")
        pd = check_directions(tile,trail,visited)
        if len(pd) == 0:
            reached_the_end = False
            break
        tile = pd[0]
        
        total += 1
        for i in range(1,len(pd)):
            other_visited = visited.copy()
            other_visited.add(pd[i])
            other_routes.append([pd[i],total,other_visited])
        visited.add(tile)
    return total, other_routes, reached_the_end

def solve2(input):
    trail = parse(input)
    s,e = get_start_and_end(trail)
    print(s,e)
    longest_route = 0
    

    q = deque([[s,0,set([s])]])

    while len(q)>0:
        next = q.popleft()
        print(f"Starting check route: {next[0]} steps: {next[1]}")
        total, other_routes, reached_the_end = check_route(next, trail,e)
        print(f"Finished checking {next[0]}, route was {total} steps long ")
        if reached_the_end:
            longest_route = max(longest_route,total)
        for r in other_routes:
            q.append(r)


    print(longest_route)


if __name__ == "__main__":
    solve2("input.txt")
    