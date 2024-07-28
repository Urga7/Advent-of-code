instructions = input()
input()

automata = {}

line = input()
while line != "":
    key, raw_values = line.split(" = ")
    left, right = raw_values.strip("()").split(", ")
    automata[key] = {'L': left, 'R': right}
    line = input()

q0 = "AAA"
qf = "ZZZ"

q = q0
stepsCounter = 0
while q != qf:
    instruction = instructions[stepsCounter % len(instructions)]
    q = automata[q][instruction]
    stepsCounter += 1

print(stepsCounter)


