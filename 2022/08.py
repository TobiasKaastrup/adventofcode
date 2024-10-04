from util import parse_matrix

def get_outer_visible(input):
    return len(input)*2+len(input[0])*2-4

def check_if_tree_is_visible(tree,matrix):
    x = tree[0]
    y = tree[1]
    height = matrix[x][y]

    print(f"\n-----checking new tree: {tree} height: {height}--------")

    #check others to the left (row)
    leftVis = True
    for i in range(0,y):
        print(f"checking row {x}, col {i}, height: {matrix[x][i]}")
        if matrix[x][i] >= height:
            #ie. not visible
            print("Not visible from the left!")
            leftVis = False
            break
    if(leftVis):
        print("TRUE visible to the left")
        return True

    #check others to the right (row)
    rightVis = True
    for i in range(y+1,len(matrix[0])):
        print(f"checking row {x}, col {i}, height: {matrix[x][i]}")
        if matrix[x][i] >= height:
            #ie. not visible
            print("Not visible from the right")
            rightVis = False
            break
    if rightVis:
        print("TRUE visible to the right")
        return True

    #check above
    aboveVis = True
    for i in range(0,x):
        print(f"checking row {i}, col {y}, height: {matrix[i][y]}")
        if matrix[i][y] >= height:
            print("Not visible from above!")
            aboveVis = False
            break
    if aboveVis:
        print("TRUE visible from above")
        return True
        

    #check below
    belowVis = True
    for i in range(x+1, len(matrix[0])):
        print(f"checking row {i}, col {y}, height: {matrix[i][y]}")
        if matrix[i][y] >= height:
            print("Not visible from below!")
            belowVis = False
            break
    if belowVis:
        print("TRUE visible from below")
        return True
        
    return False

def check_all_inner_trees(matrix):
    total = 0
    for i in range(1,len(matrix)-1):
        for j in range(1,len(matrix[0])-1):
            if(check_if_tree_is_visible((i,j),matrix)):
                total += 1
    return total

def get_scenic_score(tree,matrix):
    x = tree[0]
    y = tree[1]
    height = matrix[x][y]

    print(f"\n-----checking new tree: {tree} height: {height}--------")

    #check others to the left (row)
    print("\nLEFT")
    left_count = 0
    for i in range(y-1,0-1,-1):
        left_count += 1
        print(f"checking row {x}, col {i}, height: {matrix[x][i]}")
        if matrix[x][i] >= height:
            break
    print(f"scenic: {left_count}")

    #check others to the right (row)
    print("\nRIGHT")
    right_count = 0
    
    for i in range(y+1,len(matrix[0])):
        print(f"checking row {x}, col {i}, height: {matrix[x][i]}")
        right_count += 1
        if matrix[x][i] >= height:
            #ie. not visible
            break
    print(f"scenic: {right_count}")

    #check above
    print("\nABOVE")
    above_count = 0
    for i in range(x-1,0-1,-1):
        print(f"checking row {i}, col {y}, height: {matrix[i][y]}")
        above_count += 1
        if matrix[i][y] >= height:
            break
    print(f"scenic: {above_count}")


    #check below
    print("\nBELOW")
    below_count = 0
    for i in range(x+1, len(matrix[0])):
        print(f"checking row {i}, col {y}, height: {matrix[i][y]}")
        below_count += 1
        if matrix[i][y] >= height:
            break
    print(f"scenic: {below_count}")

    scenic_score = below_count*above_count*right_count*left_count
    print(f"scenic score: {scenic_score}")
    return scenic_score

def find_most_scenic_tree(matrix):
    best = 0
    for i in range(1,len(matrix)-1):
        for j in range(1,len(matrix[0])-1):
            best = max(get_scenic_score((i,j),matrix),best)

    return best


def solve1(input):
    outer = get_outer_visible(input)
    inner = check_all_inner_trees(input)
    print(f'\n\n\nSOLUTION: \nnumber of visible trees: {inner + outer}')

def solve2(input):
    best = find_most_scenic_tree(input)
    print(f'\n\n\nSOLUTION2: \nbest scenic score: {best}')

if __name__ == "__main__":
    matrix = parse_matrix("inputs/08.txt")
    solve2(matrix)