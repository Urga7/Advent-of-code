sources = [int(seed) for seed in input()[6:].split()]
numSources = len(sources)
mapped = []
numOfConversions = 7

input()
for _ in range(numOfConversions):
    input()

    while True:
        line = input()
        if line == "":
            break

        mapping = [int(num) for num in line.split()]
        destinationStart = mapping[0]
        sourceStart = mapping[1]
        rangeValue = mapping[2]
        delta = destinationStart - sourceStart

        for source in sources[:]:
            if sourceStart <= source <= sourceStart + rangeValue:
                mapped.append(source + delta)
                sources.remove(source)

    for m in mapped:
        sources.append(m)

    mapped.clear()

closestLocation = float('inf')
for location in sources:
    if location < closestLocation:
        closestLocation = location

print(closestLocation)
