import re
f = open("5-input.txt","r")
data_lines = f.readlines()

f2 = open("5-input.txt","r")
data = f2.read()


stacks = [[],[],[],[],[],[],[],[],[]]
#stacks = [[],[],[]]

for line in data_lines:
    if not re.search(r"\[\w\]",line):
        break
    cubes = re.finditer(r"\[\w\]",line)
    for match in cubes:
        index = int(match.start()/4)
        stacks[index].append(match.group())

for stack in stacks:
    stack.reverse()

#print(stacks)


instructions = data.split('\n\n')[1].split('\n')
for instruction in instructions:
    l = re.findall(r'\d+',instruction)
    l = list(map(int, l))
    if l[0] > 1:
        for i in range(l[0], 0, -1):
            stacks[l[2]-1].append(stacks[l[1]-1][-(i)])
            #stacks[l[1]-1].pop()
            
        for i in range(l[0]):
             stacks[l[1]-1].pop()
        print("moved more than one")
        for stack in stacks:
                print(stack)
    else:
        for i in range(l[0]):
            stacks[l[2]-1].append(stacks[l[1]-1][-1])
            stacks[l[1]-1].pop()
            print("moved one")
        for stack in stacks:
                print(stack)

result = ''
for stack in stacks:
    result = result + stack[-1][1]
    print(stack[-1])

print(result)

