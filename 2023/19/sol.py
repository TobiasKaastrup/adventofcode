import re
def parse(input):
    f = open(input,"r")
    data = f.read()
    splitted = data.split("\n\n")
    workflow_dict = {}
    workflows = splitted[0].split("\n")
    for workflow in workflows:
        id = workflow.split("{")[0]
        content = workflow.split("{")[1][:-1]
        workflow_dict[id] = content.split(",")

    parts = []
    ratings = splitted[1].split("\n")
    for rating in ratings:
        part = {}
        ratings = rating[1:-1].split(",")
        for rat in ratings:
            part[rat.split("=")[0]] = int(rat.split("=")[1])
        parts.append(part)
    return workflow_dict,parts

def check_part(part, workflow_dict):
    current_flow = "in"
    while current_flow not in ["A", "R"]:
        for condition in workflow_dict[current_flow]:
            if ":" not in condition:
                current_flow = condition
            else:
                category = condition[0]
                operator = condition[1]
                value = int(re.findall(r"\d+",condition)[0])
                destination = condition.split(":")[1]

                if operator ==  "<":
                    if part[category] < value:
                        current_flow = destination
                        break
                if operator ==  ">":
                    if part[category] > value:
                        current_flow = destination
                        break
    return current_flow

def find_accepted_combinations(workflow_dict):
    accepted = 0
    # for x in range(4000):
    #     for m in range(4000):
    #         for a in range(4000):
    #             for s in range(4000):
    #                 combination = {"x":x,"m":m,"a":a,"s":s}
    #                 print(combination)
    #                 if check_part(combination,workflow_dict) == "A":
    #                     accepted += 1
    accepted_a_range = []
    accepted_a = False
    for a in range(1,4001):
        combination = {"x":1,"m":1,"a":a,"s":1}
        if check_part(combination, workflow_dict) == "A":
            if not accepted_a:
                accepted_a = True
                accepted_a_range.append(a)
            if a == 4000:
                accepted_a_range.append(4001)
        else:
            if accepted_a:
                accepted_a = False
                accepted_a_range.append(a)
        

    accepted_x_range = []
    accepted_x = False
    for x in range(1,4001):
        combination = {"x":x,"m":1,"a":1,"s":1}
        if check_part(combination, workflow_dict) == "A":
            if not accepted_x:
                accepted_x= True
                accepted_x_range.append(x)
            if x == 4000:
                accepted_x_range.append(4001)
        else:
            if accepted_x:
                accepted_x = False
                accepted_x_range.append(x)

    accepted_m_range = []
    accepted_m = False
    for m in range(1,4001):
        combination = {"x":1,"m":m,"a":1,"s":1}
        if check_part(combination, workflow_dict) == "A":
            if not accepted_m:
                accepted_m= True
                accepted_m_range.append(m)
            if m == 4000:
                accepted_m_range.append(4001)
        else:
            if accepted_m:
                accepted_m = False
                accepted_m_range.append(m)

    accepted_s_range = []
    accepted_s = False
    for s in range(1,4001):
        combination = {"x":1,"m":m,"a":1,"s":1}
        if check_part(combination, workflow_dict) == "A":
            if not accepted_s:
                accepted_s= True
                accepted_s_range.append(s)
            if s == 4000:
                accepted_s_range.append(4001)
        else:
            if accepted_s:
                accepted_s = False
                accepted_s_range.append(s)

    print(accepted_x_range)
    print(accepted_m_range)
    print(accepted_a_range)
    print(accepted_s_range)

def solve1(input):
    workflow_dict, parts = parse(input)
    total = 0
    for part in parts:
        if check_part(part, workflow_dict) == "A":
            for rating in part.values():
                total += rating
    print(total)

def solve2(input):
    workflow_dict, parts = parse(input)
    find_accepted_combinations(workflow_dict)


if __name__ == "__main__":
    solve2("test.txt")


    
