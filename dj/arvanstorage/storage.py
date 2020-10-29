from django.conf import settings
from django.core.files.storage import Storage, FileSystemStorage
import boto3
import os
import tempfile


class MyStorage(Storage):

    def __init__(self):
        aws_access_key_id = settings.ARVAN_ACCESS_KEY_ID
        aws_secret_access_key = settings.ARVAN_SECRET_ACCESS_KEY
        endpoint_url = settings.ARVAN_S3_ENDPOINT_URL
        session = boto3.session.Session()

        self.s3_client = session.client(
            service_name='s3',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            endpoint_url=endpoint_url,
        )

        self.bucket_name = settings.ARVAN_STORAGE_BUCKET_NAME


    def list_buckets(self):
        response = self.s3_client.list_buckets()
        buckets = []
        for bucket in response['Buckets']:
            buckets.append(bucket["Name"])
        return buckets


    def get_bucket_keys(self):
        """Get a list of keys in an S3 bucket."""
        keys = []
        resp = self.s3_client.list_objects_v2(Bucket=self.bucket_name)
        try:
            objs = resp['Contents']
            for obj in objs:
                keys.append(obj['Key'])
            return keys
        except Exception as e:
            if str(e).strip("'") == 'Contents':
                return []
            else:
                raise e


    def upload_file(self, filename, name_in_bucket):
        self.s3_client.upload_file(filename, self.bucket_name, name_in_bucket)


    def get_url(self, Key):
        return self.s3_client.generate_presigned_url('get_object', Params={'Bucket': self.bucket_name, 'Key': Key})



    def _save(self, name, content):

        tf = tempfile.NamedTemporaryFile()
        content.seek(0, os.SEEK_SET)
        tf.write(content.read())
        tf.seek(0, os.SEEK_SET)

        file_root, file_ext = os.path.splitext(name)
        keys = self.get_bucket_keys()
        if name in keys:
            name = self.get_alternative_name(file_root, file_ext)

        self.upload_file(tf.name, name)
        tf.close()

        return name


    def exists(self, name):
        return False


    def url(self, name):
        # if self.base_url is None:
        #     raise ValueError("This file is not accessible via a URL.")
        # url = filepath_to_uri(name)
        # if url is not None:
        #     url = url.lstrip('/')
        # return urljoin(self.base_url, url)


        return self.get_url(name)
