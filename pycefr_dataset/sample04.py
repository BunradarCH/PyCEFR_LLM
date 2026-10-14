# Synthetic Python sample 04; intended focus: A1.

temperatures = [22, 28, 19, 31]
for temperature in temperatures:
    if temperature >= 30:
        print("hot")
    else:
        print("mild")

def label_value(value):
    return "large" if value > 5 else "small"

print("label", label_value(7))
