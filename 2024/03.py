from util import parse_lines
import re

def solve1(input):
    total = 0
    muls = re.findall("mul\(\d+,\d+\)",input)

    dos = re.findall("do\(\)",input)

    donts = re.findall("don't\(\)")

    for mul in muls:
        nums = re.findall("\d+",mul)
        total += int(nums[0])*int(nums[1])

    return total

def solve2(input):
    total = 0

    enabled = re.split("don't\(\)",input)[0]

    #split on do
    dos = re.split("do\(\)",input)

    for i in range(1,len(dos)):
        #split on don't and add to enabled
        enabled += re.split("don't\(\)",dos[i])[0]


    muls = re.findall("mul\(\d+,\d+\)",enabled)
    for mul in muls:
        nums = re.findall("\d+",mul)
        total += int(nums[0])*int(nums[1])

    return (total)

if __name__ == "__main__":
    with open("inputs/03.txt") as f:
        input = f.read()

    input2 = parse_lines("inputs/03test.txt")
    input2_joined = "".join(input2)
    print(solve2(input2_joined))