f = open("5-input.txt", "r")
data = f.read()

segments = data.split("\n\n")

locations = []

def str_to_int(str):
    return int(str)

seeds_v1 = list(map(str_to_int,segments[0].split(':')[1].strip().split(' ')))

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

def convert_to_soils(seed_tup):
    soil_numbers = []
    for soil in seed_to_soil_map:
        if seed_tup[0] >= soil["source"] and seed_tup[0] < soil["source"] + soil["range"]:
            diff = seed_tup[0] - soil["source"]
            #check if range should split
            if seed_tup[0] + seed_tup[1] > soil["source"] + soil["range"]: #SPLIT!
                smallest_non_fitting = soil["source"] + soil["range"] + 1
                range_fitting = soil["source"]+soil["range"]-seed_tup[0]
                #check lowest seed beyond split
                soil_numbers.append((soil["destination"]+diff, range_fitting))
                soil_numbers.append((smallest_non_fitting, seed_tup[1]-range_fitting))
            else: #if no split
                soil_numbers.append((soil["destination"] + diff,seed_tup[1]))
            break
    return soil_numbers

def convert_to_fert(soil_tup):
    fert_numbers = []
    for fert in soil_to_fertilizer_map:
        if soil_tup[0] >= fert["source"] and soil_tup[0] < fert["source"] + fert["range"]:
            diff = soil_tup[0] - fert["source"]
            #check if range should split
            if soil_tup[0] + soil_tup[1] > fert["source"] + fert["range"]: #SPLIT!
                smallest_non_fitting = fert["source"] + fert["range"] + 1
                range_fitting = fert["source"]+fert["range"]-soil_tup[0]
                #check lowest seed beyond split
                fert_numbers.append((fert["destination"]+diff, range_fitting))
                fert_numbers.append((smallest_non_fitting, soil_tup[1]-range_fitting))
            else: #if no split
                fert_numbers.append((fert["destination"] + diff,soil_tup[1]))
            break
    return fert_numbers

def convert_to_water(fert_tup):
    water_numbers = []
    for water in fertilizer_to_water_map:
        if fert_tup[0] >= water["source"] and fert_tup[0] < water["source"] + water["range"]:
            diff = fert_tup[0] - water["source"]
            #check if range should split
            if fert_tup[0] + fert_tup[1] > water["source"] + water["range"]: #SPLIT!
                smallest_non_fitting = water["source"] + water["range"] + 1
                range_fitting = water["source"]+water["range"]-fert_tup[0]
                #check lowest seed beyond split
                water_numbers.append((water["destination"]+diff, range_fitting))
                water_numbers.append((smallest_non_fitting, fert_tup[1]-range_fitting))
            else: #if no split
                water_numbers.append((water["destination"] + diff,fert_tup[1]))
            break
    return water_numbers



def convert_to_light(water_tup):
    light_numbers = []
    for light in water_to_light_map:
        if water_tup[0] >= light["source"] and water_tup[0] < light["source"] + light["range"]:
            diff = water_tup[0] - light["source"]
            #check if range should split
            if water_tup[0] + water_tup[1] > light["source"] + light["range"]: #SPLIT!
                smallest_non_fitting = light["source"] + light["range"] + 1
                range_fitting = light["source"]+light["range"]-water_tup[0]
                #check lowest seed beyond split
                light_numbers.append((light["destination"]+diff, range_fitting))
                light_numbers.append((smallest_non_fitting, water_tup[1]-range_fitting))
            else: #if no split
                light_numbers.append((light["destination"] + diff,water_tup[1]))
            break
    return light_numbers

def convert_to_temp(tup):
    numbers = []
    for x in light_to_temperature_map:
        if tup[0] >= x["source"] and tup[0] < x["source"] + x["range"]:
            diff = tup[0] - x["source"]
            #check if range should split
            if tup[0] + tup[1] > x["source"] + x["range"]: #SPLIT!
                smallest_non_fitting = x["source"] + x["range"] + 1
                range_fitting = x["source"]+x["range"]-tup[0]
                #check lowest seed beyond split
                numbers.append((x["destination"]+diff, range_fitting))
                numbers.append((smallest_non_fitting, tup[1]-range_fitting))
            else: #if no split
                numbers.append((x["destination"] + diff,tup[1]))
            break
    return numbers

def convert_to_hum(tup):
    numbers = []
    for x in temperature_to_humidity_map:
        if tup[0] >= x["source"] and tup[0] < x["source"] + x["range"]:
            diff = tup[0] - x["source"]
            #check if range should split
            if tup[0] + tup[1] > x["source"] + x["range"]: #SPLIT!
                smallest_non_fitting = x["source"] + x["range"] + 1
                range_fitting = x["source"]+x["range"]-tup[0]
                #check lowest seed beyond split
                numbers.append((x["destination"]+diff, range_fitting))
                numbers.append((smallest_non_fitting, tup[1]-range_fitting))
            else: #if no split
                numbers.append((x["destination"] + diff,tup[1]))
            break
    return numbers

def convert_to_loc(tup):
    numbers = []
    for x in humidity_to_location_map:
        if tup[0] >= x["source"] and tup[0] < x["source"] + x["range"]:
            diff = tup[0] - x["source"]
            #check if range should split
            if tup[0] + tup[1] > x["source"] + x["range"]: #SPLIT!
                smallest_non_fitting = x["source"] + x["range"] + 1
                range_fitting = x["source"]+x["range"]-tup[0]
                #check lowest seed beyond split
                numbers.append((x["destination"]+diff, range_fitting))
                numbers.append((smallest_non_fitting, tup[1]-range_fitting))
            else: #if no split
                numbers.append((x["destination"] + diff,tup[1]))
            break
    return numbers

seed_tuples = []

for i, seed in enumerate(seeds_v1):
    if i%2 == 0:
        seed_tuples.append((seed,seeds_v1[i+1]))

# # test tups - outcomment ffs!
# seed_tuples = [(79,14), (55,13)]

soil_tuples = []
fert_tuples = []
water_tuples = []
light_tuples = []
temp_tuples = []
hum_tuples = []
loc_tuples = []

# HERTIL!

for tup in seed_tuples:
    soil_results = convert_to_soils(tup)
    for soil_result in soil_results:
        soil_tuples.append(soil_result)

for tup in soil_tuples:
    fert_results = convert_to_fert(tup)
    for fert_result in fert_results:
        fert_tuples.append(fert_result)

for tup in fert_tuples:
    water_results = convert_to_water(tup)
    for water_result in water_results:
        water_tuples.append(water_result)
for tup in water_tuples:
    light_results = convert_to_light(tup)
    for light_result in light_results:
        light_tuples.append(light_result)
for tup in light_tuples:
    temp_results = convert_to_temp(tup)
    for temp_result in temp_results:
        temp_tuples.append(temp_result)
for tup in temp_tuples:
    hum_results = convert_to_temp(tup)
    for hum_result in hum_results:
        hum_tuples.append(hum_result)
for tup in hum_tuples:
    loc_results = convert_to_temp(tup)
    for loc_result in loc_results:
        loc_tuples.append(loc_result)

print(len(seed_tuples))
print(len(soil_tuples))
print(len(fert_tuples))
print(len(water_tuples))
print(len(light_tuples))
print(len(temp_tuples))
print(len(hum_tuples))
print(len(loc_tuples))

def turn_tup_to_num(tup):
    return tup[0]

final_locations = list(map(turn_tup_to_num,loc_tuples))

final_locations.sort()

print(final_locations)



#one_seed_tup = [(104847962, 3583832)]





# 5ight

# for seed in seeds:
#     convert(seed)

# locations.sort()
# print(locations)