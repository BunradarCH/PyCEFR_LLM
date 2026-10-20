from pycefr import pycerfl
from create_gold_labels import create_gold_labels

# Step 1: Run PyCEFR analysis
pycerfl.read_Directory("pycefr_dataset", "dataset_30")
pycerfl.summary_Levels()

# Step 2: Generate gold_labels.csv
create_gold_labels()

print("PyCEFR analysis and gold label generation completed!")
