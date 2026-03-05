from datetime import datetime, timezone, timedelta
from urllib import parse

from django.conf import settings

from botocore.signers import CloudFrontSigner

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_private_key


PRIVATE_KEY = load_pem_private_key(
    settings.AWS_S3_CLOUDFRONT_KEY,
    password=None
)

def rsa_signer(message):
    return PRIVATE_KEY.sign(
        message,
        padding.PKCS1v15(),
        hashes.SHA1()
    )

cloudfront_signer = CloudFrontSigner(
    settings.AWS_S3_CLOUDFRONT_KEY_ID,
    rsa_signer
)

def generate_signed_url(key: str, expires=600):
    key_parsed: str = parse.quote(key)
    url: str = f"https://{settings.AWS_S3_CUSTOM_DOMAIN}/{key_parsed}"

    expire_date = datetime.now(timezone.utc) + timedelta(seconds=expires)

    signed_url: str = cloudfront_signer.generate_presigned_url(
        url,
        date_less_than=expire_date
    )

    return signed_url
