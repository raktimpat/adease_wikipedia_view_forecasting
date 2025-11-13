URL = '1mdgQscjqnCtdg7LGItomyK0abN6lcHBb'

import pandas as pd
import ssl
import certifi

ctx = ssl.create_default_context(cafile=certifi.where())

cert = {"ssl": ctx}
train_url = 'https://drive.google.com/file/d/1qQkymAitU6l2pSe702rDUhQpoP8MUZXl'
exog_url = 'https://drive.google.com/file/d/19qvuu7E8yD63o4WkOdy_lLFSrZlZPpuE'
def load_data():
    try:
        train_data = pd.read_csv(train_url, storage_options=cert)
        exog_data = pd.read_csv(exog_url, storage_options=cert)

        train_data.to_csv('data/raw/train_data.csv', index=False)
        exog_data.to_csv('data/raw/exog_data.csv', index=False)
        print("Data loaded and saved successfully.")
    except Exception as e:
        print(f"An error occurred while loading data: {e}")

if __name__ == "__main__":
    load_data()