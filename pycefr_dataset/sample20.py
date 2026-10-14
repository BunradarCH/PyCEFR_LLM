# Synthetic Python sample 20; intended focus: B2.

values = [3, 8, 2, 9, 5, 11]
print("input values", values)

for value in values:
    if value % 2 == 0:
        print("even", value)

def describe(values):
    return [(value, "even" if value % 2 == 0 else "odd") for value in values]

print(describe(values))
def merge_sorted(left, right):
    a = iter(left)
    b = iter(right)
    sentinel = object()
    x, y = next(a, sentinel), next(b, sentinel)
    while x is not sentinel and y is not sentinel:
        if x <= y:
            yield x
            x = next(a, sentinel)
        else:
            yield y
            y = next(b, sentinel)
    if x is not sentinel:
        yield x
    if y is not sentinel:
        yield y
    yield from a
    yield from b

print(list(merge_sorted([1, 4, 7], [2, 3, 9])))
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
