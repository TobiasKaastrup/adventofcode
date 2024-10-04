import re
def parse(input):
    f = open(input,"r")
    data = f.read()

    patterns = data.split('\n\n')
    return patterns

def find_vertical(pattern):
    print("----------")
    #print(pattern)
    pattern = pattern.split("\n")
    candidates = []
    rows = len(pattern)
    columns = len(pattern[0])
    for i in range(columns-1):
        candidates.append(i+1)
        for j in range(rows):
            if pattern[j][i] != pattern[j][i+1]:
                candidates.pop()
                break
            
    #print(candidates)
    advanced_candidates = []
    for cand in candidates:
        flag = False
        advanced_candidates.append(cand)
        row_range = min(columns-cand,cand)
        #print(row_range)
        for row in pattern:
            for i in range(1,row_range):
                if flag:
                    break
                left = row[cand-i-1]
                right = row[cand+i]
                if left != right:
                    #print(f'Candidate {cand} was not a mirror')
                    advanced_candidates.pop()
                    flag = True
                    break
    #print(f"Candidates: {advanced_canditates}")
    if advanced_candidates:
        return advanced_candidates[0]
    else:
        return 0

def find_horizontal(pattern):
    print("----------")
    #print(pattern)
    pattern = pattern.split("\n")
    candidates = []
    rows = len(pattern)
    columns = len(pattern[0])
    for i in range(rows-1):
        candidates.append(i+1)
        for j in range(columns):
            if pattern[i][j] != pattern[i+1][j]:
                candidates.pop()
                break
            
    #print(candidates)
    advanced_candidates = []
    for cand in candidates:
        flag = False
        advanced_candidates.append(cand)
        col_range = min(rows-cand,cand)
        #print(row_range)
        for c in range(columns):
            for i in range(1,col_range):
                if flag:
                    break
                left = pattern[cand-i-1][c]
                right = pattern[cand+i][c]
                if left != right:
                    #print(f'Candidate {cand} was not a mirror')
                    advanced_candidates.pop()
                    flag = True
                    break
    print(f"Candidates: {advanced_candidates}")
    if advanced_candidates:
        return advanced_candidates[0] * 100
    else:
        return 0

def sol1(input):
    patterns = parse(input)
    #print(patterns)
    ans = 0
    for pattern in patterns:
        #ans += find_vertical(pattern)
        ans += find_horizontal(pattern)
    print(f"The answer for part 1 is: {ans}")

sol1("input.txt")