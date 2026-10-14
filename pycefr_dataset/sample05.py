# Synthetic Python sample 05; intended focus: A1.

items = ["pen", "book", "bag"]
for index, item in enumerate(items):
    if index % 2 == 0:
        print(index, item)

values = [3, 8, 2, 9, 5, 11]

def label_value(value):
    return "large" if value > 5 else "small"

print("label", label_value(7))
def remove_outliers(numbers):
    if len(numbers) < 3:
        return list(numbers)
    ordered = sorted(numbers)
    low = ordered[0]
    high = ordered[-1]
    filtered = [number for number in numbers if low < number < high]
    return filtered if filtered else list(numbers)

print("trimmed", remove_outliers(values))
