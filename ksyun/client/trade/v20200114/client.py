import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class TradeClient(AbstractClient):
    _apiVersion = '2020-01-14'
    _endpoint = 'trade.api.ksyun.com'
    _service = 'trade'
    def DescribeInstances(self, request):
        """实例信息描述
        :param request: Request instance for DescribeInstances.
        :type request: :class:`ksyun.client.trade.v20200114.models.DescribeInstancesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeInstances", params, "application/x-www-form-urlencoded")
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
