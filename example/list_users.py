import os

from ksyun.common import credential
from ksyun.common.profile.client_profile import ClientProfile
from ksyun.common.profile.http_profile import HttpProfile
from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.client.iam.v20151101 import client as iam_client, models as iam_models

try:
    cred = credential.Credential(
        os.environ.get("KSYUN_SECRET_ID", "KSYUN_SECRET_ID_HERE"),
        os.environ.get("KSYUN_SECRET_KEY", "KSYUN_SECRET_KEY_HERE")
    )

    httpProfile = HttpProfile()
    httpProfile.endpoint = "iam.api.ksyun.com"
    httpProfile.reqMethod = "POST"
    httpProfile.reqTimeout = 60
    httpProfile.scheme = "http"
    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile

    iamClient = iam_client.IamClient(cred, "cn-beijing-6", profile=clientProfile)

    print(iamClient.call("ListUsers", {
            "MaxItems": 100,
        }))

except KsyunSDKException as err:
    print(err)
