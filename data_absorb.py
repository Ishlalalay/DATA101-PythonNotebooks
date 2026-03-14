'''
import os
import kaggle

# Ensure Kaggle API credentials are set
os.environ['KAGGLE_CONFIG_DIR'] = os.path.expanduser("~/.kaggle")

# Dataset reference
dataset_ref = "bwandowando/philippine-cities-air-quality-index-data-2026"

# Download the latest dataset version
kaggle.api.dataset_download_files(dataset_ref, path="./data", unzip=True)

print("Dataset updated successfully.")


# KGAT_97ddd9b66699a4e3e9a78c10de2838e3
# export KAGGLE_API_TOKEN=KGAT_97ddd9b66699a4e3e9a78c10de2838e3
# kaggle competitions list


KGAT_02d8bbccafae80094ff28a61b34e538e
export KAGGLE_API_TOKEN=KGAT_02d8bbccafae80094ff28a61b34e538e
kaggle competitions list
'''

import os
import kaggle

# set KAGGLE_CONFIG_DIR=C:\Users\kiwib\.kaggle\kaggle.json
# Step 1: Point to the folder containing kaggle.json
# Make sure kaggle.json is located at: C:\Users\kiwib\.kaggle\kaggle.json
os.environ["KAGGLE_CONFIG_DIR"] = r"C:\Users\kiwib\.kaggle"

# Step 2: Dataset reference (from Kaggle URL)
dataset_ref = "bwandowando/philippine-cities-air-quality-index-data-2026"

# Step 3: Function to download and unzip dataset
def update_dataset():
    kaggle.api.dataset_download_files(dataset_ref, path="./dataset", unzip=True)
    print("Dataset updated successfully.")

# Step 4: Run the script
if __name__ == "__main__":
    update_dataset()