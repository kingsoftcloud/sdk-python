import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class RelytClient(AbstractClient):
    _apiVersion = '2024-01-17'
    _endpoint = 'relyt.api.ksyun.com'
    _service = 'relyt'

    def GetDwsuMetric(self, request):
        """获取实例监控数据
        :param request: Request instance for GetDwsuMetric.
        :type request: :class:`ksyun.client.relyt.v20240117.models.GetDwsuMetricRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetDwsuMetric", params, "application/json")
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
