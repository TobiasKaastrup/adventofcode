import re
def parse(input):
    f = open(input,"r")
    return list(map(str.strip,f.readlines()))

def find(lst, key, value):
    for i, dic in enumerate(lst):
        if dic[key] == value:
            return i
    return -1

def dir_exists(name, filesystem):
    for dir in filesystem:
        if dir["name"] == name:
            print(f'{name} is already a dict')
            return True
    return False

def map_dirs(commands):
    id = 0
    filesystem = [{
        "name": "/",
        "id": id,
        "dirs": [],
        "files": [],
        "parent": 0,
    }]

    current_dir = 0
    for line in commands:
        if line.startswith("$ cd"):
            if ".." in line:
                current_dir = filesystem[current_dir]["parent"] #Problemet er her
                parent_name = line.split("cd ")[1]
                parent_id = find(filesystem,"name",parent_name) #og her
                current_dir = parent_id
            else:
                cd_to = line.split("cd ")[1]
                current_dir = find(filesystem,"name",cd_to+str(current_dir))
        elif line.startswith("dir"):
            name = line.split(" ")[1]
            if not dir_exists(name,filesystem):
                id += 1
                filesystem.append({
                    "name": name+str(current_dir), #Og her - det her med ID'et inde i navnet
                    "id": id,
                    "dirs": [],
                    "files": [],
                    "parent": current_dir
                })
                filesystem[current_dir]["dirs"].append(id)
        elif not line.startswith("$"):
            filesystem[current_dir]["files"].append(int(line.split(" ")[0]))

    return filesystem

def sum_filesizes(filesystem):
    sub_10000 = []
    for dir in filesystem:
        total = 0
        for file in dir["files"]:
            total += file
        for dir in dir["dirs"]:
            for file in filesystem[dir]["files"]:
                total += file
        if total <= 100000:
            sub_10000.append(total)

    result = 0
    for n in sub_10000:
        result += n

    return result

def sol1(input):
    commands = parse(input)
    filesystem = map_dirs(commands)

    print(len(filesystem))
    
    name_set = set()
    for dir in filesystem:
        name_set.add(dir["name"])
    print(len(name_set))

    print(sum_filesizes(filesystem))

    

sol1("test.txt")
