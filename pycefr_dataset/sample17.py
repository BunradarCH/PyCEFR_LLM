# Synthetic Python sample 17; intended focus: B2.

values = [3, 8, 2, 9, 5, 11]
print("input values", values)

for value in values:
    if value % 2 == 0:
        print("even", value)

def categorize(values):
    groups = {"high": [], "low": []}
    for value in values:
        key = "high" if value >= 5 else "low"
        groups[key].append(value)
    return groups

print(categorize(values))
from contextlib import contextmanager

@contextmanager
def transaction(log):
    log.append("begin")
    try:
        yield log
    except Exception:
        log.append("rollback")
        raise
    else:
        log.append("commit")

history = []
with transaction(history) as record:
    record.append("updated")
print(history)
def remove_outliers(numbers):
    if len(numbers) < 3:
        return list(numbers)
    ordered = sorted(numbers)
    low = ordered[0]
    high = ordered[-1]
    filtered = [number for number in numbers if low < number < high]
    return filtered if filtered else list(numbers)

print("trimmed", remove_outliers(values))
