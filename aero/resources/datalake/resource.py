import os
from boto3.session import Session
import awswrangler as wr
import pandas as pd


class S3DataLakeResource(Session):

    def to_csv(self, df: pd.DataFrame, path: str) -> None:
        wr.config.s3_endpoint_url = os.getenv('S3_ENDPOINT_URL', None)

        wr.s3.to_csv(
            df=df,
            index=False,
            path=path,
            boto3_session=self
        )


def s3_datalake():
    return S3DataLakeResource(
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID', None),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY', None)
    )
