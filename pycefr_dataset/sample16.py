# Synthetic Python sample 16; intended focus: B2.

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
from dataclasses import dataclass

@dataclass
class Measurement:
    label: str
    value: float

    def scaled(self, factor: float) -> "Measurement":
        return Measurement(self.label, self.value * factor)

measurements = [Measurement("a", 3.0), Measurement("b", 8.0)]
print([item.scaled(1.5) for item in measurements])
