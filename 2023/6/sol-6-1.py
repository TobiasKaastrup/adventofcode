import re
f = open("6-input.txt", "r")
data = f.readlines()

times = re.findall(r'\d+',data[0])
distances = re.findall(r'\d+',data[1])

result = 1
num_of_winning_hold_times = []

for i in range(4):
    count = 0
    time = int(times[i])
    distance = int(distances[i])

    print('------')

    for j in range(time):
        distance_travelled = j*(time-j)
        if distance_travelled > distance:
            count += 1
            print(f'Holding {j} seconds takes you {distance_travelled} out of {distance}')
    num_of_winning_hold_times.append(count)

for race in num_of_winning_hold_times:
    result *= race

print(result)
# def check_distance_from_speed(hold_time, total_time, record_distance):
#     if hold_time

