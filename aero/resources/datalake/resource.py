import os
from boto3 import client


def s3_datalake():
    return client(
        's3',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID', None),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY', None),
        endpoint_url=os.getenv('S3_ENDPOINT_URL', None)
    )
