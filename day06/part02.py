line = input()[11:]
times = line.split()
time = 0
for number in times:
    for symbol in number:
        time *= 10
        time += int(symbol)

line = input()[11:]
records = line.split()
record = 0
for number in records:
    for symbol in number:
        record *= 10
        record += int(symbol)

possibleWays = 0
for t in range(time):
    if t * (time - t) > record:
        possibleWays += 1


print(possibleWays)
