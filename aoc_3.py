import re

def is_valid(check):
    return not check.isdigit() and check != '.'

def check_sides(start, end):
    start_s_line = start - 1 if start > 0 else start
    end_s_line = end + 1 if end < len(line) - 1 else end
    # print(line[start_s_line], line[end_s_line])
    ss_valid = any([is_valid(check) for check in [line[start_s_line], line[end_s_line]]])
    if ss_valid:
        # print(int(''.join([char for char in line[start:end+1]])), "side checking valid")
        return int(''.join([char for char in line[start:end+1]]))
    return None

def check_prior(start, end):
    # check prior line
    start_p_line = start - 1 if start > 0 else start
    end_p_line = end + 2 if end < len(line) - 1 else end
    # print([char for char in line[start:end+1]], "checking", lines[index-1][start_p_line:end_p_line])
    p_valid = any([is_valid(check) for check in lines[index-1][start_p_line:end_p_line]])
    if p_valid:
        # print(int(''.join([char for char in line[start:end+1]])), "prior checking valid")
        return int(''.join([char for char in line[start:end+1]]))
    return None

def check_next(start, end):
    # check next line
    start_p_line = start - 1 if start > 0 else start
    end_p_line = end + 2 if end < len(line) - 1 else end
    # print([char for char in line[start:end+1]], "checking", lines[index+1][start_p_line:end_p_line])
    n_valid = any([is_valid(check) for check in lines[index+1][start_p_line:end_p_line]])
    if n_valid:
        # print(int(''.join([char for char in line[start:end+1]])), "next checking valid")
        return int(''.join([char for char in line[start:end+1]]))
    return None



with open("aoc_3.txt") as fp:
    lines = [line.rstrip() for line in fp]

sum = 0
for index, line in enumerate(lines):
    matches = re.finditer(r'(\d+)', line)
    for m in matches:
        start, end = m.start(0), m.end(0) - 1

        if s_valid := check_sides(start, end):
            sum += s_valid

        if index > 0:
            if p_valid := check_prior(start, end):
                sum += p_valid

        if index < len(line) - 1:
            if n_valid := check_next(start, end):
                sum += n_valid

print("Sum:", sum)

