def parse(input):
    f = open(input,"r")
    return f.read()

def find_marker(string):
    for i in range(4,len(string)):
        char_set = set()
        for j in range(4):
            char_set.add(string[i-j])
        if len(char_set) == 4:
            print(i+1)
            break

def find_message(string):
    for i in range(14,len(string)):
        char_set = set()
        for j in range(14):
            char_set.add(string[i-j])
        if len(char_set) == 14:
            print(i+1)
            break


def sol1(input):
    find_marker((parse(input)))

def sol2(input):
    find_message((parse(input)))

sol2("input.txt")