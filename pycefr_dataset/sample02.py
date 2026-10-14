# Synthetic Python sample 02; intended focus: A1.

names = ["Mina", "Kai", "Lina"]
message = "Welcome"
for name in names:
    if len(name) > 3:
        print(message, name)

values = [3, 8, 2, 9, 5, 11]

def label_value(value):
    return "large" if value > 5 else "small"

print("label", label_value(7))
def rolling_totals(numbers):
    running = 0
    result = []
    for number in numbers:
        running += number
        result.append(running)
    return result

print("rolling totals", rolling_totals(values))
