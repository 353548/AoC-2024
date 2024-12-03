def is_monotonic(report):
    if report == sorted(report):
        return True
    elif report == sorted(report, reverse=True):
        return True
    else:
        return False

def good_diff(report):
    for l in range(1, len(report)):
        if abs(report[l - 1] - report[l]) not in [1, 2, 3]:
            return False
    return True

def is_safe(report):
    if is_monotonic(report) and good_diff(report):
        return True
    else:
        for l in range(len(report)):
            temp_level = report.copy()
            temp_level.pop(l)
            if is_monotonic(temp_level) and good_diff(temp_level):
                return True
        return False
    

with open('input.txt', 'r') as f:
    reports = [list(map(int, levels.strip().split())) for levels in f.readlines()]

reports = [report for report in reports if is_safe(report)]

x = '1 3 6 7 9'
x = list(map(int, x.strip().split()))
x = is_safe(x)
print(len(reports))