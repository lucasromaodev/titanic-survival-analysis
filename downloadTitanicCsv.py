import os
import shutil

def download_titanic_csv():
    # Copy kaggle.json to expected location temporarily
    custom_path = r'C:\Users\luckh\Desktop\Automações\titanic-project\kaggle.json'
    target_dir = r'C:\Users\luckh\.kaggle'
    os.makedirs(target_dir, exist_ok=True)
    shutil.copy(custom_path, os.path.join(target_dir, 'kaggle.json'))

    # Continue as normal
    download_dir = r'C:\Users\luckh\Desktop\Automações\titanic-project'
    csv_path = os.path.join(download_dir, 'Titanic-Dataset.csv')

    if os.path.isfile(csv_path):
        print(f"Existing file found, removing: {csv_path}")
        os.remove(csv_path)

    os.makedirs(download_dir, exist_ok=True)
    
    from kaggle.api.kaggle_api_extended import KaggleApi

    api = KaggleApi()
    api.authenticate()

    print("Downloading Titanic dataset...")
    api.dataset_download_files('yasserh/titanic-dataset', path=download_dir, unzip=True)
    print("Download complete!")

    return csv_path
