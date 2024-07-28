firstNumbers = []
secondNumbers = []

line = "a"
totalSum = 0

while line != "":
    line = input()
    numbers = []

    for i in range(len(line)):
        c = line[i]
        number = ord(c) - ord('0')

        if 0 <= number <= 9:
            numbers.append((number, i))

        i1 = line.find("one", i)
        if(i1 != -1):
            numbers.append((1, i1))

        i2 = line.find("two", i)
        if(i2 != -1):
            numbers.append((2, i2))

        i3 = line.find("three", i)
        if(i3 != -1):
            numbers.append((3, i3))

        i4 = line.find("four", i)
        if(i4 != -1):
            numbers.append((4, i4))

        i5 = line.find("five", i)
        if(i5 != -1):
            numbers.append((5, i5))

        i6 = line.find("six", i)
        if(i6 != -1):
            numbers.append((6, i6))

        i7 = line.find("seven", i)
        if(i7 != -1):
            numbers.append((7, i7))

        i8 = line.find("eight", i)
        if(i8 != -1):
            numbers.append((8, i8))

        i9 = line.find("nine", i)
        if(i9 != -1):
            numbers.append((9, i9))

    firstIndex = 99999999
    first = 0
    lastIndex = -1
    last = 0
    for pair in numbers:
        if pair[1] > lastIndex:
            lastIndex = pair[1]
            last = pair[0]

        if pair[1] < firstIndex:
            firstIndex = pair[1]
            first = pair[0]

    firstNumbers.append(first)
    secondNumbers.append(last)

for i in range(len(firstNumbers) - 1):
    print(firstNumbers[i], secondNumbers[i])
    totalSum += firstNumbers[i] * 10 + secondNumbers[i]

print(totalSum, '\n')