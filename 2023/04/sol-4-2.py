f = open("4-input.txt", "r")
lines = f.readlines()

elf_total = 0
copy_dict = {}

def str_to_int(str):
    return int(str)

for i, line in enumerate(lines):

    winners_raw = line.split('|')[0]
    drawn_raw = line.split('|')[1]

    winners_clean = winners_raw.split(':')[1].strip().replace("  ", " ").split(" ")
    drawn_clean = drawn_raw.strip().replace("  ", " ").split(" ")

    winner_ints = list(map(str_to_int, winners_clean))
    drawn_ints = list(map(str_to_int, drawn_clean))

    if i not in copy_dict:
        copy_dict[i] = 1
    else:
        copy_dict[i] += 1
    
    for copy in range(copy_dict[i]):
        card_winnings = 0
        for num in drawn_ints:
            if num in winner_ints:
                if i+1+card_winnings in copy_dict:
                    copy_dict[i+1+card_winnings] +=1
                else:
                    copy_dict[i+1+card_winnings] = 1
                card_winnings += 1
print(copy_dict)

for value in copy_dict.values():
    elf_total += value
print(elf_total)