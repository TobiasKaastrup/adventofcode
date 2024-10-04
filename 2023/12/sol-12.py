import re
def parse(input):
    f = open(input,"r")
    lines = f.readlines()

    def strip_line(line):
        return line.strip()

    cleaned = list(map(strip_line,lines))
    return cleaned

def count_arrangements(line):
    count = 1
    ds = list(map(int,re.findall(r'\d',line)))
    cond = line.split(' ')[0]
    s_split = re.split(r'\.+',cond)
    s_split = [x for x in s_split if x]

    #Forward check

    forward_splits = s_split.copy()
    for s in s_split:
        q_marks = s.count('?')
        broken = s.count('#')
        print(ds)
        print(s)
        if (broken == ds[0] and len(ds) <= len(forward_splits)) or (q_marks == ds[0] and broken == 0) or (q_marks + broken == ds[0]):
            ds.pop(0)
            forward_splits.pop(0)
            print("Only one option")

        elif len(ds) > 1 and q_marks + broken == ds[0] + ds[1] + 1:
            ds.pop(0)
            ds.pop(0)
            forward_splits.pop(0)
            print("Only one option")
# Mere end 1 mulighed:
        elif broken == 0 and q_marks == ds[0] + 1:
            count *= 2
            ds.pop(0)
            forward_splits.pop(0)
        else:
            print("Found some possibilities one the remaining splits")
            result, ds_pop = advanced_counting(s,ds)
            if result:
                count *= result
                forward_splits.pop(0)
                continue
            break
        print('---')
    
    print("\nStarting backwards lookup ...")
    backward_splits = forward_splits.copy()
    length = len(forward_splits)-1
    for i in range(length,-1,-1):
        q_marks = forward_splits[i].count('?')
        broken = forward_splits[i].count('#')
        print(ds)
        print(forward_splits[i])
        if (broken == ds[-1]) or (q_marks == ds[-1] and broken == 0) or (q_marks + broken == ds[-1]):
            ds.pop()
            backward_splits.pop()
            print("Only one option")

        elif len(ds) > 1 and q_marks + broken == ds[-1] + ds[-2] + 1:
            ds.pop()
            ds.pop()
            forward_splits.pop(-1)
            print("Only one option")
# Mere end 1 mulighed:
        elif broken == 0 and q_marks == ds[-1] + 1:
            count *= 2
            ds.pop()
            forward_splits.pop(-1)
        else:
            print("Found some possibilities one the remaining splits")
            break
        print('---')

    print(f'remaining splits after backward: {backward_splits}')

    print(f'COUNT: {count}')

def advanced_counting(s, ds):
    print("starting advanced counting")
    count = 0

    tests = []
    test_s = ""
    test_d = ""
    for c in s:
        if c == "?":
            test_s = test_s + "#"
            test_d = test_d + "."
        else:
            test_s = test_s + c
            test_d = test_d + c
    print(test_d)
    print(test_s)


    return False, 0

def sum_arrangements(input):
    sum = 0
    for line in input:
        sum += count_arrangements(line)
    return sum



def sol1(input):
    print("_____________________________________________________________________________________")

    for line in parse(input):
        count_arrangements(line)
        print('\n\n')
    #count_arrangements(parse(input)[0])
    #print(f'The sum of arrangements is: ')

sol1("test.txt")