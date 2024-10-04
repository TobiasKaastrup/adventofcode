f = open("4-input.txt")
lines = f.readlines()

total = 0

for line in lines:
    l_r = line.split(",")
    start_l = int(l_r[0].split("-")[0])
    end_l = int(l_r[0].split("-")[1])
    start_r = int(l_r[1].split("-")[0])
    end_r = int(l_r[1].split("-")[1].strip())
    
    if start_l <= start_r and end_l >= end_r:
        total += 1
    elif start_r <= start_l and end_r >= end_l:
        total += 1
print(total)