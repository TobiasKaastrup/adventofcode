f = open("3-input.txt", "r")
lines = f.readlines()

result = 0
symbol_set = {'*'}
num_set = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

def get_symbol_indexes(input):
    indexes = []
    current_row = -1

    for row in input:
        current_row += 1
        current_column = -1
        for char in (row.strip()):
            current_column += 1
            if char in symbol_set:
                indexes.append((current_row,current_column))
    return indexes

def get_number_indexes(input):
    indexes = []
    current_row = -1

    for row in input:
        current_row += 1
        current_column = -1
        for char in (row.strip()):
            current_column += 1
            if char in num_set:
                indexes.append((current_row, current_column))
    return indexes


def detect_three_figure_numbers(number_list):
    three_figure_values_and_indexes = []
    number_indexes_without_threes = number_list.copy()

    for i in range(len(number_list)-2):
        value = 0
        number_indexes = []
        if number_list[i][0] == number_list[i+1][0]: #Check if same row

            # Check for 3 figures
            if (number_list[i][1] == number_list[i+1][1] -1 and number_list[i][1] == number_list[i+2][1] -2):
                number_indexes.append(number_list[i])
                number_indexes.append(number_list[i+1])
                number_indexes.append(number_list[i+2])

                number_indexes_without_threes.remove(number_list[i])
                number_indexes_without_threes.remove(number_list[i+1])
                number_indexes_without_threes.remove(number_list[i+2])

                first_row = int(number_list[i][0])
                first_col = int(number_list[i][1])

                second_row = int(number_list[i+1][0])
                second_col = int(number_list[i+1][1])

                third_row = int(number_list[i+2][0])
                third_col = int(number_list[i+2][1])

                value += int(lines[first_row][first_col]) * 100
                value += int(lines[second_row][second_col]) * 10
                value += int(lines[third_row][third_col])

                three_figure_values_and_indexes.append({"value":value,"indexes":number_indexes})

    return three_figure_values_and_indexes, number_indexes_without_threes

def detect_two_figure_numbers(number_list):
    two_figure_values_and_indexes = []
    number_indexes_without_twos = number_list.copy()

    for i in range(len(number_list)-1):
        value = 0
        number_indexes = []
        if number_list[i][0] == number_list[i+1][0]: #Check if same row

            # Check for 2 figures
            if (number_list[i][1] == number_list[i+1][1] -1):
                number_indexes.append(number_list[i])
                number_indexes.append(number_list[i+1])

                number_indexes_without_twos.remove(number_list[i])
                number_indexes_without_twos.remove(number_list[i+1])

                first_row = int(number_list[i][0])
                first_col = int(number_list[i][1])

                second_row = int(number_list[i+1][0])
                second_col = int(number_list[i+1][1])


                value += int(lines[first_row][first_col]) * 10
                value += int(lines[second_row][second_col])

                two_figure_values_and_indexes.append({"value":value,"indexes":number_indexes})

    return two_figure_values_and_indexes, number_indexes_without_twos

def detect_one_figure_numbers(number_list):
    one_figure_values_and_indexes = []

    for i in range(len(number_list)):
        value = 0
        number_indexes = []
        number_indexes.append(number_list[i])
        first_row = int(number_list[i][0])
        first_col = int(number_list[i][1])
        value += int(lines[first_row][first_col])

        one_figure_values_and_indexes.append({"value":value,"indexes":number_indexes})

    return one_figure_values_and_indexes

