# Synthetic Python sample 10; intended focus: A2.

values = [3, 8, 2, 9, 5, 11]
print("input values", values)

for value in values:
    if value % 2 == 0:
        print("even", value)

def describe(values):
    return [(value, "even" if value % 2 == 0 else "odd") for value in values]

print(describe(values))
