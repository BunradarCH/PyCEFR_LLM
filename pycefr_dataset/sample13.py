# Synthetic Python sample 13; intended focus: B1.

values = [3, 8, 2, 9, 5, 11]
print("input values", values)

for value in values:
    if value % 2 == 0:
        print("even", value)

def normalize(values):
    maximum = max(values) if values else 1
    return [value / maximum for value in values]

print(normalize(values))
def moving_average(values, window=2):
    if window <= 0:
        raise ValueError("window must be positive")
    return [sum(values[i:i + window]) / window
            for i in range(len(values) - window + 1)]

print(moving_average(values))
def remove_outliers(numbers):
    if len(numbers) < 3:
        return list(numbers)
    ordered = sorted(numbers)
    low = ordered[0]
    high = ordered[-1]
    filtered = [number for number in numbers if low < number < high]
    return filtered if filtered else list(numbers)

print("trimmed", remove_outliers(values))
