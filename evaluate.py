
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
GOLD_FILE = ROOT / "gold_labels.csv"
QWEN_FILE = ROOT / "results" / "qwen_explanations.json"
OUTPUT_FILE = ROOT / "results" / "evaluation.csv"

LEVELS = ["A1", "A2", "B1", "B2", "C1", "C2"]


def get_section(text, number):
    pattern = (
        rf"(?m)^\s*{number}\.\s+[^\n]*\n"
        rf"(.*?)(?=^\s*{number + 1}\.\s|\Z)"
    )
    match = re.search(pattern, text, re.S | re.M | re.I)
    return match.group(1).strip() if match else ""


def extract_total(text):
    patterns = [
        r"total (?:number of (?:detected )?elements )?"
        r"(?:is|of|=|:)\s*(\d+)",
        r"totaling\s+(\d+)",
        r"total\s+is\s+(\d+)",
        r"=\s*(\d+)(?:\s+elements)?\.",
        r"(\d+)\s+elements\s+in total",
    ]
    for pattern in patterns:
        match = re.search(pattern, text, re.I)
        if match:
            return int(match.group(1))
    return None


def extract_level(text):
    match = re.search(r"\b(A1|A2|B1|B2|C1|C2)\b", text, re.I)
    return match.group(1).upper() if match else None


def extract_distribution(text):
    found = {}
    for level in LEVELS:
        patterns = [
            rf"\b(\d+)\s+(?:elements?\s+)?(?:at|for|in)\s+{level}\b",
            rf"\b{level}\s*(?:has|with|contains|\(|:|=)\s*(\d+)\b",
        ]
        values = set()
        for pattern in patterns:
            for match in re.finditer(pattern, text, re.I):
                values.add(int(match.group(1)))
        if values:
            found[level] = values
    return found


def compare(actual, expected):
    if actual is None:
        return "REVIEW"
    return "PASS" if actual == expected else "FAIL"


with open(GOLD_FILE, newline="", encoding="utf-8-sig") as file:
    gold_rows = list(csv.DictReader(file))

with open(QWEN_FILE, encoding="utf-8") as file:
    explanations = json.load(file)

results = []

for gold in gold_rows:
    filename = gold["filename"]
    text = explanations.get(filename, "")

    sections = [get_section(text, i) for i in range(1, 5)]

    total = extract_total(sections[0])
    distribution = extract_distribution(sections[1])
    frequent = extract_level(sections[2])
    highest = extract_level(sections[3])

    expected_distribution = {
        level: int(gold[f"{level}_count"])
        for level in LEVELS
    }

    if not distribution:
        distribution_status = "REVIEW"
    elif any(len(values) != 1 for values in distribution.values()):
        distribution_status = "REVIEW"
    elif any(
        next(iter(values)) != expected_distribution[level]
        for level, values in distribution.items()
    ):
        distribution_status = "FAIL"
    elif set(distribution) != {
        level for level in LEVELS
        if expected_distribution[level] > 0
    }:
        distribution_status = "REVIEW"
    else:
        distribution_status = "PASS"

    row = {
        "filename": filename,
        "total_check": compare(total, int(gold["total_elements"])),
        "distribution_check": distribution_status,
        "frequent_check": compare(
            frequent, gold["most_frequent_level"]
        ),
        "highest_check": compare(
            highest, gold["highest_detected_level"]
        ),
    }

    results.append(row)

OUTPUT_FILE.parent.mkdir(exist_ok=True)

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=results[0].keys())
    writer.writeheader()
    writer.writerows(results)

checks = [
    row[key]
    for row in results
    for key in [
        "total_check",
        "distribution_check",
        "frequent_check",
        "highest_check",
    ]
]

passed = checks.count("PASS")
failed = checks.count("FAIL")
review = checks.count("REVIEW")

print("Evaluation completed!")
print(f"Samples: {len(results)}")
print(f"Passed checks: {passed}")
print(f"Failed checks: {failed}")
print(f"Need manual review: {review}")

if review == 0:
    print(f"Factual accuracy: {passed / len(checks) * 100:.2f}%")
else:
    print("Final accuracy pending manual review.")

print("\nSamples requiring attention:")
for row in results:
    if any(value != "PASS" for value in list(row.values())[1:]):
        print(row)

print(f"\nSaved to: {OUTPUT_FILE}")
