from collections import deque
def parse(input):
    with open(input,"r") as f:
        lines = f.readlines()
    return list(map(str.strip, lines))

def take_step(current_plots, reachable_plots, layout):
    new_plots = set()

    for plot in current_plots:
        for dir in range(4):
            if dir == 0: #UP
                new_plot = (plot[0]-1,plot[1])
            elif dir == 1: #RIGHT
                new_plot = (plot[0],plot[1]+1)
            elif dir == 2: #DOWN
                new_plot = (plot[0]+1,plot[1])
            elif dir == 3: #LEFT
                new_plot = (plot[0],plot[1]-1)
            if layout[new_plot[0]][new_plot[1]] != "#":
                #print(new_plot)
                new_plots.add(new_plot)
    return new_plots

def solve1(input, steps):
    layout = parse(input)

    #Find s
    for i, row in enumerate(layout):
        for j in range(len(row)):
            if layout[i][j] == "S":
                s = (i,j)

    reachable_plots = [s]
    q = deque([[s]])

    #Needs to keep track of steps taken!
    for i in range(steps):
        next = q.popleft()
        new_plots = take_step(next,reachable_plots,layout)
        q.append(new_plots)
        for plot in new_plots:
            reachable_plots.append(plot)
        print(f"After {i+1} steps: {len(new_plots)} plots are reachable")
    

def solve2(input,steps):
    layout = parse(input)

    north_edge = 0
    west_edge = 0
    south_edge = len(layout)
    east_edge = len(layout[0])

    

if __name__ == "__main__":
    solve1("input.txt", 64)
