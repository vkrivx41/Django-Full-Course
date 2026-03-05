import datetime
import json
import base64
import rsa
from django.conf import settings
from urllib.parse import quote

from botocore.signers import CloudFrontSigner


def rsa_signer(message):
    private_key = rsa.PrivateKey.load_pkcs1(settings.CLOUDFRONT_PRIVATE_KEY.encode())
    return rsa.sign(message, private_key, "SHA-1")


def generate_signed_cookies():

    expire_date = datetime.datetime.utcnow() + datetime.timedelta(hours=1)

    policy = json.dumps({
        "Statement": [
            {
                "Resource": f"https://{settings.CLOUDFRONT_DOMAIN}/attachments/*",
                "Condition": {
                    "DateLessThan": {
                        "AWS:EpochTime": int(expire_date.timestamp())
                    }
                }
            }
        ]
    })

    signer = CloudFrontSigner(settings.CLOUDFRONT_KEY_PAIR_ID, rsa_signer)

    signed_cookie = signer.generate_presigned_cookie(policy)

    return signed_cookie











    import datetime
import json
import base64
import rsa
from django.conf import settings
from urllib.parse import quote

from botocore.signers import CloudFrontSigner


def rsa_signer(message):
    private_key = rsa.PrivateKey.load_pkcs1(settings.CLOUDFRONT_PRIVATE_KEY.encode())
    return rsa.sign(message, private_key, "SHA-1")


def generate_signed_cookies():

    expire_date = datetime.datetime.utcnow() + datetime.timedelta(hours=1)

    policy = json.dumps({
        "Statement": [
            {
                "Resource": f"https://{settings.CLOUDFRONT_DOMAIN}/attachments/*",
                "Condition": {
                    "DateLessThan": {
                        "AWS:EpochTime": int(expire_date.timestamp())
                    }
                }
            }
        ]
    })

    signer = CloudFrontSigner(settings.CLOUDFRONT_KEY_PAIR_ID, rsa_signer)

    signed_cookie = signer.generate_presigned_cookie(policy)

    return signed_cookie