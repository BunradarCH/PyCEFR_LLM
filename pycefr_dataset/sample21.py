# Synthetic Python sample 21; intended focus: C1.

values = [3, 8, 2, 9, 5, 11]
print("input values", values)

for value in values:
    if value % 2 == 0:
        print("even", value)

def summarize(values):
    total = sum(values)
    return {"count": len(values), "total": total}

summary = summarize(values)
print(summary)
from functools import wraps

def trace_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("calling", func.__name__)
        return func(*args, **kwargs)
    return wrapper

@trace_calls
def total_score(values):
    return sum(values)

print(total_score(values))
def safe_mean(values):
    try:
        if not values:
            raise ValueError("empty sequence")
        return sum(values) / len(values)
    except (TypeError, ValueError) as exc:
        print("Cannot calculate mean:", exc)
        return None

print(safe_mean(values))
def remove_outliers(numbers):
    if len(numbers) < 3:
        return list(numbers)
    ordered = sorted(numbers)
    low = ordered[0]
    high = ordered[-1]
    filtered = [number for number in numbers if low < number < high]
    return filtered if filtered else list(numbers)

print("trimmed", remove_outliers(values))
