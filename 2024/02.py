from util import parse_lines

def check_if_line_is_safe(line):
    nums = list(map(int,line.split(' ')))
    #check if asc or desc
    ascending = nums[0] < nums[1]
    i = 0
    print(f"checking line {line}")
    while i < len(nums)-1:
        if abs(nums[i] - nums[i+1]) > 3:
            print("tooo big")
            return 0
        if ascending and nums[i] >= nums[i+1]:
            print("not ascending")
            return 0
        if not ascending and nums[i] <= nums[i+1]:
            print("not descending")
            return 0
        i+= 1
    print("Safe!")
    return 1

def check_if_line_is_safe_with_dampener(line):
    if check_if_line_is_safe(line) == 1:
        return 1
    else:
        safe_with_removal = False
        for x in range(0,len(line.split(" "))):
            if remove_index_and_check_if_safe(line,x) == 1:
                return 1
        if not safe_with_removal:
            return 0
        

def remove_index_and_check_if_safe(line,index):
    #make a copy of list before popping
    new_line = line.split(" ")
    new_line.pop(index)
    linestring = " ".join(str(x) for x in new_line)
    return check_if_line_is_safe(linestring)

def solve1(input):
    total = 0
    lines = parse_lines(input)

    for line in lines:
        total += check_if_line_is_safe(line)

    return total

def solve2(input):
    total = 0
    lines = parse_lines(input)

    for line in lines:
        total += check_if_line_is_safe_with_dampener(line)

    return total

if __name__ == "__main__":
    print(solve2("inputs/02.txt"))