import re
f = open("6-input.txt", "r")
data = f.readlines()

time = int(re.sub(r'\D','',data[0]))
distance = int(re.sub(r'\D','',data[1]))

result = 1
num_of_winning_hold_times = []

count = 0
for j in range(time):
    distance_travelled = j*(time-j)
    if distance_travelled > distance:
        count += 1

print(count)

