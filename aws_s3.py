import boto3
import os
from typing import List


def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    response = s3_client.upload_file(file_name, bucket, object_name)


def download_file(local_file_path, bucket, object_name):
    """Download a file from an S3 bucket

    :param local_file_path: Local path to save file
    :param bucket: Bucket to download from
    :param object_name: S3 object name
    """

    # Download the file
    s3_client = boto3.client('s3')
    response = s3_client.download_file(bucket, object_name, local_file_path)


def list_objects(bucket, prefix) -> List[str]:
    """List objects in an S3 bucket

    :param bucket: Bucket to list objects from
    :param prefix: Prefix to filter objects by
    :return: List of object names
    """

    # Retrieve the list of bucket objects
    s3_client = boto3.client('s3')
    response = s3_client.list_objects_v2(Bucket=bucket, Prefix=prefix)

    # Iterate through object list and add to list
    object_list = []
    for obj in response['Contents']:
        object_list.append(obj['Key'])

    return object_list


def delete_objects(bucket, object_names):
    """Delete multiple objects from an S3 bucket
    
    :param bucket: Bucket to delete objects from
    :param object_names: List of S3 object names
    """

    # Prepare the format for the delete operation
    objects = [{'Key': obj_name} for obj_name in object_names]

    # Delete the objects
    s3_client = boto3.client('s3')
    response = s3_client.delete_objects(Bucket=bucket, Delete={'Objects': objects})
