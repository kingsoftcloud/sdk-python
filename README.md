# 简介
欢迎使用金山云开发者工具套件（SDK）
为方便 Python 开发者调试和接入金山云产品 API，这里向您介绍适用于 Python 的金山云开发工具包，并提供首次使用开发工具包的简单示例。让您快速获取金山云 Python SDK 并开始调用。

# 依赖环境

1. 依赖环境：Python 2.7, 3.6-3.10 版本。
2. 从 金山云控制台 开通相应产品。
3. 获取 SecretID、SecretKey 以及调用地址（endpoint)，具体参考各产品说明。

# 获取安装

安装 Python SDK 前，先获取安全凭证。在第一次使用云 API 之前，用户首先需要在金山云控制台上申请安全凭证，安全凭证包括 SecretID 和 SecretKey, SecretID 是用于标识 API 调用者的身份，SecretKey 是用于加密签名字符串和服务器端验证签名字符串的密钥。SecretKey 必须严格保管，避免泄露。

## 通过 Pip 安装(推荐)

您可以通过 pip 安装方式将金山云 API Python SDK 安装到您的项目中，如果您的项目环境尚未安装 pip，请详细参见 [pip](https://pip.pypa.io/en/stable/installing/?spm=a3c0i.o32026zh.a3.6.74134958lLSo6o)官网 安装。

通过pip方式安装或更新请在命令行中执行以下命令:

```bash
pip install --upgrade kingsoftcloud-sdk-python
```

请注意，如果同时有 python2 和 python3 环境， python3 环境需要使用 pip3 命令安装。

## 通过源码包安装

前往 [Github 仓库](https://github.com/kingsoftcloud/sdk-python) 下载最新代码，解压后

    $ cd kingsoftcloud-sdk-python
    $ python setup.py install

# 示例

以调用子用户列表接口为例。

```python
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
```

**注意，您必须明确知道您调用的接口所需参数，否则可能会调用失败。**

# 更多示例
参见金山云控制台-API Explorer-对应服务-SDK示例

## 代理

如果是有代理的环境下，可通过两种方式设置代理

1. 在初始化HttpProfile时指定proxy，参考[example](https://github.com/ksyun/ksyun-sdk-python/blob/master/examples/cvm/v20170312/describe_zones.py)
2. 需要设置系统环境变量 `https_proxy`

否则可能无法正常调用，抛出连接超时的异常。