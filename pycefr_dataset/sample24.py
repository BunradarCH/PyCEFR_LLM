# Synthetic Python sample 24; intended focus: C1.

values = [3, 8, 2, 9, 5, 11]
print("input values", values)

for value in values:
    if value % 2 == 0:
        print("even", value)

def unique_sorted(values):
    return sorted(set(values))

print(unique_sorted(values))
from collections.abc import Iterable

def flatten(tree):
    for item in tree:
        if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
            yield from flatten(item)
        else:
            yield item

nested = [1, [2, [3, 4]], 5]
print(list(flatten(nested)))
from collections import defaultdict

def group_by_parity(values):
    groups = defaultdict(list)
    for value in values:
        groups["even" if value % 2 == 0 else "odd"].append(value)
    return dict(groups)

print(group_by_parity(values))
def count_categories(numbers):
    counts = {"negative": 0, "zero": 0, "positive": 0}
    for number in numbers:
        if number < 0:
            counts["negative"] += 1
        elif number == 0:
            counts["zero"] += 1
        else:
            counts["positive"] += 1
    return counts

print("categories", count_categories(values))
def remove_outliers(numbers):
    if len(numbers) < 3:
        return list(numbers)
    ordered = sorted(numbers)
    low = ordered[0]
    high = ordered[-1]
    filtered = [number for number in numbers if low < number < high]
    return filtered if filtered else list(numbers)

print("trimmed", remove_outliers(values))
def make_report(numbers):
    report = []
    for position, number in enumerate(numbers, start=1):
        status = "above average" if number > sum(numbers) / len(numbers) else "at or below average"
        report.append({"position": position, "value": number, "status": status})
    return report

for record in make_report(values):
    print("report", record)
