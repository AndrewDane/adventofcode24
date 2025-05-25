import os
import re

print(os.getcwd())
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

# pt 2

do_exp = r"do\(\)"
dont_exp = r"don't\(\)"


# capture lines of dos and donts by using do_dont_line_exp to create a list of string lines. then parse each group like in pt 1 or discard. the first few mul elements get executed as there is no don't prior to it
def find_do_dont_line(input):
    do_dont_line_exp = r"(?:do\(\)).*?(?:don't\(\))"
    command_lines = re.findall(do_dont_line_exp, input)
    return command_lines


def find_prefix_line(input):
    prefix = r"(^.*?(do\(\)))"
    prefix_line = re.findall(prefix, input)
    return prefix_line


print(find_do_dont_line(puzzle_input))
res = [search_and_multiply(line) for line in find_do_dont_line(puzzle_input)]
# 1128698544 - too high, 2821746360 - even higher though i used a correct regex, but i was using total input. now it's here: 71339374 but this is missing the prefix line of the input prior to the first do. 71563420 - too low
print(find_prefix_line(puzzle_input))
res.append(search_and_multiply(find_prefix_line(puzzle_input)[0][0]))
print(sum(res))
