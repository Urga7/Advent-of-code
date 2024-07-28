from collections import Counter

def get_numeric_value(card_rank):
    if card_rank == 'A':
        return 13
    if card_rank == 'K':
        return 12
    if card_rank == 'Q':
        return 11
    if card_rank == 'T':
        return 10
    if card_rank == 'J':
        return 1
    return int(card_rank)

def most_common_card(hand):
    card_counts = Counter(hand)
    most_common = card_counts.most_common(1)
    return most_common[0][0] if most_common else None

allHands = []
winningsSum = 0

line = input()
while line != "":
    handValue = 0
    handWithJ, bet = line.split()
    bet = int(bet)

    for i in range(5):
        handValue += (14**(5 - i)) * get_numeric_value(handWithJ[i])

    numJokers = 0
    for card in handWithJ:
        if card == 'J':
            numJokers += 1

    handWithoutJ = [card for card in handWithJ if card != 'J']
    mostCommon = most_common_card(handWithoutJ)
    if mostCommon is not None:
        for _ in range(numJokers):
            handWithoutJ.append(mostCommon)

    hand = "AAAAA"
    if numJokers != 5:
        hand = handWithoutJ

    valueCounts = Counter(hand)
    counts = sorted(valueCounts.values())
    uniqueValues = len(set(hand))
    handType = 0
    if uniqueValues == 1:
        handType = 7 #Five of a kind
    elif uniqueValues == 2:
        if counts == [2, 3]:
            handType = 5 #Full house
        elif counts == [1, 4]:
            handType = 6 #Four of a kind
    elif uniqueValues == 3:
        if counts == [1, 2, 2]:
            handType = 3  #Two pair
        else:
            handType = 4 #Three of a kind
    elif uniqueValues == 4:
        handType = 2 #One pair
    else:
        handType = 1 #High card

    handValue += handType * (14**6)
    allHands.append((handValue, bet))
    line = input()

sortedHands = sorted(allHands, key=lambda num: num[0])
for k in range(len(sortedHands)):
    winningsSum += (k + 1) * sortedHands[k][1]

print(winningsSum)