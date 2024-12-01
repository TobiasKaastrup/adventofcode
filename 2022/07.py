#working on test but not on full input

from util import parse_lines


def find_all_dirs_and_files(input):
    dirs = {}
    files = {}
    prev_dir = ""
    current_dir = ""
    for line in input:
        if line == "$ cd ..":
            current_dir = prev_dir #this may be the bug - maybe the full input sometimes jumps more than one level
        elif line.startswith("$ cd"):
            prev_dir = current_dir
            current_dir = line[5:]
            dirs[current_dir] = {
                "files": [],
                "dirs": []
            }
        elif line == "$ ls":
            hello = "hello"
        #find subdirs
        elif line.startswith("dir"):
            name = line.split(" ")[1]
            dirs[current_dir]["dirs"].append(name)
        else:
            size = line.split(" ")[0]
            filename = line.split(" ")[1]
            files[filename] = int(size)
            dirs[current_dir]["files"].append(filename)


    return dirs, files

def get_total_file_size(dir_id,dirs,files):
    total = 0
    dir_dict = dirs[dir_id]
    print(dir_id,dir_dict)
    for file in dir_dict["files"]:
        total += files[file]

    for dir in dir_dict["dirs"]:
        total += get_total_file_size(dir,dirs,files)

    return total


def solve1(input):
    total = 0
    lines = parse_lines(input)
    dirs, files = find_all_dirs_and_files(lines)

    for dir in dirs.keys():
        dir_volume = get_total_file_size(dir,dirs,files)
        if dir_volume < 100000:
            total += dir_volume
    print(f"\nSolution 1, sum of directory sizes < 100.000: \n\n{total}")

if __name__ == "__main__":
    solve1("inputs/07.txt")