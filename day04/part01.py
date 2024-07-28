import re

totalSum = 0
line = input()
while line != "":
    info = line[9:]
    numbers_sets = re.split(r'\s*\|\s*', info)
    winningNumbers = list(map(int, numbers_sets[0].split()))
    playerNumbers = list(map(int, numbers_sets[1].split()))
    matchesCount = sum(1 for number in playerNumbers if number in winningNumbers)
    totalSum += ((1 << matchesCount) >> 1)
    line = input()

print(totalSum)