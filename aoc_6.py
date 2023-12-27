# with open("aoc_6.txt") as fp:
#     lines = [l.rstrip() for l in fp]

# times = lines[0].split()[1:]
# distances = lines[1].split()[1:]

# total = 1
# for i, time in enumerate(times):
#     num_breaking = 0
#     for t in range(1,int(time)+1):
#         remaining_time = int(time) - t
#         distance = t * remaining_time
#         if distance > int(distances[i]):
#             num_breaking += 1
#     total *= num_breaking

# print("PART TWO asnwer:", total)


############ PART TWO

with open("aoc_6.txt") as fp:
    lines = [l.rstrip() for l in fp]

time = "".join(lines[0].split()[1:])
record_distance = "".join(lines[1].split()[1:])

num_breaking = 0
for t in range(1,int(time)+1):
    remaining_time = int(time) - t
    dist = t * remaining_time
    if dist > int(record_distance):
        num_breaking += 1

print("PART TWO asnwer:", num_breaking)
