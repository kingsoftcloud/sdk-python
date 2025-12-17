import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class MonitorClient(AbstractClient):
    _apiVersion = '2018-11-14'
    _endpoint = 'monitor.api.ksyun.com'
    _service = 'monitor'
    def GetMetricStatisticsBatch(self, request):
        """批量获取监控数据
        :param request: Request instance for GetMetricStatisticsBatch.
        :type request: :class:`ksyun.client.monitor.v20181114.models.GetMetricStatisticsBatchRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetMetricStatisticsBatch", params, "application/json")
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


