import os
import shutil
from config import BASE_DIR, KAGGLE_JSON_PATH, TARGET_DIR

def download_titanic_csv():
    # Copy kaggle.json to expected location temporarily
    os.makedirs(TARGET_DIR, exist_ok=True)
    shutil.copy(KAGGLE_JSON_PATH, os.path.join(TARGET_DIR, 'kaggle.json'))

    csv_path = os.path.join(BASE_DIR, 'Titanic-Dataset.csv')

    if os.path.isfile(csv_path):
        print(f"Existing file found, removing: {csv_path}")
        os.remove(csv_path)

    os.makedirs(BASE_DIR, exist_ok=True)
    
    from kaggle.api.kaggle_api_extended import KaggleApi

    api = KaggleApi()
    api.authenticate()

    print("Downloading Titanic dataset...")
    api.dataset_download_files('yasserh/titanic-dataset', path=BASE_DIR, unzip=True)
    print("Download complete!")

    return csv_path
