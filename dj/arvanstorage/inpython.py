import tempfile
import boto3
import os

access_key = 'b0d5bbca-ef7e-498b-a21d-8de4edf08da4'
secret_key = 'a8aefbd5d89a79e3257387eea20d5a67e3aa0e5dd45677a6695a64fe767e6c93'
endpoint = 'https://s3.ir-thr-at1.arvanstorage.com'
session = boto3.session.Session()

s3_client = session.client(
    service_name='s3',
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    endpoint_url=endpoint,
)



def list_buckets():
    response = s3_client.list_buckets()
    buckets = []
    for bucket in response['Buckets']:
        buckets.append(bucket["Name"])
    return buckets


def get_bucket_keys(bucket):
    """Get a list of keys in an S3 bucket."""
    keys = []
    resp = s3_client.list_objects_v2(Bucket=bucket)
    for obj in resp['Contents']:
        keys.append(obj['Key'])
    return keys


def upload_file(filename, bucket_name, name_in_bucket):
    s3_client.upload_file(filename, bucket_name, name_in_bucket)


def get_url(bucket, Key):
    return s3_client.generate_presigned_url('get_object', Params={'Bucket': bucket, 'Key': Key})
