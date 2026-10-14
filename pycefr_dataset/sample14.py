# Synthetic Python sample 14; intended focus: B1.

values = [3, 8, 2, 9, 5, 11]
print("input values", values)

for value in values:
    if value % 2 == 0:
        print("even", value)

def unique_sorted(values):
    return sorted(set(values))

print(unique_sorted(values))
from collections import defaultdict

def group_by_parity(values):
    groups = defaultdict(list)
    for value in values:
        groups["even" if value % 2 == 0 else "odd"].append(value)
    return dict(groups)

print(group_by_parity(values))
