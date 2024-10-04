f = open("4-input.txt", "r")
lines = f.readlines()

elf_total = 0


def str_to_int(str):
    return int(str)

def check_lines(line_list, prev_total):
    copied_cards = []

    for line in line_list:

        winners_raw = line.split('|')[0]
        drawn_raw = line.split('|')[1]

        winners_clean = winners_raw.split(':')[1].strip().replace("  ", " ").split(" ")
        drawn_clean = drawn_raw.strip().replace("  ", " ").split(" ")

        winner_ints = list(map(str_to_int, winners_clean))
        drawn_ints = list(map(str_to_int, drawn_clean))

        for i, num in enumerate(drawn_ints):
            hits_on_card = 0
            if num in winner_ints:
                hits_on_card += 1
                copied_cards.append(line_list[i+hits_on_card])

    if(len(copied_cards) == 0):
        return "finished"
    this_total = prev_total + len(copied_cards)
    print(f"finished function run, this total: {this_total}")
    check_lines(copied_cards, this_total)


check_lines(lines, 0)
print(elf_total)