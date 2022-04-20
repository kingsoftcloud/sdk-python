# -*- coding: utf-8 -*-
# Copyright 2022 Ksyun Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os

from ksyun.common import common_client
from ksyun.common import credential
from ksyun.common.exception import KsyunSDKException
from ksyun.common.profile.client_profile import ClientProfile
from ksyun.common.profile.http_profile import HttpProfile

try:
    cred = credential.Credential(
        os.environ.get("KSYUN_SECRET_ID", "KSYUN_SECRET_ID_HERE"),
        os.environ.get("KSYUN_SECRET_KEY", "KSYUN_SECRET_KEY_HERE")
    )

    httpProfile = HttpProfile()
    # 域名首段必须和下文中CommonClient初始化的产品名严格匹配
    httpProfile.endpoint = "iam.api.ksyun.com"
    httpProfile.reqMethod = "POST"  # get请求(默认为post请求)
    httpProfile.reqTimeout = 30  # 请求超时时间，单位为秒(默认60秒)

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile

    # 实例化要请求的common client对象，clientProfile是可选的。
    client = common_client.CommonClient("cls", '2022-10-16', cred, "cn-beijing-6", profile=clientProfile)
    fpath = os.path.join(os.path.dirname(__file__), "binary.data")
    with open(fpath, "rb") as f:
        body = f.read()
    headers = {
        # 使用对应地域下真实存在的日志主题ID
        "X-CLS-TopicId": "f6c4fa6f-367a-4f14-8289-1ff6f77ed975",
        # 取值00000000000000000000000000000000，ffffffffffffffffffffffffffffffff
        "X-CLS-HashKey": "0fffffffffffffffffffffffffffffff",
        # 压缩类型
        "X-CLS-CompressType": "",
    }
    # 二进制数据作为body字节传入
    print(client.call_octet_stream("UploadLog", headers, body))
except KsyunSDKException as err:
    print(err)
