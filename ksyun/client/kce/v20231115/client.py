import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class KceClient(AbstractClient):
    _apiVersion = '2023-11-15'
    _endpoint = 'kce.api.ksyun.com'
    _service = 'kce'

    def DescribeCluster(self, request):
        """查询集群列表，只加载集群基本信息，不会加载组件详情等信息
        :param request: Request instance for DescribeCluster.
        :type request: :class:`ksyun.client.kce.v20231115.models.DescribeClusterRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeCluster", params, "application/x-www-form-urlencoded")
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
