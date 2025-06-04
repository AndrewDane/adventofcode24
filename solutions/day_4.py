import re
import numpy as np

# open the file and preprocess data
with open("input/fourth.txt", "r", encoding="utf-8") as file:
    input = file.readlines()

# rid of \n
lines = []
for line in input:
    lines.append(line.removesuffix("\n"))

# 1x140 array
# [] search each line with regex
xmas_pattern = r"XMAS"
samx_pattern = r"SAMX"


def find_xmas_line(line):
    match = re.findall(xmas_pattern, line)
    return len(match)


total_xmas_line = 0
for line in lines:
    total_xmas_line += find_xmas_line(line)


def find_samx_line(line):
    match = re.findall(samx_pattern, line)
    return len(match)


total_samx_line = 0
for line in lines:
    total_samx_line += find_samx_line(line)
print(total_xmas_line)  # 216
print(total_samx_line)  # 211
# INFO 216 + 211

# [x] Search each column up and down. how?

# [x] make 140x140 array for extracting diagonals with numpy
lines = [list(line) for line in lines]


matrix = np.array(lines)
columns = ["".join(matrix[:, i]) for i in range(matrix.shape[1])]
total_samx_col = 0
total_xmas_col = 0

for line in columns:
    total_samx_col += find_samx_line(line)
    total_xmas_col += find_xmas_line(line)
print(total_xmas_col + total_samx_col)

# [] search each diagonal se, sw, ne, nw
# offset=-1 matrix.diagonal


def get_diagonals_3_or_more(matrix):
    rows, cols = matrix.shape
    diagonals = []

    # ↘ direction: top-left to bottom-right
    for offset in range(-rows + 3, cols - 2):  # Ensure len ≥ 3
        diag = matrix.diagonal(offset=offset)
        if len(diag) >= 3:
            diagonals.append("".join(diag))

    # ↙ direction: top-right to bottom-left
    flipped = np.fliplr(matrix)  # Flip left-right
    for offset in range(-rows + 3, cols - 2):
        diag = flipped.diagonal(offset=offset)
        if len(diag) >= 3:
            diagonals.append("".join(diag))

    return diagonals


diagonals = get_diagonals_3_or_more(matrix)

total_xmas_diag = 0
total_samx_diag = 0

for line in diagonals:
    total_xmas_diag += find_xmas_line(line)
    total_samx_diag += find_samx_line(line)
print(total_samx_diag + total_xmas_diag)
# [] write 8 functions that will do the search. alternatively, use regex for some of them.

# use regex or individual characters? Proly regex. Then, how do I extract diagonals?
