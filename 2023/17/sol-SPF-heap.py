import math
import heapq
def parse(input):
    f = open(input,"r")
    lines = f.readlines()
    return list(map(str.strip,lines))

def move(pos, dir, current_loss, layout):

    if dir == 0: #right
        loss = int(layout[pos[0]][pos[1]+1])
        return (pos[0],pos[1]+1), loss+current_loss
    if dir == 1: #down
        loss = int(layout[pos[0]+1][pos[1]])
        return (pos[0]+1,pos[1]), loss+current_loss
    if dir == 2: #left
        loss = int(layout[pos[0]][pos[1]-1])
        return (pos[0],pos[1]-1), loss+current_loss
    if dir == 3: #up
        loss = int(layout[pos[0]-1][pos[1]])
        return (pos[0]-1,pos[1]), loss+current_loss

def get_possible_directions_v2(pos,latest_dirs,layout):
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
    #Remove dir if the last ten dirs were that one
    if len(set(latest_dirs)) == 1:
        try:
            dirs.remove(int(latest_dirs[0]))
        except ValueError:
            x = 0
    #Remove all other dirs if last four were not the same
    for i in range(-2,-5,-1):
        if latest_dirs[i] != latest_dirs[-1]:
            dirs_to_remove = [0,1,2,3]
            dirs_to_remove.remove(int(latest_dirs[-1]))
            for dir in dirs_to_remove:
                try:
                    dirs.remove(dir)
                except ValueError:
                    x = 0
    return dirs

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


def solve1(input):
    layout = parse(input)
    visited = {}

    e = f"{(len(layout)-1,len(layout[0])-1)}"
    
    #Vars to keep track of position and directions
    pos = (0,0)
    current_loss = 0
    
    q = [[(0,0),0,[-3,-2,-1]]]

    while len(q) > 0: #Should not keep looping, should just go with the shortest path recorded!
    #for i in range(100000):
        next = q[0]
        next_pos = next[0]
        next_latest_dirs = next[2]
        loss_of_next = next[1]

        #clean queue
        q.pop(0)
    
        dirs = get_possible_directions(next_pos,next_latest_dirs,layout)

        for dir in dirs:
            latest_dirs = next_latest_dirs.copy()
            latest_dirs.pop(0)
            latest_dirs.append(dir)
            new_postion, loss = move(next_pos,dir,loss_of_next,layout)
            id = f'{new_postion}-{latest_dirs}'

            if id not in visited.keys():
                visited[id] = loss
                q.append([new_postion,loss,latest_dirs])
            else:
                if visited[id] > loss:
                    visited[id] = loss
                    q.append([new_postion,loss,latest_dirs])
            
        q.sort(key=sort_by_shortest)
    #print(visited)
        
    end_losses = []

    for key, value in visited.items():
        if key.startswith(e):
            end_losses.append(value)
    
    print(min(end_losses))

def solve2(input):
    layout = parse(input)
    visited = {}

    e = f"{(len(layout)-1,len(layout[0])-1)}"

    #Vars to keep track of position and directions
    pos = (0,0)
    current_loss = 0

    #q = [[(0,0),0,[3,3,3,3,-6,-5,3,3,3,3]]]
    q = [(0,((0,0),"3333653333"))]
    heapq.heapify(q)

    best_end_loss = math.inf

    while len(q) > 0: #Should not keep looping, should just go with the shortest path recorded!
    #for i in range(100000):
        next = heapq.heappop(q)
        next_pos = next[1][0]
        next_latest_dirs = next[1][1]
        loss_of_next = next[0]

        dirs = get_possible_directions_v2(next_pos,next_latest_dirs,layout)

        for dir in dirs:
            latest_dirs = next_latest_dirs
            latest_dirs = latest_dirs[1:]
            latest_dirs += str(dir)
            new_position, loss = move(next_pos,dir,loss_of_next,layout)
            id = f'{new_position}-{latest_dirs}'
            print(new_position)

            if str(new_position) == e:
                if loss < best_end_loss:
                    best_end_loss = loss
                    #best_end_loss = min(best_end_loss,loss)
                    print(f"new best endloss: {best_end_loss}")

            if loss < best_end_loss:

                if id not in visited.keys():
                    visited[id] = loss
                    #Headpush here
                    heapq.heappush(q,(loss,(new_position,latest_dirs)))
                    #q.append([new_postion,loss,latest_dirs])
                else:
                    if visited[id] > loss:
                        visited[id] = loss
                        #heappush here
                        heapq.heappush(q,(loss,(new_position,latest_dirs)))
                        #q.append([new_postion,loss,latest_dirs])

    print("FINISHED!")

    print(best_end_loss)
    # end_losses = []

    # for key, value in visited.items():
    #     #print(key,value)
    #     if key.startswith(e):
    #         end_losses.append(value)

    # print(min(end_losses))

if __name__ == "__main__":
    solve2("input.txt")