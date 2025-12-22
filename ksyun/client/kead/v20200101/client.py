import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class KeadClient(AbstractClient):
    _apiVersion = '2020-01-01'
    _endpoint = 'kead.api.ksyun.com'
    _service = 'kead'
    def DescribeKead(self, request):
        """高防包列表
        :param request: Request instance for DescribeKead.
        :type request: :class:`ksyun.client.kead.v20200101.models.DescribeKeadRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeKead", params, "application/json")
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


    def DescribeKeadIp(self, request):
        """高防包IP列表
        :param request: Request instance for DescribeKeadIp.
        :type request: :class:`ksyun.client.kead.v20200101.models.DescribeKeadIpRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeKeadIp", params, "application/json")
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


    def DescribeBlockIp(self, request):
        """查询封禁IP
        :param request: Request instance for DescribeBlockIp.
        :type request: :class:`ksyun.client.kead.v20200101.models.DescribeBlockIpRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeBlockIp", params, "application/json")
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


