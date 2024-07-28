gearSum = 0
matrix = []
line = input()

while line != "":
    matrix.append(list(line))
    line = input()

iMax = len(matrix)
jMax = len(matrix[0])
readingNumber = True
currentNumberId = 1
allNumbers = [[0 for _ in range(jMax)] for _ in range(iMax)]
idToNumber = {}
currentNumber = 0

def numericalNeighbours(i, j):

    numNeighbours = []

    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]

    for dx, dy in directions:
        ni = i + dx
        nj = j + dy

        if 0 <= ni < iMax and 0 <= nj < jMax:
            neighbourId = allNumbers[ni][nj]
            if neighbourId > 0 and neighbourId not in numNeighbours:
                numNeighbours.append(allNumbers[ni][nj])

    return numNeighbours


for i in range(iMax):
    for j in range(jMax):
        if readingNumber:
            if '0' <= matrix[i][j] <= '9':
                currentNumber *= 10
                currentNumber += int(matrix[i][j])
                allNumbers[i][j] = currentNumberId

            else:
                readingNumber = False
                idToNumber[currentNumberId] = currentNumber
                currentNumber = 0
                currentNumberId += 1

        else:
            if '0' <= matrix[i][j] <= '9':
                readingNumber = True
                currentNumber += int(matrix[i][j])
                allNumbers[i][j] = currentNumberId

for i in range(iMax):
    for j in range(jMax):
        if matrix[i][j] == '*':
            neighbours = numericalNeighbours(i, j)
            if len(neighbours) == 2:
                gearSum += idToNumber[neighbours[0]] * idToNumber[neighbours[1]]

print(gearSum)
