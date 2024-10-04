f = open("1-input.txt",'r')
data = f.read()

elfs = data.split('\n\n')

elf_top_three = [0,0,0]
total = 0

for elf in elfs:
    count = 0
    for calorie in elf.split("\n"):
        count += int(calorie)
    if count > elf_top_three[0]:
        elf_top_three.insert(0, count)
    elif count > elf_top_three[1]:
        elf_top_three.insert(1, count)
    elif count > elf_top_three[2]:
        elf_top_three.insert(2, count)

for elf in elf_top_three[:3]:
    total += elf

print(total)