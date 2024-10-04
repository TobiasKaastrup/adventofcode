f = open("2-input.txt", "r")
lines = f.readlines()

result = 0

# only 12 red cubes, 13 green cubes, and 14 blue cubes?

def game_cleaner(game):
    id_and_data = game.split(':')
    id = id_and_data[0].split("Game ")[1]
    data = id_and_data[1].strip()

    game_dict = {
        "id": int(id),
        "shows": 0,
        "red": [],
        "green": [],
        "blue": [],
    }

    for show in data.split(';'):
        game_dict["shows"] += 1
        game_dict["blue"].append(0)
        game_dict["green"].append(0)
        game_dict["red"].append(0)
        cubes = show.split(',')

        for color in cubes:
            if "green" in color:
                game_dict["green"][game_dict["shows"] - 1]  += int(color.split(' green')[0])
            elif "blue" in color:
                game_dict["blue"][game_dict["shows"] - 1]  += int(color.split(' blue')[0])
            elif "red" in color:
                game_dict["red"][game_dict["shows"] - 1]  += int(color.split(' red')[0])
    return game_dict



def check_if_possible(game_dict):
    # Returns the ID if the game is possible
    for num in game_dict["red"]:
        if num > 12:
            return 0
    for num in game_dict["blue"]:
        if num > 14:
            return 0
    for num in game_dict["green"]:
        if num > 13:
            return 0

    return game_dict["id"]

def find_highest_of_each_color(game_dict):

    result = [0,0,0]
    for num in game_dict["red"]:
        if num > result[0]:
            result[0] = num
    for num in game_dict["green"]:
        if num > result[1]:
            result[1] = num
    for num in game_dict["blue"]:
        if num > result[2]:
            result[2] = num
    return result

def multiply_min_values(list_of_mins):
    result = 1
    for num in list_of_mins:
        result *= num
    return result

final_result = 0

for game in lines:
    dict = game_cleaner(game)
    #dict["minRGB"] = find_highest_of_each_color(dict)
    power = multiply_min_values(find_highest_of_each_color(dict))
    final_result += power

print(final_result)




