f = open("5-input.txt", "r")
data = f.read()

segments = data.split("\n\n")

locations = []

def str_to_int(str):
    return int(str)

seeds_v1 = list(map(str_to_int,segments[0].split(':')[1].strip().split(' ')))
first_seed_pair = [104847962,3583832]
second_seed_pair = [1212568077, 114894281]
third_seed_pair = [3890048781,333451605]
fourth_seed_pair = [1520059863,217361990]
fifth_seed_pair = [310308287,12785610]
sixt_seed_pair = [3492562455,292968049]
eight_seed_pair = [1901414562,516150861]
nineth_seed_pair = [2474299950,152867148]
tenth_seed_pair = [3394639029,59690410]
eleventh_seed_pair = [862612782,176128197]

seed_tuples = []

for i, seed in enumerate(seeds_v1):
    if i%2 == 0:
        seed_tuples.append((seed,seeds_v1[i+1]))

#print(seed_tuples)


# SOIL MAP

seed_to_soil_map_lines = segments[1].split(':')[1].strip().split('\n')
seed_to_soil_map = []

for line in seed_to_soil_map_lines:
    info = line.split(' ')
    conversion_dict = {}
    conversion_dict["source"] = int(info[1])
    conversion_dict["destination"] = int(info[0])
    conversion_dict["range"] = int(info[2])
    seed_to_soil_map.append(conversion_dict)

# FERTILIZER MAP

soil_to_fertilizer_map_lines = segments[2].split(':')[1].strip().split('\n')
soil_to_fertilizer_map = []

for line in soil_to_fertilizer_map_lines:
    info = line.split(' ')
    conversion_dict = {}
    conversion_dict["source"] = int(info[1])
    conversion_dict["destination"] = int(info[0])
    conversion_dict["range"] = int(info[2])
    soil_to_fertilizer_map.append(conversion_dict)

# WATER MAP

fertilizer_to_water_map_lines = segments[3].split(':')[1].strip().split('\n')
fertilizer_to_water_map = []

for line in fertilizer_to_water_map_lines:
    info = line.split(' ')
    conversion_dict = {}
    conversion_dict["source"] = int(info[1])
    conversion_dict["destination"] = int(info[0])
    conversion_dict["range"] = int(info[2])
    fertilizer_to_water_map.append(conversion_dict)

# LIGHT MAP

water_to_light_map_lines = segments[4].split(':')[1].strip().split('\n')
water_to_light_map = []

for line in water_to_light_map_lines:
    info = line.split(' ')
    conversion_dict = {}
    conversion_dict["source"] = int(info[1])
    conversion_dict["destination"] = int(info[0])
    conversion_dict["range"] = int(info[2])
    water_to_light_map.append(conversion_dict)

# TEMPERATURE MAP

light_to_temperature_map_lines = segments[5].split(':')[1].strip().split('\n')
light_to_temperature_map = []

for line in light_to_temperature_map_lines:
    info = line.split(' ')
    conversion_dict = {}
    conversion_dict["source"] = int(info[1])
    conversion_dict["destination"] = int(info[0])
    conversion_dict["range"] = int(info[2])
    light_to_temperature_map.append(conversion_dict)

# HUMIDITY MAP

temperature_to_humidity_map_lines = segments[6].split(':')[1].strip().split('\n')
temperature_to_humidity_map = []

for line in temperature_to_humidity_map_lines:
    info = line.split(' ')
    conversion_dict = {}
    conversion_dict["source"] = int(info[1])
    conversion_dict["destination"] = int(info[0])
    conversion_dict["range"] = int(info[2])
    temperature_to_humidity_map.append(conversion_dict)

# LOCATION MAP

humidity_to_location_map_lines = segments[7].split(':')[1].strip().split('\n')
humidity_to_location_map = []

for line in humidity_to_location_map_lines:
    info = line.split(' ')
    conversion_dict = {}
    conversion_dict["source"] = int(info[1])
    conversion_dict["destination"] = int(info[0])
    conversion_dict["range"] = int(info[2])
    humidity_to_location_map.append(conversion_dict)


#Check soil destination

soil_numbers = []

