# 调用子用户列表

import os
from ksyun.common import credential
from ksyun.common.profile.client_profile import ClientProfile
from ksyun.common.profile.http_profile import HttpProfile
from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.client.iam.v20151101 import client, models

try:
    # 实例化一个证书对象，入参需要传入secretId，secretKey
    cred = credential.Credential(
        os.environ.get("KSYUN_SECRET_ID", "KSYUN_SECRET_ID_HERE"),
        os.environ.get("KSYUN_SECRET_KEY", "KSYUN_SECRET_KEY_HERE")
    )
    httpProfile = HttpProfile()
    httpProfile.endpoint = "iam.api.ksyun.com"
    httpProfile.reqMethod = "GET"  # get请求(默认为post请求)
    httpProfile.reqTimeout = 30  # 请求超时时间，单位为秒(默认60秒)

    clientProfile = ClientProfile()
    # clientProfile.signMethod = "HMAC-SHA256"  # 指定签名算法
    clientProfile.httpProfile = httpProfile
    client = client.IamClient(cred, "cn-beijing-6", clientProfile)

    # 实例化一个请求对象, 每个接口都会对应一个request对象。
    req = models.ListUsersRequest()

    # # 传参示例1
    # req.Marker = "10"
    # req.MaxItems = 10

    # 传参示例2
    # 这里还支持以标准json格式的string来赋值请求参数的方式。下面的代码跟上面的参数赋值是等效的。
    params = '''{
           "Marker": "10",
           "MaxItems": 10
       }'''
    req.from_json_string(params)

    # 调用接口返回
    resp = client.ListUsers(req)
    print(resp)
except KsyunSDKException as err:
    print(err)
