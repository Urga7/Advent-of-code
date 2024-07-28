import re

totalSum = 0
line = input()
cards = [1 for element in range(205)]
index = 0

while line != "":
    info = line[9:]
    numbers_sets = re.split(r'\s*\|\s*', info)
    winningNumbers = list(map(int, numbers_sets[0].split()))
    playerNumbers = list(map(int, numbers_sets[1].split()))

    matchesCount = sum(1 for number in playerNumbers if number in winningNumbers)
    for i in range(matchesCount):
        cards[index + i + 1] += cards[index]

    totalSum += cards[index]
    index += 1
    line = input()

print(totalSum)