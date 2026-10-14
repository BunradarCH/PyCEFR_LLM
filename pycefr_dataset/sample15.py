# Synthetic Python sample 15; intended focus: B1.

values = [3, 8, 2, 9, 5, 11]
print("input values", values)

for value in values:
    if value % 2 == 0:
        print("even", value)

def describe(values):
    return [(value, "even" if value % 2 == 0 else "odd") for value in values]

print(describe(values))
def pairwise_differences(values):
    result = []
    for left, right in zip(values, values[1:]):
        result.append(right - left)
    return result

print(pairwise_differences(values))
def rolling_totals(numbers):
    running = 0
    result = []
    for number in numbers:
        running += number
        result.append(running)
    return result

print("rolling totals", rolling_totals(values))
