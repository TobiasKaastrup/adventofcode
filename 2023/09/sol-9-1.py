f = open("9-input.txt","r")
lines = f.readlines()

histories = []

for line in lines:
    history = list(map(int, line.split(" ")))
    histories.append(history)
    print(history)

extrapolations = []

def get_sequence(history):
    sequence =[]
    for i in range(len(history)-1):
        sequence.append(history[i+1]-history[i])
    return sequence

def get_all_sequences(history):
    new_seq = get_sequence(history)
    input_and_all_seqs = [history,new_seq]
    while new_seq.count(0) != len(new_seq) and len(new_seq) != 1:
        new_seq = get_sequence(new_seq)
        input_and_all_seqs.append(new_seq)
    return input_and_all_seqs

def extrapolate(sequence):
    sequence.reverse()
    sequence[0].append(0)
    for i, seq in enumerate(sequence):
        if i == 0:
            continue
        sequence[i].append(sequence[i-1][-1]+sequence[i][-1])
    sequence.reverse()
    result = sequence[0][-1]
    extrapolations.append(result)

#first_seq = [[-7, -13, -20, -17, 16, 108, 297, 630, 1163, 1961, 3098, 4657, 6730, 9418, 12831, 17088, 22317, 28655, 36248, 45251, 55828], [-6, -7, 3, 33, 92, 189, 333, 533, 798, 1137, 1559, 2073, 2688, 3413, 4257, 5229, 6338, 7593, 9003, 10577], [-1, 10, 30, 59, 97, 144, 200, 265, 339, 422, 514, 615, 725, 844, 972, 1109, 1255, 1410, 1574], [11, 20, 29, 38, 47, 56, 65, 74, 83, 92, 101, 110, 119, 128, 137, 146, 155, 164], [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

first_history = [-7, -13, -20, -17, 16, 108, 297, 630, 1163, 1961, 3098, 4657, 6730, 9418, 12831, 17088, 22317, 28655, 36248, 45251, 55828, 68152]
for history in histories:
    all_seq = get_all_sequences(history)
    extrapolate(all_seq)

sum = 0
for value in extrapolations:
    sum += value

print(sum)