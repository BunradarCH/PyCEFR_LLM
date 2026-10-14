# Synthetic Python sample 28; intended focus: C2.

values = [3, 8, 2, 9, 5, 11]
print("input values", values)

for value in values:
    if value % 2 == 0:
        print("even", value)

def normalize(values):
    maximum = max(values) if values else 1
    return [value / maximum for value in values]

print(normalize(values))
from functools import singledispatch

@singledispatch
def render(value):
    return repr(value)

@render.register
def _(value: int):
    return f"integer:{value}"

@render.register
def _(value: list):
    return "list:" + ",".join(map(str, value))

print(render(5), render([1, 2, 3]))
def moving_average(values, window=2):
    if window <= 0:
        raise ValueError("window must be positive")
    return [sum(values[i:i + window]) / window
            for i in range(len(values) - window + 1)]

print(moving_average(values))
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
