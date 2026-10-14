# Synthetic Python sample 08; intended focus: A2.

values = [3, 8, 2, 9, 5, 11]
print("input values", values)

for value in values:
    if value % 2 == 0:
        print("even", value)

def normalize(values):
    maximum = max(values) if values else 1
    return [value / maximum for value in values]

print(normalize(values))
