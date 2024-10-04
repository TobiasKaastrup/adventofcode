import re
def parse(input):
    f = open(input,"r")
    return f.read()

def convert(string):
    total = 0
    for char in string:
        total += ord(char)
        total *= 17
        total = total%256
    return total

def make_boxes():
    boxes = []
    for i in range(256):
        boxes.append([])
    return boxes

def calculate_power(box,slot,focal_length):
    return (box+1)*(slot+1)*focal_length


def solve(input):
    data = parse(input).split(",")
    result = 0
    for part in data:
        result += convert(part)
    print(result)

def solve2(input):
    data = parse(input).split(",")
    boxes = make_boxes()
    #print(data)

    for part in data:
        label = re.match(r"\w+",part).group()
        box = convert(label)
        
        if "-" in part:
            boxes[box] = [x for x in boxes[box] if x["label"] != label]

        if "=" in part:
            focal_length = part[-1]
            replaced = False
            for slot in boxes[box]:
                if slot["label"] == label:
                    slot["focal_length"] = int(focal_length)
                    replaced = True
                    break
            if not replaced:
                    boxes[box].append({"label":label,"focal_length":int(focal_length)})
    
    result = 0

    for i,box in enumerate(boxes):
        for j,lens in enumerate(box):
            result += calculate_power(i,j,lens["focal_length"])
    print(boxes)
    
    print(result)







#solve("input.txt")

solve2("input.txt")