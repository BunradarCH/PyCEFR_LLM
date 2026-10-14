# Synthetic Python sample 26; intended focus: C2.

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
class RegistryMeta(type):
    registry = {}

    def __new__(mcls, name, bases, namespace):
        cls = super().__new__(mcls, name, bases, namespace)
        if name != "Plugin":
            mcls.registry[name.lower()] = cls
        return cls

class Plugin(metaclass=RegistryMeta):
    def run(self, value):
        raise NotImplementedError

class Double(Plugin):
    def run(self, value):
        return value * 2

print(RegistryMeta.registry["double"]().run(4))
def safe_mean(values):
    try:
        if not values:
            raise ValueError("empty sequence")
        return sum(values) / len(values)
    except (TypeError, ValueError) as exc:
        print("Cannot calculate mean:", exc)
        return None

print(safe_mean(values))
