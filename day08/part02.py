from math import lcm

instructions = input()
input()

automata = {}
q0 = []
qf = []

line = input()
while line != "":
    key, raw_values = line.split(" = ")
    left, right = raw_values.strip("()").split(", ")
    automata[key] = {'L': left, 'R': right}
    if key[2] == 'A':
        q0.append(key)
    if key[2] == 'Z':
        qf.append(key)

    line = input()

q = q0
steps = []
for i in range(len(q)):
    stepsCounter = 0
    while q[i][2] != 'Z':
        instruction = instructions[stepsCounter % len(instructions)]
        q[i] = automata[q[i]][instruction]
        stepsCounter += 1

    steps.append(stepsCounter)

result = steps[0]
for i in range(1, len(steps)):
    result = lcm(result, steps[i])

print(result)


