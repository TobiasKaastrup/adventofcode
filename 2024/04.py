from util import parse_matrix

def solve1(input):
    total = 0
    matrix = parse_matrix(input)

    w = len(matrix[0])
    h = len(matrix)

    for y in range(h):
        for x in range(w):
            if matrix[y][x] == 'X':
                print(f'Checking X on row: {y} col. {x}')

                if x < w-3:
                    if check_right(matrix,y,x):
                        print('XMAS to the right')
                        total += 1

                if x > 2:
                    if check_left(matrix,y,x):
                        print('XMAS to the left')
                        total += 1

                if y < h-3:
                    if check_down(matrix,y,x):
                        print('XMAS down')
                        total += 1

                if y > 2:
                    if check_up(matrix,y,x):
                        print('XMAS up')
                        total += 1
                if y > 2 and x > 2:
                    if check_up_left(matrix,y,x):
                        print('XMAS up left')
                        total += 1
                if y > 2 and x < w-3:
                    if check_up_right(matrix,y,x):
                        print('XMAS up right')
                        total += 1
                if y < h-3 and x > 2:
                    if check_down_left(matrix,y,x):
                        print('XMAS down left')
                        total += 1
                if y < h-3 and x < w-3:
                    if check_down_right(matrix,y,x):
                        print('XMAS down right')
                        total += 1
    return (total)

def solve2(input):
    total = 0
    matrix = parse_matrix(input)

    w = len(matrix[0])
    h = len(matrix)

    for y in range(h):
        for x in range(w):
            if matrix[y][x] == 'A' and x > 0 and x < w-1 and y > 0 and y < h-1:
                print(f'Checking A on row: {y} col. {x}')
                if check_for_mas(matrix,y,x):
                    print("X-MAS")
                    total += 1

    return total



def check_right(matrix,y,x):
    if matrix[y][x+1] == 'M' and matrix[y][x+2] == 'A' and matrix[y][x+3] == 'S':
        return True
    return False

def check_left(matrix,y,x):
    if matrix[y][x-1] == 'M' and matrix[y][x-2] == 'A' and matrix[y][x-3] == 'S':
        return True
    return False
def check_down(matrix,y,x):
    if matrix[y+1][x] == 'M' and matrix[y+2][x] == 'A' and matrix[y+3][x] == 'S':
        return True
    return False

def check_up(matrix,y,x):
    if matrix[y-1][x] == 'M' and matrix[y-2][x] == 'A' and matrix[y-3][x] == 'S':
        return True
    return False

def check_up_left(matrix,y,x):
    if matrix[y-1][x-1] == 'M' and matrix[y-2][x-2] == 'A' and matrix[y-3][x-3] == 'S':
        return True
    return False

def check_up_right(matrix,y,x):
    if matrix[y-1][x+1] == 'M' and matrix[y-2][x+2] == 'A' and matrix[y-3][x+3] == 'S':
        return True
    return False


def check_down_left(matrix,y,x):
    if matrix[y+1][x-1] == 'M' and matrix[y+2][x-2] == 'A' and matrix[y+3][x-3] == 'S':
        return True
    return False

def check_down_right(matrix,y,x):
    if matrix[y+1][x+1] == 'M' and matrix[y+2][x+2] == 'A' and matrix[y+3][x+3] == 'S':
        return True
    return False


def x_check_left(matrix,y,x):
    if matrix[y-1][x-1] == "S" and matrix[y+1][x+1] == "M":
        return True
    if matrix[y-1][x-1] == "M" and matrix[y+1][x+1] == "S":
        return True
    return False

def x_check_right(matrix,y,x):
    if matrix[y-1][x+1] == "S" and matrix[y+1][x-1] == "M":
        return True
    if matrix[y-1][x+1] == "M" and matrix[y+1][x-1] == "S":
        return True
    return False


def check_for_mas(matrix,y,x):
    return x_check_left(matrix,y,x) and x_check_right(matrix,y,x)



if __name__ == "__main__":
    print(solve2("inputs/04.txt"))