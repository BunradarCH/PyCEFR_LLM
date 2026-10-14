# Synthetic Python sample 12; intended focus: B1.

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
class ScoreBook:
    def __init__(self, values):
        self.values = list(values)

    def passing(self, cutoff=5):
        return [value for value in self.values if value >= cutoff]

book = ScoreBook(values)
print(book.passing())
