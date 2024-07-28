numOfConversions = 7
pairs = [int(seed) for seed in input()[6:].split()]
sources = []
mapped = []
newIntervals = []
for pair in range(len(pairs) >> 1):
    seedStart = pairs[2 * pair]
    seedEnd = pairs[2 * pair + 1] + seedStart - 1
    sources.append((seedStart, seedEnd))

input()
for _ in range(numOfConversions):
    input()

    while True:
        line = input()
        if line == "":
            break

        mapping = [int(num) for num in line.split()]
        mappingDestination = mapping[0]
        mappingStart = mapping[1]
        rangeValue = mapping[2]
        mappingEnd = mappingStart + rangeValue - 1
        delta = mappingDestination - mappingStart

        for pair in sources:
            seedStart, seedEnd = pair
            if seedStart > mappingEnd or seedEnd < mappingStart:
                newIntervals.append((seedStart, seedEnd))
            elif seedStart < mappingStart and seedEnd > mappingEnd:
                newIntervals.append((seedStart, mappingStart - 1))
                mapped.append((mappingStart + delta, mappingEnd + delta))
                newIntervals.append((mappingEnd + 1, seedEnd))
            elif seedStart < mappingStart and seedEnd <= mappingEnd:
                newIntervals.append((seedStart, mappingStart - 1))
                mapped.append((mappingStart + delta, seedEnd + delta))
            elif seedStart >= mappingStart and seedEnd > mappingEnd:
                mapped.append((seedStart + delta, mappingEnd + delta))
                newIntervals.append((mappingEnd + 1, seedEnd))
            elif seedStart >= mappingStart and seedEnd <= mappingEnd:
                mapped.append((seedStart + delta, seedEnd + delta))

        sources.clear()
        sources = newIntervals[:]
        newIntervals.clear()

    for m in mapped:
        sources.append(m)

    mapped.clear()


closestLocation = float('inf')
for location in sources:
    if location[0] < closestLocation:
        closestLocation = location[0]

print(closestLocation)
