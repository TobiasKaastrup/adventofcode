f = open("3-input.txt","r")
lines = f.readlines()

alpha = '0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def split_bag(bag):
    mid = int(len(bag)/2)
    front = bag.strip()[0:mid]
    back =  bag.strip()[mid:]
    if len(front) != len(back):
        print(f"Warning! {bag}")
    return [front,back]

chars = []
char_values = []
for line in lines:
    splitted = split_bag(line)
    print(splitted)
    for char in splitted[0]:
        if char in splitted[1]:
            chars.append(char)
            char_values.append(alpha.find(char))
            break
            

total = 0

for value in char_values:
    total += value

print(char_values)
print(chars)

print(total)

