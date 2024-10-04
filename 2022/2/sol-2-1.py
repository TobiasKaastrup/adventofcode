f = open("2-input.txt",'r')
lines = f.readlines()

print(lines)

total = 0

def get_points(line):
    if "X" in line:
        if "A" in line:
            return 1+3
        if "B" in line:
            return 1
        if "C" in line:
            return 1+6
        
    if "Y" in line:
        if "A" in line:
            return 2+6
        if "B" in line:
            return 2+3
        if "C" in line:
            return 2

    if "Z" in line:
        if "A" in line:
            return 3
        if "B" in line:
            return 3+6
        if "C" in line:
            return 3+3

for line in lines:
    total += get_points(line)

print(total)
