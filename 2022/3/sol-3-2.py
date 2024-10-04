f = open("3-input.txt","r")
lines = f.readlines()

alpha = '0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

every_fourth_elf = lines[::3]

group_chars = []
group_values = []

for elf in every_fourth_elf:
    i = lines.index(elf)
    for char in elf:
        if char in lines[i+1] and char in lines[i+2]:
            group_chars.append(char)
            group_values.append(alpha.find(char))
            break
total = 0
for value in group_values:
    total += value

print(total)
        

#print(every_fourth_elf)
