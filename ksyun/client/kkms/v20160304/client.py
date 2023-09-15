import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class KkmsClient(AbstractClient):
    _apiVersion = '2016-03-04'
    _endpoint = 'kkms.api.ksyun.com'
    _service = 'kkms'
    def CreateKey(self, request):
        """创建用户的主密钥
        :param request: Request instance for CreateKey.
        :type request: :class:`ksyun.client.kkms.v20160304.models.CreateKeyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateKey", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ModifyKey(self, request):
        """修改用户主密钥
        :param request: Request instance for ModifyKey.
        :type request: :class:`ksyun.client.kkms.v20160304.models.ModifyKeyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyKey", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ModifyKeyState(self, request):
        """修改用户主密钥的状态
        :param request: Request instance for ModifyKeyState.
        :type request: :class:`ksyun.client.kkms.v20160304.models.ModifyKeyStateRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyKeyState", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DeleteKey(self, request):
        """删除用户主密钥
        :param request: Request instance for DeleteKey.
        :type request: :class:`ksyun.client.kkms.v20160304.models.DeleteKeyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteKey", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeKeys(self, request):
        """查询用户主密钥信息
        :param request: Request instance for DescribeKeys.
        :type request: :class:`ksyun.client.kkms.v20160304.models.DescribeKeysRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeKeys", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def Encrypt(self, request):
        """加密明文数据
        :param request: Request instance for Encrypt.
        :type request: :class:`ksyun.client.kkms.v20160304.models.EncryptRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("Encrypt", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def Decrypt(self, request):
        """解密密文数据
        :param request: Request instance for Decrypt.
        :type request: :class:`ksyun.client.kkms.v20160304.models.DecryptRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("Decrypt", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def GenerateDataKey(self, request):
        """创建数据密钥
        :param request: Request instance for GenerateDataKey.
        :type request: :class:`ksyun.client.kkms.v20160304.models.GenerateDataKeyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GenerateDataKey", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


