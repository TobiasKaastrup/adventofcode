def parse_lines(input):
    with open(input,"r") as f:
        lines = f.readlines()
    return list(map(str.strip,lines))

