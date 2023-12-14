import re

sum = 0
count = 0
with open("aoc_4.txt") as fp:
    for line in fp:
        line = line.rstrip()

        winning_matches = re.search(r':\s+(.+?)\s+\|', line)
        winning_nums = winning_matches.group(1).split()
        print(winning_nums)

        having_matches = re.search(r'\|\s+(.+)', line)
        having_nums = having_matches.group(1).split()
        print(having_nums)

        won_nums = set(having_nums).intersection(set(winning_nums))
        print(won_nums)
        if won_nums:
            num = 1
            for i in range(len(won_nums)-1):
                num *= 2
            sum += num

        # count += 1
        # if count == 3: break

print("Sum:", sum)
