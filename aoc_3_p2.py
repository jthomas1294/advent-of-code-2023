import re

def is_valid(check):
    return check.isdigit()

# def check_sides(start, end):
#     start_s_line = start - 1 if start > 0 else start
#     end_s_line = end + 1 if end < len(line) - 1 else end
#     # print(line[start_s_line], line[end_s_line])
#     ss_valid = any([is_valid(check) for check in [line[start_s_line], line[end_s_line]]])
#     if ss_valid:
#         # print(int(''.join([char for char in line[start:end+1]])), "side checking valid")
#         return int(''.join([char for char in line[start:end+1]]))
#     return None

def check_sides(line, index):
    l_start = index - 5 if index > 5 else 0
    l_end = index+1 if index < len(line) - 1 else index
    left = re.search(r'(\d+)\*', line[l_start:l_end])
    if left: print(left.group(1))

    r_start = index
    r_end = index+5 if index+5 < len(line) - 1 else len(line) - 1
    right = re.search(r'\*(\d+)', line[r_start:r_end])
    if right: print(right.group(1))

    if left and right:
        print(left.group(1), right.group(1), int(left.group(1)) * int(right.group(1)))
        return int(left.group(1)) * int(right.group(1))
    
    return 0

# def check_prior(start, end):
#     # check prior line
#     start_p_line = start - 1 if start > 0 else start
#     end_p_line = end + 2 if end < len(line) - 1 else end
#     # print([char for char in line[start:end+1]], "checking", lines[index-1][start_p_line:end_p_line])
#     p_valid = any([is_valid(check) for check in lines[index-1][start_p_line:end_p_line]])
#     if p_valid:
#         # print(int(''.join([char for char in line[start:end+1]])), "prior checking valid")
#         return int(''.join([char for char in line[start:end+1]]))
#     return None

def check_prior(line, index):
    # start = index - 5 if index > 5 else 0
    # end = index+5 if index+5 < len(line) - 1 else len(line) - 1
    matches = re.finditer(r'(\d)', line[index-1:index+2])
    # if matches: print(line[index-1:index+2], matches.groups())
    for m in matches:
        start, end = m.start(0), m.end(0) - 1

# def check_next(start, end):
#     # check next line
#     start_p_line = start - 1 if start > 0 else start
#     end_p_line = end + 2 if end < len(line) - 1 else end
#     # print([char for char in line[start:end+1]], "checking", lines[index+1][start_p_line:end_p_line])
#     n_valid = any([is_valid(check) for check in lines[index+1][start_p_line:end_p_line]])
#     if n_valid:
#         # print(int(''.join([char for char in line[start:end+1]])), "next checking valid")
#         return int(''.join([char for char in line[start:end+1]]))
#     return None



with open("aoc_3.txt") as fp:
    lines = [line.rstrip() for line in fp]

sum = 0
for index, line in enumerate(lines):
    matches = re.finditer(r'(\*+)', line)
    for m in matches:
        start, end = m.start(0), m.end(0) - 1

        sum += check_sides(line, start)

        if index > 0:
            check_prior(lines[index-1], start)
    
    if index == 5: break

print("Sum:", sum)

