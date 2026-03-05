
from django.conf import settings

import boto3
from botocore.exceptions import BotoCoreError


class Boto3Client:
    client = boto3.client(
        "s3",
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_S3_REGION_NAME
    )

    @classmethod
    def generate_upload_presigned_post(cls, key, content_type, max_size, expires=600):
        
        try:
            response =  cls.client.generate_presigned_post(
                Bucket=settings.AWS_STORAGE_BUCKET_NAME,
                Key=key,
                Fields={'Content-Type': content_type},
                Conditions=[
                    ['content-length-range', 1, max_size]  # 1 file only
                ],
                ExpiresIn=expires
            )
        except BotoCoreError:
            return None
        
        return response


    @classmethod
    def generate_download_presigned_url(cls, key, expires=600):
        """
        We generate a presigned url with the action as 'get_object'
        Params: contains the bucket name and the key
        Expires: the url TTL
        """
        try:
            response = cls.client.generate_presigned_url(
                'get_object',
                Params={
                    "Bucket": settings.AWS_STORAGE_BUCKET_NAME,
                    "Key": key,
                },
                ExpiresIn=expires,
            )
        except BotoCoreError:
            return None
        
        return response
    