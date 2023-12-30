import re

with open("aoc_8.txt") as fp:
    lines = [l.rstrip() for l in fp]

instructions = list(lines[0])
move_legened = {'L': 0, 'R': 1}

network = {}
for line in lines[2:]:
    match = re.search(r"(\w+)\s*=\s*\((\w+),\s*(\w+)\)", line)
    matches = match.groups()
    network[matches[0]] = (matches[1], matches[2])

steps = 0
instruction_num = 0

position = network['AAA']
looking = True
while True:
    # print("position", position)
    next_direction = move_legened[instructions[instruction_num]]
    next = position[next_direction]
    # print("next", next)
    steps += 1

    if next == 'ZZZ':
        break
    else:
        position = network[next]

    instruction_num += 1
    if instruction_num == len(instructions):
        instruction_num = 0

print(steps)