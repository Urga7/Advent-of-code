sequences = []
line = input()
iteration = 0

while line != "":
    sequenceIndex = 0
    sequences.append([])
    sequences[iteration].append([int(num) for num in line.split()])
    allZeros = False
    while not allZeros:
        sequences[iteration].append([])
        allZeros = True
        for i in range(len(sequences[iteration][sequenceIndex]) - 1):
            newNum = sequences[iteration][sequenceIndex][i + 1] - sequences[iteration][sequenceIndex][i]
            sequences[iteration][sequenceIndex + 1].append(newNum)
            if newNum != 0:
                allZeros = False

        sequenceIndex += 1

    line = input()
    iteration += 1

totalSum = 0
for sequence in sequences:
    iterationSum = 0
    sequence.reverse()
    for line in sequence:
        iterationSum = line[0] - iterationSum

    totalSum += iterationSum

print(totalSum)


