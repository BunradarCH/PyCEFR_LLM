# Synthetic Python sample 01; intended focus: A1.

values = [3, 8, 2, 9, 5]
threshold = 5
for value in values:
    if value >= threshold:
        print("selected", value)

def label_value(value):
    return "large" if value > 5 else "small"

print("label", label_value(7))
