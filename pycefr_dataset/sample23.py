# Synthetic Python sample 23; intended focus: C1.

values = [3, 8, 2, 9, 5, 11]
print("input values", values)

for value in values:
    if value % 2 == 0:
        print("even", value)

def normalize(values):
    maximum = max(values) if values else 1
    return [value / maximum for value in values]

print(normalize(values))
from typing import Generic, TypeVar

T = TypeVar("T")

class Stack(Generic[T]):
    def __init__(self):
        self._items = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

stack = Stack[int]()
for value in values:
    stack.push(value)
print(stack.pop())
def moving_average(values, window=2):
    if window <= 0:
        raise ValueError("window must be positive")
    return [sum(values[i:i + window]) / window
            for i in range(len(values) - window + 1)]

print(moving_average(values))
def rolling_totals(numbers):
    running = 0
    result = []
    for number in numbers:
        running += number
        result.append(running)
    return result

print("rolling totals", rolling_totals(values))
