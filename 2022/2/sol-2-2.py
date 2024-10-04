f = open("2-input.txt",'r')
lines = f.readlines()

print(lines)

total = 0

def get_points(line):
    if "A" in line:
        if "X" in line:
            return 3+0
        if "Y" in line:
            return 1+3
        if "Z" in line:
            return 2+6
        
    if "B" in line:
        if "X" in line:
            return 1+0
        if "Y" in line:
            return 2+3
        if "Z" in line:
            return 3+6

    if "C" in line:
        if "X" in line:
            return 2+0
        if "Y" in line:
            return 3+3
        if "Z" in line:
            return 1+6

for line in lines:
    total += get_points(line)

print(total)
