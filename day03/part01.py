sum = 0

matrix = []
line = input()
index = 0

while line != "":
    matrix.append(list(line))
    line = input()

iMax = len(matrix)
jMax = len(matrix[0])
readingNumber = True
currentNumber = 0
includeInSum = False
def nextToSymbol(i, j):
    iMax = len(matrix)
    jMax = len(matrix[0])

    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1), (1, 0), (1, 1)]

    for dx, dy in directions:
        ni = i + dx
        nj = j + dy

        if 0 <= ni < iMax and 0 <= nj < jMax:
            if matrix[ni][nj] != '.' and not matrix[ni][nj].isdigit():
                return True

    return False


for i in range(iMax):
    for j in range(jMax):
        if readingNumber:
            if '0' <= matrix[i][j] <= '9':
                currentNumber *= 10
                currentNumber += int(matrix[i][j])
                if nextToSymbol(i, j):
                    includeInSum = True

            else:
                readingNumber = False
                if includeInSum:
                    sum += currentNumber

                includeInSum = False
                currentNumber = 0

        else:
            if '0' <= matrix[i][j] <= '9':
                readingNumber = True
                currentNumber += int(matrix[i][j])
                if nextToSymbol(i, j):
                    includeInSum = True


print(sum)

