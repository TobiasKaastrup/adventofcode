f = open("4-input.txt", "r")
lines = f.readlines()

elf_total = 0

def str_to_int(str):
    return int(str)

for line in lines:
    card_total = 0

    winners_raw = line.split('|')[0]
    drawn_raw = line.split('|')[1]

    winners_clean = winners_raw.split(':')[1].strip().replace("  ", " ").split(" ")
    drawn_clean = drawn_raw.strip().replace("  ", " ").split(" ")

    winner_ints = list(map(str_to_int, winners_clean))
    drawn_ints = list(map(str_to_int, drawn_clean))

    for num in drawn_ints:
        if num in winner_ints:
            if card_total == 0:
                card_total = 1
            else:
                card_total *= 2
    elf_total += card_total
    
print(elf_total)