# Synthetic Python sample 25; intended focus: C1.

values = [3, 8, 2, 9, 5, 11]
print("input values", values)

for value in values:
    if value % 2 == 0:
        print("even", value)

def describe(values):
    return [(value, "even" if value % 2 == 0 else "odd") for value in values]

print(describe(values))
import asyncio

async def calculate_after_delay(value):
    await asyncio.sleep(0)
    return value * value

async def gather_results(values):
    tasks = [calculate_after_delay(value) for value in values]
    return await asyncio.gather(*tasks)

print(asyncio.run(gather_results(values)))
def pairwise_differences(values):
    result = []
    for left, right in zip(values, values[1:]):
        result.append(right - left)
    return result

print(pairwise_differences(values))
