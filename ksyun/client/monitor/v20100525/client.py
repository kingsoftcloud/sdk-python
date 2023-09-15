import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class MonitorClient(AbstractClient):
    _apiVersion = '2010-05-25'
    _endpoint = 'monitor.api.ksyun.com'
    _service = 'monitor'
    def GetMetricStatistics(self, request):
        """获取监控数据
        :param request: Request instance for GetMetricStatistics.
        :type request: :class:`ksyun.client.monitor.v20100525.models.GetMetricStatisticsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetMetricStatistics", params, "application/json")
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


    def ListMetrics(self, request):
        """查看实例对应的监控指标
        :param request: Request instance for ListMetrics.
        :type request: :class:`ksyun.client.monitor.v20100525.models.ListMetricsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListMetrics", params, "application/json")
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


