def parse(input):
    f = open(input,"r")
    lines = f.readlines()
    return list(map(str.strip,lines))

def move(pos, dir, layout): 
    loss = int(layout[pos[0]][pos[1]])

    if dir == 0: #right
        return (pos[0],pos[1]+1), loss
    if dir == 1: #down
        return (pos[0]+1,pos[1]), loss
    if dir == 2: #left
        return (pos[0],pos[1]-1), loss
    if dir == 3: #up
        return (pos[0]-1,pos[1]), loss

def get_possible_directions(pos,latest_dirs,layout):
    south_edge = len(layout)-1
    east_edge = len(layout[0])-1
    dirs = [0,1,2,3]
    #remove opposite of last dir or if it would go OOB
    if latest_dirs[-1] == 0 or pos[1] == 0:
        dirs.remove(2)
    if latest_dirs[-1] == 1 or pos[0] == 0:
        dirs.remove(3)
    if latest_dirs[-1] == 2 or pos[1] == east_edge:
        dirs.remove(0)
    if latest_dirs[-1] == 3 or pos[0] == south_edge:
        dirs.remove(1)
    #Remove dir if the last three dirs were that one
    if len(set(latest_dirs)) == 1:
        try:
            dirs.remove(latest_dirs[0])
        except ValueError:
            x = 0
    return dirs


def check_shortest_path(layout,current_loss, prev_best):
    position = (0,0)
    latest_dirs = [-1,-2,-3]
    end = (len(layout)-1,len(layout[0])-1)
    total_loss = current_loss
    other_directions = [] #should also hold current total loss
    possible_dirs = get_possible_directions(position, latest_dirs,layout)
    while len(possible_dirs) > 0:
        lowest_possible_dir = min(possible_dirs)
        possible_dirs.remove(lowest_possible_dir)
        for dir in possible_dirs:
            other_directions.append(((position,dir),total_loss))
        position, loss = move(position, lowest_possible_dir,layout)
        total_loss += loss
        if position == end or (prev_best != 0 and total_loss > prev_best): #OR IF TOTAL > BEST ONE YET
            break
        latest_dirs.pop(0)
        latest_dirs.append(lowest_possible_dir)
        possible_dirs = get_possible_directions(position,latest_dirs,layout)
        
        #print(position)
    return total_loss, other_directions


def check_others(others,layout,best_result,unique_dirs):
    new_directions = []
    for dir in others:
        #print(f"Checking shortest path for: {dir}")
        loss, new_others = check_shortest_path(layout,dir[1],best_result)
        best_result = min(best_result,loss)
        #print(f'result was: {loss}')
        for other in new_others:
            if other[0] in unique_dirs.keys():
                if other[1] < unique_dirs[other[0]]:
                    new_directions.append(other)
            else:
                new_directions.append(other)
    return best_result, new_directions
        





# def solve1(input):
#     layout = parse(input)
#     shortest_loss, other_directions = check_shortest_path(layout,0,0)
#     min_loss = shortest_loss
#     unique_dirs = {}
#     for dir in other_directions:
#         unique_dirs[dir[0]] = dir[1]
#     #print(unique_dirs)

#     while len(other_directions) > 0:
#         best, other_directions = check_others(other_directions,layout,min_loss,unique_dirs)
#         for dir in other_directions:
#             unique_dirs[dir[0]] = dir[1]
#         print(best)
#         print(len(other_directions))

def solve1(input):
    layout = parse(input)
    shortest_loss, other_directions = check_shortest_path(layout,0,0)
    min_loss = shortest_loss
    unique_dirs = {}
    for dir in other_directions:
        loss, others = check_shortest_path(layout,dir[1],130)
        print(loss)




if __name__ == "__main__":
    solve1("test.txt")