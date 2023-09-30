import aws_s3
import pandas as pd


# Specify the S3 bucket and prefix
bucket_name = 'mindatos-project'
prefix = 'energy-data/'

# List all objects in the S3 bucket under the specified prefix
object_keys = aws_s3.list_objects(bucket_name, prefix)

local_file_path = '/tmp/data'

data_frames = {}

for object_key in object_keys:
    if object_key.endswith('.csv'):
        # Download the object to the local file path
        aws_s3.download_file(local_file_path, bucket_name, object_key)
        data_frames[object_key] = pd.read_csv('/tmp/data', sep = ';')