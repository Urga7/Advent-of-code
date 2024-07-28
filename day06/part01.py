line = input()[11:]
times = [int(number) for number in line.split()]
line = input()[11:]
records = [int(number) for number in line.split()]
totalProduct = 1

for i in range(len(times)):
    possibleWays = 0
    for time in range(times[i]):
        if time * (times[i] - time) > records[i]:
            possibleWays += 1

    totalProduct *= possibleWays

print(totalProduct)
