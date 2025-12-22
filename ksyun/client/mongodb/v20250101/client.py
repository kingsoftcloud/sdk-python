import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class MongodbClient(AbstractClient):
    _apiVersion = '2025-01-01'
    _endpoint = 'mongodb.api.ksyun.com'
    _service = 'mongodb'
    def DescribeDefaultParams(self, request):
        """查询默认参数模板
        :param request: Request instance for DescribeDefaultParams.
        :type request: :class:`ksyun.client.mongodb.v20250101.models.DescribeDefaultParamsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDefaultParams", params, "application/json")
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


