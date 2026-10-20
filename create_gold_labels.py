
import json
import csv
from pathlib import Path


def create_gold_labels():
    # Step 1: Read PyCEFR JSON results
    json_path = Path("DATA_JSON/dataset_30.json")

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    samples = data["dataset_30"]

    levels = ["A1", "A2", "B1", "B2", "C1", "C2"]

    # Step 2: Define CSV columns
    columns = [
        "filename",
        "total_elements",
        "detected_levels",
        "A1_count",
        "A2_count",
        "B1_count",
        "B2_count",
        "C1_count",
        "C2_count",
        "most_frequent_level",
        "highest_detected_level"
    ]

    # Step 3: Generate reference labels
    rows = []

    for filename, result in sorted(samples.items()):

        counts = {
            level: int(result["Levels"].get(level, 0))
            for level in levels
        }

        total = sum(counts.values())

        detected = [
            level for level in levels
            if counts[level] > 0
        ]

        if total > 0:
            max_count = max(counts.values())

            most_frequent = [
                level for level in levels
                if counts[level] == max_count
            ]

            highest = detected[-1]
        else:
            most_frequent = []
            highest = ""

        row = {
            "filename": filename,
            "total_elements": total,
            "detected_levels": ";".join(detected),
            "most_frequent_level": ";".join(most_frequent),
            "highest_detected_level": highest
        }

        for level in levels:
            row[f"{level}_count"] = counts[level]

        rows.append(row)

    # Step 4: Save gold_labels.csv
    output_path = Path("gold_labels.csv")

    with open(output_path, "w",
              newline="", encoding="utf-8") as f:

        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Created gold_labels.csv for {len(rows)} files")


# Allows this script to run independently
if __name__ == "__main__":
    create_gold_labels()
