import re

line = input()
powerSum = 0
while line != "":
    match = re.match(r"Game (\d+):", line)
    gameId = int(match.group(1))
    cubeInfo = line[8:]
    rounds = cubeInfo.split(";")
    regex = "\d{1,2}|red|green|blue"

    red = 0;
    green = 0;
    blue = 0;
    for i in range(len(rounds)):
        tokens = re.findall(regex, rounds[i])

        for j in range(0, len(tokens), 2):
            value = int(tokens[j])
            color = tokens[j + 1][0]

            if color == "r" and value > red:
                red = value

            if color == "g" and value > green:
                green = value

            if color == "b" and value > blue:
                blue = value

    powerSum += red * green * blue

    line = input()


print(powerSum)