def check_if_num_is_close_to_symbol(numbers_and_indexes, symbol_list, gear_dict):
    total = 0

    for num_and_index in numbers_and_indexes:
        for index_tuple in num_and_index["indexes"]:
            prev_row = index_tuple[0]-1
            current_row = index_tuple[0]
            next_row = index_tuple[0]+1
            prev_col = index_tuple[1]-1
            current_col = index_tuple[1]
            next_col = index_tuple[1]+1
            if (prev_row,prev_col) in symbol_list:
                if (prev_row,prev_col) in gear_dict:
                    #print(gear_dict[(prev_row,prev_col)])
                    gear_dict[(prev_row,prev_col)]["hits"] += 1
                    gear_dict[(prev_row,prev_col)]["ratio"] *= num_and_index["value"]
                else:
                    gear_dict[(prev_row,prev_col)] = {"hits": 1, "ratio":num_and_index["value"]}
                break
            if (current_row, prev_col) in symbol_list:
                if (current_row,prev_col) in gear_dict:
                    gear_dict[(current_row,prev_col)]["hits"] += 1
                    gear_dict[(current_row,prev_col)]["ratio"] *= num_and_index["value"]
                else:
                    gear_dict[(current_row,prev_col)] = {"hits": 1, "ratio":num_and_index["value"]}

                break
            if (next_row, prev_col) in symbol_list:
                if (next_row,prev_col) in gear_dict:
                    gear_dict[(next_row,prev_col)]["hits"] += 1
                    gear_dict[(next_row,prev_col)]["ratio"] *= num_and_index["value"]
                else:
                     gear_dict[(next_row,prev_col)] = {"hits": 1, "ratio":num_and_index["value"]}

                break
            if (prev_row, current_col) in symbol_list:
                if (prev_row,current_col) in gear_dict:
                    gear_dict[(prev_row,current_col)]["hits"] += 1
                    gear_dict[(prev_row,current_col)]["ratio"] *= num_and_index["value"]
                else:
                    gear_dict[(prev_row,current_col)] = {"hits": 1, "ratio":num_and_index["value"]}

                break
            if (next_row, current_col) in symbol_list:
                if (next_row,current_col) in gear_dict:
                    gear_dict[(next_row,current_col)]["hits"] += 1
                    gear_dict[(next_row,current_col)]["ratio"] *= num_and_index["value"]
                else:
                    gear_dict[(next_row,current_col)] = {"hits": 1, "ratio":num_and_index["value"]}

                break
            if (prev_row, next_col) in symbol_list:
                if (prev_row,next_col) in gear_dict:
                    gear_dict[(prev_row,next_col)]["hits"] += 1
                    gear_dict[(prev_row,next_col)]["ratio"] *= num_and_index["value"]
                else:
                    gear_dict[(prev_row,next_col)] = {"hits": 1, "ratio":num_and_index["value"]}

                break
            if (current_row, next_col) in symbol_list:
                if (current_row,next_col) in gear_dict:
                    gear_dict[(current_row,next_col)]["hits"] += 1
                    gear_dict[(current_row,next_col)]["ratio"] *= num_and_index["value"]
                else:
                    gear_dict[(current_row,next_col)] = {"hits": 1, "ratio":num_and_index["value"]}

                break
            if (next_row, next_col) in symbol_list:
                if (next_row,next_col) in gear_dict:
                    gear_dict[(next_row,next_col)]["hits"] += 1
                    gear_dict[(next_row,next_col)]["ratio"] *= num_and_index["value"]
                else:
                    gear_dict[(next_row,next_col)] = {"hits": 1, "ratio":num_and_index["value"]}

                break
    return gear_dict

#print(get_symbol_indexes(lines))
#print(get_number_indexes(lines))
#get_symbol_indexes(lines)
#print(symbol_set)

number_indexes = get_number_indexes(lines)
symbol_indexes = get_symbol_indexes(lines)

three_fig_val_and_ind, number_indexes_without_threes = detect_three_figure_numbers(number_indexes)

two_fig_val_and_ind, number_indexes_without_twos = detect_two_figure_numbers(number_indexes_without_threes)

one_fig_val_and_ind = detect_one_figure_numbers(number_indexes_without_twos)

gear_dict = {}

gear_dict_three = check_if_num_is_close_to_symbol(three_fig_val_and_ind,symbol_indexes, gear_dict)
gear_dict_two = check_if_num_is_close_to_symbol(two_fig_val_and_ind,symbol_indexes, gear_dict)
gear_dict_one = check_if_num_is_close_to_symbol(one_fig_val_and_ind,symbol_indexes, gear_dict)

print(f'length: {len(gear_dict)}')

gear_total = 0
counter = 1
for key, value in gear_dict.items():
    if value['hits'] == 2:
        #print(f'{counter}: {key}, {value}')
        counter += 1
        gear_total += value["ratio"]

print(f'gear total: {gear_total}')

#print(three_fig_val_and_ind)
print(symbol_indexes)


#two_sum = check_if_num_is_close_to_symbol(two_fig_val_and_ind,symbol_indexes)
#one_sum = check_if_num_is_close_to_symbol(one_fig_val_and_ind,symbol_indexes)
#check_if_num_is_close_to_symbol(three_figures,symbol_indexes)



# FEJL FUNDET HER: 18: (6, 86), {'hits': 2, 'ratio': 53730} Mangler * i indeks (6,82) - ikke alligevel

# Værdi som ikke er med: 19642 - indeks (10,128) tror jeg!?  Finder aldrig stjernen ud for 322 på indeks: [(11, 128), (11, 129), (11, 130)]

# Værdi 4116 - indeks (14,133)