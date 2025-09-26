import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class TradeClient(AbstractClient):
    _apiVersion = '2025-08-28'
    _endpoint = 'trade.api.ksyun.com'
    _service = 'trade'

    def QueryInstances(self, request):
        """根据搜索条件查询实例列表
        :param request: Request instance for QueryInstances.
        :type request: :class:`ksyun.client.trade.v20250828.models.QueryInstancesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("QueryInstances", params, "application/json")
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
