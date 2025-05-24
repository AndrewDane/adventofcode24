import os

current_dir = os.getcwd()
input_path = os.path.join(current_dir, "input/second.txt")
with open(input_path, "r", encoding="utf-8") as file:
    puzzle_input = file.read()

reports = puzzle_input.split("\n")
reports.pop()


def is_safe(report: list[int]):
    differentials = [a - b for a, b in zip(report, report[1:])]
    is_mono = all(i > 0 for i in differentials) or all(i < 0 for i in differentials)
    is_in_range = all(0 < abs(i) <= 3 for i in differentials)
    if is_mono and is_in_range:
        return True
    return False


safe = 0
for report in reports:
    levels = [*map(int, report.split())]
    if is_safe(levels):
        safe += 1
    else:
        for i in range(len(levels)):
            tolerated_levels = levels[:i] + levels[i + 1 :]
            if is_safe(tolerated_levels):
                safe += 1
                break
print(safe)
