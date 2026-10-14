# Synthetic Python sample 30; intended focus: C2.

values = [3, 8, 2, 9, 5, 11]
print("input values", values)

for value in values:
    if value % 2 == 0:
        print("even", value)

def describe(values):
    return [(value, "even" if value % 2 == 0 else "odd") for value in values]

print(describe(values))
from contextlib import asynccontextmanager
import asyncio

@asynccontextmanager
async def managed_resource():
    resource = {"open": True, "events": []}
    try:
        yield resource
    finally:
        resource["open"] = False
        print("resource closed", resource["events"])

async def workflow():
    async with managed_resource() as resource:
        resource["events"].append("processed")
        await asyncio.sleep(0)
        return len(resource["events"])

print(asyncio.run(workflow()))
def pairwise_differences(values):
    result = []
    for left, right in zip(values, values[1:]):
        result.append(right - left)
    return result

print(pairwise_differences(values))
def remove_outliers(numbers):
    if len(numbers) < 3:
        return list(numbers)
    ordered = sorted(numbers)
    low = ordered[0]
    high = ordered[-1]
    filtered = [number for number in numbers if low < number < high]
    return filtered if filtered else list(numbers)

print("trimmed", remove_outliers(values))
