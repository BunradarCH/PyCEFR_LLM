# Synthetic Python sample 03; intended focus: A1.

prices = [12, 7, 20, 4]
total = 0
for price in prices:
    total += price
    if price > 10:
        print("premium", price)
print("total", total)

values = [3, 8, 2, 9, 5, 11]

def label_value(value):
    return "large" if value > 5 else "small"

print("label", label_value(7))
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
