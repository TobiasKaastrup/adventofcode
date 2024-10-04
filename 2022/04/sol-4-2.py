f = open("4-input.txt")
lines = f.readlines()

total = 0

for line in lines:
    l_r = line.split(",")
    start_l = int(l_r[0].split("-")[0])
    end_l = int(l_r[0].split("-")[1])
    start_r = int(l_r[1].split("-")[0])
    end_r = int(l_r[1].split("-")[1].strip())
    
    if start_l < start_r and end_l < start_r:
        print("case 1")
        continue
    elif start_r < start_l and end_r < start_l:
        print("case 2")
        continue
    else:
        print("case 3")
        total += 1
print(total)