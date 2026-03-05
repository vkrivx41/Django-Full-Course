import boto3
import requests

from utilities.s3 import storage

def run():
    stroage_client  = storage.Boto3Client()

    # buckets = stroage_client.client.list_buckets()

    # print(buckets['Buckets'])

    # presigned_post_url = stroage_client.generate_upload_presigned_post(
    #     "attachments/image1.png", "image/png", 1024 * 1024 * 10,
    #     expires=600
    # )
    # print(presigned_post_url)

    # print()
    # s3://demo-chatapp-bucket/attachments/1/musk.jpg

    presigned_download_url = stroage_client.generate_download_presigned_url(
        "attachments/login-form-design-03.jpg", expires=60
    )

    if presigned_download_url is not None:
        response = requests.get(presigned_download_url)
        print(response)
        print(presigned_download_url)

# create_bucket
# delete_bucket
# get_bucket_location
# download_file
# upload_file
# generate_presigned_post
# generate_presigned_url
# list_buckets
