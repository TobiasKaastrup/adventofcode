import re
def parse(input):
    f = open(input,"r")
    data = f.read()

    patterns = data.split('\n\n')
    return patterns

def find_vertical(pattern):
    print("----------")
    print(pattern)

    print("Vertical smudges:")
    pattern = pattern.split("\n")
    rows = len(pattern)
    columns = len(pattern[0])
    advanced_candidates = []
    for cand in range(1,columns):
        smudges = 0
        flag = False
        row_range = min(columns-cand,cand)
        for row in pattern:
            for i in range(0,row_range):
                if flag:
                    break
                left = row[cand-1-i]
                right = row[cand+i]
                if left != right:
                    smudges += 1
        if smudges == 1:
            advanced_candidates.append(cand)
    if advanced_candidates:
        return advanced_candidates[0]
    else:
        return 0

def find_horizontal(pattern):
    pattern = pattern.split("\n")
    rows = len(pattern)
    columns = len(pattern[0])
    advanced_candidates = []
    for cand in range(1,rows):
        smudges = 0
        flag = False
        col_range = min(rows-cand,cand)
        for c in range(columns):
            for i in range(0,col_range):
                if flag:
                    break
                left = pattern[cand-i-1][c]
                right = pattern[cand+i][c]
                if left != right:
                    smudges += 1

        if smudges == 1:
            advanced_candidates.append(cand)
    if advanced_candidates:
        return advanced_candidates[0] * 100
    else:
        return 0

def sol2(input):
    patterns = parse(input)
    ans = 0
    for pattern in patterns:
        ans += find_vertical(pattern)
        ans += find_horizontal(pattern)
    print(f"The answer for part 2 is: {ans}")

sol2("input.txt")