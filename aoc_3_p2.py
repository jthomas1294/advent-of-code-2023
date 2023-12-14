# INCOMPLETE

import re

def is_valid(check):
    return check.isdigit()


def check_sides(line, index):
    left, right = None, None

    l_start = index - 5 if index > 5 else 0
    l_end = index+1 if index < len(line) - 1 else index
    left = re.search(r'(\d+)\*', line[l_start:l_end])
    if left:
        left = int(left.group(1))

    r_start = index
    r_end = index+5 if index+5 < len(line) - 1 else len(line) - 1
    right = re.search(r'\*(\d+)', line[r_start:r_end])
    if right:
        right = int(right.group(1))

    if left and right:
        print(left, right, left * right)
        return None, left * right
    
    return (left or right), None

def check_line(line, index):
    core_string = line[index-1:index+2]
    all_matches = re.findall(r'(\d)', core_string)
    if all_matches:
        # print("all_matches", all_matches)
        offset = 3
        p_start = index-offset if index > offset else 0
        p_end = index+offset if index+offset < len(line)-1 else len(line)-1
        match_string = line[p_start:p_end+1]
        matches = re.finditer(r'(\d{2,3})+', match_string)
        # if matches: print(line[index-1:index+2], matches.groups())
        for m in matches:
            print("check_line", match_string, int(match_string[m.start(0):m.end(0)]))
            return int(match_string[m.start(0):m.end(0)])

    return None



with open("aoc_3.txt") as fp:
    lines = [line.rstrip() for line in fp]

sum = 0
for index, line in enumerate(lines):
    matches = re.finditer(r'(\*+)', line)
    for m in matches:
        start, end = m.start(0), m.end(0) - 1

        left_or_right, sides_product = check_sides(line, start)
        if sides_product:
            sum += sides_product
            print("multiplied sides", sides_product)
            continue

        # print("left_or_right", left_or_right, "sides_product", sides_product)

        prior = check_line(lines[index-1], start)
        if index > 0 and prior and left_or_right:
            product = prior * left_or_right
            sum += product
            print(f"multiplied prior {prior} and left or right {left_or_right}", product)
            continue

        # print("prior", prior, "left_or_right", left_or_right)

        next = check_line(lines[index+1], start)
        if index < len(line)-1 and next and (left_or_right or prior):
            other = left_or_right or prior
            product = next * other
            sum += product
            print(f"multiplied next {next} and prior or left or right {other}", product)
            continue

        # print("next", next, "prior", prior, "left_or_right", left_or_right)

    
    # if index == 10: break

print("Sum:", sum)
