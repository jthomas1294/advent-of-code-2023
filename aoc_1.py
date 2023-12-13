import re

def find_int_digit(line, reverse=False):
    line = line[::-1] if reverse else line
    for char in line:
        if char.isdigit():
            return char

def find_digit(line):
    results = {}
    digits = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
              "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
    for d in digits.keys():
        indices_object = re.finditer(pattern=d, string=line)
        indices = [index.start() for index in indices_object]
        for index in indices:
            results[index] = d
    keys = list(results.keys())
    keys.sort()
    return f"{digits[results[keys[0]]]}{digits[results[keys[-1]]]}"

sum = 0
with open("doc.txt") as fp:
    for line in fp:
        print(line)
        line = line.rstrip()
        res = find_digit(line)
        # a = find_digit(line)
        # b = find_digit(line, reverse=True)
        # print(int(a+b))
        sum += int(res)

print("Sum:", sum)
