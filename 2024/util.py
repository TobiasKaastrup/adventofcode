def parse_lines(input):
    with open(input,"r") as f:
        lines = f.readlines()
    return list(map(str.strip,lines))

def parse_matrix(input_file):
    with open(input_file, "r") as f:
        return [list(line.strip()) for line in f]