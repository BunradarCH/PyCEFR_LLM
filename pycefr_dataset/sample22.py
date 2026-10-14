# Synthetic Python sample 22; intended focus: C1.

import re
from collections import Counter

class SensorReading:
    __slots__ = ('name', 'value')

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def label(self):
        return self.name.upper()


def valid_measurements(rows):
    for name, value in rows:
        if re.fullmatch(r'[a-z_]+', name) and isinstance(value, (int, float)):
            yield SensorReading(name, value)


def summarize(readings, threshold=20):
    readings = list(readings)
    high = [item for item in readings if item.value >= threshold]
    names = [item.label() for item in high]
    categories = Counter('high' if item.value >= threshold else 'low'
                         for item in readings)
    return {'names': names, 'counts': dict(categories), 'total': len(readings)}


def rolling_pairs(values):
    for index in range(len(values) - 1):
        yield (values[index], values[index + 1])


def main():
    raw = [('room_a', 18), ('room_b', 27), ('bad name', 99),
           ('room_c', 22), ('room_d', 11)]
    report = summarize(valid_measurements(raw))
    print('High readings:', report['names'])
    print('Categories:', report['counts'])
    values = [18, 27, 22, 11]
    print('Adjacent pairs:', list(rolling_pairs(values)))


if __name__ == '__main__':
    main()
