# Synthetic Python sample 18; intended focus: B2.

values = [3, 8, 2, 9, 5, 11]
print("input values", values)

for value in values:
    if value % 2 == 0:
        print("even", value)

def normalize(values):
    maximum = max(values) if values else 1
    return [value / maximum for value in values]

print(normalize(values))
class SequenceView:
    def __init__(self, values):
        self._values = tuple(values)

    def __len__(self):
        return len(self._values)

    def __iter__(self):
        yield from self._values

view = SequenceView(values)
print(list(view), len(view))
