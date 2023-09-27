import boto3
import botocore

# Replace these with your own AWS credentials and bucket name
aws_access_key_id = 'YOUR_ACCESS_KEY_ID'
aws_secret_access_key = 'YOUR_SECRET_ACCESS_KEY'
bucket_name = 'your-s3-bucket-name'

# Initialize the S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# Specify the file you want to download from the bucket
file_key = 'path/to/your/file.txt'

# Specify the local file path where you want to save the downloaded file
local_file_path = 'local/path/to/save/file.txt'

try:
    # Download the file from the S3 bucket
    s3.download_file(bucket_name, file_key, local_file_path)
    print(f"File downloaded successfully to {local_file_path}")
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == '404':
        print("The file does not exist in the bucket.")
    else:
        print(f"An error occurred: {str(e)}")
