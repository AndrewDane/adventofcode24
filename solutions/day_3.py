# import os
import re

# print(os.getcwd())
with open("input/third.txt", "r", encoding="utf-8") as file:
    puzzle_input = file.read()
print(puzzle_input[0])
puzzle_input.strip("\n")
puzzle_input.strip(" ")


# pt 1
def search_and_multiply(input):
    search_and_multiply_exp = r"mul\(\d+,\d+\)"
    print(puzzle_input)
    res = re.findall(search_and_multiply_exp, input)
    res = [s.removeprefix("mul(").removesuffix(")").split(",") for s in res]
    res = [int(a[0]) * int(a[1]) for a in res]

    return sum(res)


search_and_multiply(puzzle_input)
# 28357231 - too low. 188116424 - right answer
pt2_regex = r"do\(\)|don't\(\)|mul\(\d+,\d+\)"
instructions = re.findall(pt2_regex, puzzle_input)


# pt 2
def process_instructions(instructions):
    is_enabled = True
    total = 0
    for instr in instructions:
        if instr == "do()":
            is_enabled = True
        elif instr == "don't()":
            is_enabled = False
        elif instr.startswith("mul") and is_enabled:
            x, y = map(int, re.findall(r"\d+", instr))
            total += x * y
    return total


result = process_instructions(instructions)
print(result)
