# Synthetic Python sample 27; intended focus: C2.

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
import asyncio

class AsyncRange:
    def __init__(self, stop):
        self.stop = stop

    def __aiter__(self):
        self.current = 0
        return self

    async def __anext__(self):
        if self.current >= self.stop:
            raise StopAsyncIteration
        result = self.current
        self.current += 1
        await asyncio.sleep(0)
        return result

async def collect():
    return [number async for number in AsyncRange(5)]

print(asyncio.run(collect()))
class ScoreBook:
    def __init__(self, values):
        self.values = list(values)

    def passing(self, cutoff=5):
        return [value for value in self.values if value >= cutoff]

book = ScoreBook(values)
print(book.passing())
def rolling_totals(numbers):
    running = 0
    result = []
    for number in numbers:
        running += number
        result.append(running)
    return result

print("rolling totals", rolling_totals(values))
