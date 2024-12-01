from util import parse_lines

def make_lists(input):
    lines = parse_lines(input)
    left_list  = []
    right_list = []

    for line in lines:
        left_list.append(line.split('   ')[0])
        right_list.append(line.split('   ')[1])

    return left_list,right_list

def solve1(input):
    total = 0
    l, r = make_lists(input)

    l.sort()
    r.sort()

    for i, num in enumerate(l):
        total += abs(int(num)-int(r[i]))

    return total

def solve2(input):
    total = 0
    l, r = make_lists(input)

    for num in l:
        total += int(num) * r.count(num)

    return total


if __name__ == "__main__":
    print(solve1("inputs/01.txt"))