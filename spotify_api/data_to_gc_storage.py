import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
file_location = []
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        file_location.append(os.path.join(dirname, filename))
        print(os.path.join(dirname, filename))
print(file_location)

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="F:\Road to Opta\directed-post-316003-300502ca1f7e.json"

def implicit():
    from google.cloud import storage

    # If you don't specify credentials when constructing the client, the
    # client library will look for credentials in the environment.
    storage_client = storage.Client()

    # Make an authenticated API request
    buckets = list(storage_client.list_buckets())
    print(buckets)

implicit()

# Function to upload data from kaggle to Google storage

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket. https://cloud.google.com/storage/docs/ """
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))

# List bucket items

def list_blobs(bucket_name):
    """Lists all the blobs in the bucket. https://cloud.google.com/storage/docs/"""
    blobs = storage_client.list_blobs(bucket_name)
    for blob in blobs:
        print(blob.name)

bucket_name = "projects_storage"

# Upload from kaggle to google storage
for filename in file_location:
    local_data = filename
    file_name = filename[46:]
    upload_blob(bucket_name, local_data, file_name)
    print('Data inside of',bucket_name,':')
    list_blobs(bucket_name)