# Synthetic Python sample 06; intended focus: A2.

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
def rolling_totals(numbers):
    running = 0
    result = []
    for number in numbers:
        running += number
        result.append(running)
    return result

print("rolling totals", rolling_totals(values))