def convert_seed_to_soil(list_of_seed_tuples):
    new_seeds = []
    for seed_tuple in list_of_seed_tuples:
        for soil in seed_to_soil_map:
            if seed_tuple[0] >= soil["source"] and seed_tuple[0] < soil["source"] + soil["range"]:
                diff = seed_tuple[0] - soil["source"]
                soil_numbers.append(soil["destination"] + diff)
                if seed_tuple[0] + seed_tuple[1] > soil["source"] + soil["range"]:
                    first_out_of_range = soil["source"] + soil["range"]+1
                    range_of_seeds_oor = seed_tuple[0] + seed_tuple[1] - soil["source"] + soil["range"]
                    new_seed_tuple = (first_out_of_range,range_of_seeds_oor)
                    new_seeds.append(new_seed_tuple)
                break
            else:
                soil_numbers.append(seed_tuple[0])
    if len(new_seeds) > 0:
        return new_seeds
    else:
        return 0


def convert(seed_tuple):
    # number = 0
    # for soil in seed_to_soil_map:
    #     if seed_tuple[0] >= soil["source"] and seed_tuple[0] < soil["source"] + soil["range"]:
    #         diff = seed_tuple[0] - soil["source"]
    #         number = soil["destination"] + diff
    #         if seed_tuple[0] + seed_tuple[1] > soil["source"] + soil["range"]:
    #             new_seeds.append((soil["source"] + soil["range"]+1,seed_tuple[0] + seed_tuple[1] - soil["source"] + soil["range"]))
    #         # print(f'sourcenum: {soil["source"]}')
    #         # print(f'number after soil: {number}')
    #         break
    for fert in soil_to_fertilizer_map:
        if number >= fert["source"] and number < fert["source"] + fert["range"]:
            diff = number - fert["source"]
            number = fert["destination"] + diff
            # print(f'sourcenum: {fert["source"]}')
            # print(f'number after fert: {number}')
            break
    for water in fertilizer_to_water_map:
        if number >= water["source"] and number < water["source"] + water["range"]:
            diff = number - water["source"]
            number = water["destination"] + diff
            # print(f'sourcenum: {water["source"]}')
            # print(f'number after water: {number}')
            break
    for light in water_to_light_map:
        if number >= light["source"] and number < light["source"] + light["range"]:
            diff = number - light["source"]
            number = light["destination"] + diff
            # print(f'sourcenum: {light["source"]}')
            # print(f'number after light: {number}')
            break
    for temp in light_to_temperature_map:
        if number >= temp["source"] and number < temp["source"] + temp["range"]:
            diff = number - temp["source"]
            number = temp["destination"] + diff
            # print(f'sourcenum: {temp["source"]}')
            # print(f'number after temp: {number}')
            break
    for humid in temperature_to_humidity_map:
        if number >= humid["source"] and number < humid["source"] + humid["range"]:
            diff = number - humid["source"]
            number = humid["destination"] + diff
            # print(f'sourcenum: {humid["source"]}')
            # print(f'number after humid: {number}')
            break
    for location in humidity_to_location_map:
        if number >= location["source"] and number < location["source"] + location["range"]:
            diff = number - location["source"]
            number = location["destination"] + diff
            # print(f'sourcenum: {location["source"]}')
            # print(f'number after location: {number}')
            break
    locations.append(number)

test_seed_tuple = (104847962, 3583832)

input_list = []


newseeds = convert_seed_to_soil(seed_tuples) #3
print(f'len soil numbers: {len(soil_numbers)}')
# while newseeds:
#     newseeds = convert_seed_to_soil(newseeds)

newseeds = convert_seed_to_soil(newseeds) #2
newseeds = convert_seed_to_soil(newseeds) #2
newseeds = convert_seed_to_soil(newseeds) #2
newseeds = convert_seed_to_soil(newseeds) #1
newseeds = convert_seed_to_soil(newseeds) #1
newseeds = convert_seed_to_soil(newseeds) #1
newseeds = convert_seed_to_soil(newseeds) #1
newseeds = convert_seed_to_soil(newseeds) #0

# I ALT 13 nye seeds

print('----')
#print(f'new seeds: {len(newseeds)}')
print(f'len soil numbers: {len(soil_numbers)}')

# print(f'Length before new seeds: {len(locations)}')
# for seed in new_seeds:
#     convert(seed)
# print(f'Length after new seeds: {len(locations)}')

#convert(test_seed_tuple)

#locations.sort()
#print(locations)
#print(new_seeds)