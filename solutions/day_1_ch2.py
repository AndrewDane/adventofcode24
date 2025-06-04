# advent of code pt 2

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


def is_ascending(report: list) -> bool:
    if report != sorted(report):
        return False
    for i in range(len(report) - 1):
        if report[i + 1] is None:
            break
        elif report[i] < report[i + 1]:
            continue
        else:
            return False
    return True


def is_descending(report: list) -> bool:
    if report != sorted(report, reverse=True):
        return False
    for i in range(len(report) - 1):
        if report[i + 1] is None:
            break
        elif report[i] > report[i + 1]:
            continue
        else:
            return False
    return True


def has_duplicates(report: list) -> bool:
    report_set = set()
    for level in report:
        if level in report_set:
            return True
        else:
            report_set.add(level)
    return False


# Tests
is_ascending([34, 35, 38, 39, 42, 48])
has_duplicates([34, 35, 38, 39, 42, 48])
is_descending([84, 83, 81, 79, 78])
# sort out duplicates, append ascending to a separate list, and create a copy of the remainder
asc_reports: list = []
desc_reports: list = []
for report in reports[:]:
    if is_ascending(report) and not has_duplicates(report):
        asc_reports.append(report)
    elif is_descending(report) and not has_duplicates(report):
        desc_reports.append(report)
desc_reports
len(asc_reports)
len(desc_reports)


def diff_bw_two_levels(report: list) -> bool:
    for i in range(len(report) - 1):
        if report[i + 1] is None:
            break
        diff = abs(report[i] - report[i + 1])
        if 1 < diff > 3:
            return False
    return True


asc_count = 0
desc_count: int = 0
for report in asc_reports:
    if diff_bw_two_levels(report):
        asc_count += 1
for report in desc_reports:
    if diff_bw_two_levels(report):
        desc_count += 1

asc_count + desc_count
diff_bw_two_levels([83, 76, 74, 71, 68, 67, 63])
