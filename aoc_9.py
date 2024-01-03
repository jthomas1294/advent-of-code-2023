
with open("aoc_9.txt") as fp:
    lines = [l.rstrip().split() for l in fp]

sum = 0

for line in lines:
    forward_iterations = []

    current = [int(n) for n in line]
    forward_iterations.append(current)

    while not all([n == 0 for n in current]):
        if len(current) > 1:
            new_current = [current[i+1]-current[i] for i in range(len(current)-1)]
            current = new_current
        else:
            current = [0]
        forward_iterations.append(current)

    # print("before", forward_iterations)

    forward_iterations.reverse()
    for i in range(len(forward_iterations)-1):
        num = forward_iterations[i][-1]
        diff = forward_iterations[i+1][-1]
        forward_iterations[i+1].append(num + diff)

    # print("after", forward_iterations)
    # print("final", forward_iterations[-1][-1])
    sum += forward_iterations[-1][-1]

print("final sum", sum)



############ PART 2

sum = 0
for line in lines:
    forward_iterations = []

    current = [int(n) for n in line]
    forward_iterations.append(current)

    while not all([n == 0 for n in current]):
        if len(current) > 1:
            new_current = [current[i+1]-current[i] for i in range(len(current)-1)]
            current = new_current
        else:
            current = [0]
        forward_iterations.append(current)

    # print("before", forward_iterations)

    forward_iterations.reverse()
    for i in range(len(forward_iterations)-1):
        diff = forward_iterations[i][0]
        num = forward_iterations[i+1][0]
        forward_iterations[i+1].insert(0, num - diff)

    # print("after", forward_iterations)
    # print("final", forward_iterations[-1][0])
    sum += forward_iterations[-1][0]

print("final sum", sum)