import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class SksClient(AbstractClient):
    _apiVersion = '2015-11-01'
    _endpoint = 'sks.api.ksyun.com'
    _service = 'sks'
    def CreateKey(self, request):
        """创建密钥
        :param request: Request instance for CreateKey.
        :type request: :class:`ksyun.client.sks.v20151101.models.CreateKeyRequest`
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


    def ImportKey(self, request):
        """导入密钥
        :param request: Request instance for ImportKey.
        :type request: :class:`ksyun.client.sks.v20151101.models.ImportKeyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ImportKey", params, "application/x-www-form-urlencoded")
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
        """删除密钥
        :param request: Request instance for DeleteKey.
        :type request: :class:`ksyun.client.sks.v20151101.models.DeleteKeyRequest`
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


    def ModifyKey(self, request):
        """修改密钥信息
        :param request: Request instance for ModifyKey.
        :type request: :class:`ksyun.client.sks.v20151101.models.ModifyKeyRequest`
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


    def DescribeKeys(self, request):
        """获取密钥列表信息
        :param request: Request instance for DescribeKeys.
        :type request: :class:`ksyun.client.sks.v20151101.models.DescribeKeysRequest`
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


