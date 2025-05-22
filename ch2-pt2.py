# advent of code day 2 pt 2
from collections import defaultdict

with open("second.txt", "r", encoding="utf-8") as file:
    puzzle_input = file.read()
    # print(repr(puzzle_input[1]))

# from raw puzzle_input, create a list of reports (each line), then to int every level
reports: list = []

raw_reports = puzzle_input.split("\n")
raw_reports[0].split(" ")

reports = [raw_report.split(" ") for raw_report in raw_reports]
reports.pop()
reports = [[int(level) for level in report] for report in reports]
reports[1]
len(reports)
reports


# if report with a strike from has_duplicates, regular logic. Else, special treatment
def is_ascending(report: tuple, strike: int) -> bool:
    if strike == 1:
        if list(report) != sorted(report):
            return False
        for i in range(len(report) - 1):
            if report[i + 1] is None:
                break
            elif report[i] < report[i + 1]:
                continue
            else:
                return False
    elif strike == 0:
        for i in range(len(report) - 1):
            if report[i + 1] is None:
                break
            elif report[i] < report[i + 1]:
                continue
            elif (
                report[i] == report[i + 1] or report[i] > report[i + 1]
            ) and strike == 0:
                strike += 1
                continue
            else:
                return False
    return True


def is_descending(report: tuple, strike: int) -> bool:
    if strike == 1:
        if list(report) != sorted(report, reverse=True):
            return False
        for i in range(len(report) - 1):
            if report[i + 1] is None:
                break
            elif report[i] > report[i + 1]:
                continue
            else:
                return False
    elif strike == 0:
        for i in range(len(report) - 1):
            if report[i + 1] is None:
                break
            elif report[i] > report[i + 1]:
                continue
            elif (
                report[i] == report[i + 1] or report[i] < report[i + 1]
            ) and strike == 0:
                strike += 1
                continue
            else:
                return False
    return True


def has_duplicates(report: list):
    report_set = set()
    strike = 0
    for level in report:
        if level in report_set:
            strike += 1
            if strike > 1:
                return (True, strike)
        else:
            report_set.add(level)
    return (False, strike)


# TODO adjust diff bw two levels to account for strikes 1/0. Thus, is_asc/desc must return a tuple with strikes too that you parse into two new dicts.
def diff_bw_two_levels(report: list) -> bool:
    for i in range(len(report) - 1):
        if report[i + 1] is None:
            break
        diff = abs(report[i] - report[i + 1])
        if 1 < diff > 3:
            return False
    return True


new_candidates = defaultdict()

for report in reports:
    if not has_duplicates(report)[0]:
        new_candidates[tuple(report)] = has_duplicates(report)[1]

len(new_candidates)
new_candidates  # type: ignore
dampened_asc = defaultdict()
dampened_desc = defaultdict()
for candidate, strike in new_candidates.items():
    if is_ascending(candidate, strike):
        dampened_asc[candidate] = is_ascending
    if is_descending(candidate, strike):
        dampened_desc.append(candidate)


# new_candidates
# len(dampened_asc) + len(dampened_desc)
# is_ascending((1, 2, 4, 7, 9, 8), 0)
# is_ascending((53, 50, 49, 49, 46, 43, 40, 39), 1)
# print(is_descending((53, 50, 49, 49, 46, 43, 40, 39), 0))

# subreps = [
#     [18, 19, 20, 22, 23],
#     [73, 70, 67, 65, 63],
#     [76, 79, 80, 83, 84, 87, 90],
#     [61, 58, 55, 53, 51, 49],
#     [20, 21, 24, 26, 29, 30, 32, 34],
#     [30, 34, 34, 34, 38],
#     [31, 33, 35, 36, 37, 40, 41],
#     [66, 64, 64, 61, 60, 58],
#     [3, 6, 9, 10, 12],
#     [96, 95, 94, 93, 90, 89, 86, 83],
#     [34, 31, 29, 27, 25, 24, 23],
#     [32, 29, 28, 25, 22, 21, 19, 18],
#     [66, 63, 60, 57, 56, 54],
# ]
# subcandidates = defaultdict()
# for report in subreps:
#     if not has_duplicates(report)[0]:
#         subcandidates[tuple(report)] = has_duplicates(report)[1]
# subcandidates

# dampened_up = []
# dampened_down = []
# for candidate, strike in subcandidates.items():
#     if is_ascending(candidate, strike):
#         dampened_up.append(candidate)
#     if is_descending(candidate, strike):
#         dampened_down.append(candidate)
# dampened_down
# dampened_up
# [
#     (18, 19, 20, 22, 23),
#     (76, 79, 80, 83, 84, 87, 90),
#     (20, 21, 24, 26, 29, 30, 32, 34),
#     (31, 33, 35, 36, 37, 40, 41),
#     (3, 6, 9, 10, 12),
# ]  # type: ignore
# [
#     (73, 70, 67, 65, 63),
#     (61, 58, 55, 53, 51, 49),
#     (96, 95, 94, 93, 90, 89, 86, 83),
#     (34, 31, 29, 27, 25, 24, 23),
#     (32, 29, 28, 25, 22, 21, 19, 18),
#     (66, 63, 60, 57, 56, 54),
# ]  # type: ignore
