import re

cubes = {"red": 12, "green": 13, "blue": 14}

def get_game_number(line):
    match = re.search(r'Game (\d+):', line)
    return match.group(1), match.end()

def round_is_valid(round):
    matches = re.findall(r'(\d+)\s([red|green|blue]+)+', round)
    for num, color in matches:
        if int(num) > cubes[color]:
            return False
    return True

# sum = 0
# with open("aoc_2.txt") as fp:
#     for line in fp:
#         game_num, str_end = get_game_number(line)
#         rounds = line[str_end:].split(";")
#         round_validity = [round_is_valid(r) for r in rounds]
#         if all(round_validity):
#             sum += int(game_num)

# print("Sum:", sum)

def find_minimum(rounds):
    result = {}
    for round in rounds:
        matches = re.findall(r'(\d+)\s([red|green|blue]+)+', round)
        for num, color in matches:
            if not result.get(color) or int(num) > result[color]:
                result[color] = int(num)
    response = 1
    for num in result.values():
        response *= num
    print(result, response)
    return response

sum = 0
with open("aoc_2.txt") as fp:
    for line in fp:
        game_num, str_end = get_game_number(line)
        rounds = line[str_end:].split(";")
        sum += find_minimum(rounds)

print("Sum:", sum)

