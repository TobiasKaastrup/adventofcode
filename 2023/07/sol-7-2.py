f = open("7-input.txt",'r')
hands = f.readlines()

card_ranks = "J23456789TQKA"

def hand_cleaner(hand):
    cards = hand.split(' ')[0]
    bid = int(hand.split(' ')[1].strip())
    return (cards,bid)

def get_card_rank(card):
    return card_ranks.find(card)


def find_hand_type(hand):

    jokers = hand.count("J")
    hand = hand.replace("J","")

    #Check if 5 of a kind
    if len(set(hand)) == 1 or len(set(hand)) == 0:
        return 7

    #Check if 4 of a kind
    if hand.count(hand[0])+jokers == 4 or hand.count(hand[1])+jokers == 4:
        return 6

    # #Check if full house
    if len(set(hand)) == 2:
        return 5

    # #Check if 3 of a kind
    if hand.count(hand[0])+jokers == 3 or hand.count(hand[1])+jokers == 3 or hand.count(hand[2])+jokers == 3:
        return 4

    # Check if two pairs
    if len(set(hand)) == 3:
        return 3

    # #Check if 1 pair
    if len(set(hand)) == 4:
        return 2

    # Check if high card
    if len(set(hand)) == 5:
        return 1
    
    return 0

def compare_hands(hand):
    return find_hand_type(hand[0])

def compare_card1(hand):
    return get_card_rank(hand[0][0])
def compare_card2(hand):
    return get_card_rank(hand[0][1])
def compare_card3(hand):
    return get_card_rank(hand[0][2])
def compare_card4(hand):
    return get_card_rank(hand[0][3])
def compare_card5(hand):
    return get_card_rank(hand[0][4])

def sum_scores(hands):
    total_winnings = 0
    for i, value in enumerate(hands):
        total_winnings += (i+1)*value[1]
    return total_winnings

sample_hands = ["49A49 734","67594 467","Q2429 453"]

hands_clean = list(map(hand_cleaner,hands))

hands_clean.sort(key=compare_card5)
hands_clean.sort(key=compare_card4)
hands_clean.sort(key=compare_card3)
hands_clean.sort(key=compare_card2)
hands_clean.sort(key=compare_card1)
hands_clean.sort(key=compare_hands)

print(hands_clean)
print(sum_scores(hands_clean))
