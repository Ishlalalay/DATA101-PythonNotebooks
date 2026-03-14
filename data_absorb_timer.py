
import schedule
import time
import os
import kaggle

def update_dataset():
    dataset_ref = "bwandowando/philippine-cities-air-quality-index-data-2026"
    kaggle.api.dataset_download_files(dataset_ref, path="./data", unzip=True)
    print("Dataset updated successfully.")

# Schedule daily at 6 AM
schedule.every().day.at("06:00").do(update_dataset)

while True:
    schedule.run_pending()
    time.sleep(60)