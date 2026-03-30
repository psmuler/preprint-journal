#!/usr/bin/env python3
"""
Download arXiv metadata JSON from Kaggle
and store it directly into ~/r2/arxiv on Cloudflare R2.

Requirements:
    pip install kaggle tqdm

Login to kaggle https://www.kaggle.com/settings and create api key
upload kaggle.json to ~/.kaggle/ 
"""

import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi
from tqdm import tqdm

# Target paths
r2_dir = os.path.expanduser("~/r2/arxiv")
os.makedirs(r2_dir, exist_ok=True)

zip_path = os.path.join(r2_dir, "arxiv-metadata-oai-snapshot.json.zip")
json_path = os.path.join(r2_dir, "arxiv-metadata-oai-snapshot.json")

# Initialize Kaggle API
api = KaggleApi()
api.authenticate()

# Download file (if not already exists)
if not os.path.exists(zip_path):
    print("Downloading dataset from Kaggle...")
    api.dataset_download_file(
        dataset="cornell-university/arxiv",
        file_name="arxiv-metadata-oai-snapshot.json",
        path=r2_dir
    )
else:
    print("ZIP file already exists — skipping download.")

# Unzip file
if not os.path.exists(json_path):
    print("Extracting JSON to", r2_dir)
    with zipfile.ZipFile(zip_path, 'r') as zf:
        for member in tqdm(zf.namelist(), desc="Extracting"):
            zf.extract(member, r2_dir)
else:
    print("JSON already extracted.")

# Optional: remove the ZIP to save space
try:
    os.remove(zip_path)
except FileNotFoundError:
    pass

print(f"✅ Done. File saved at: {json_path}")