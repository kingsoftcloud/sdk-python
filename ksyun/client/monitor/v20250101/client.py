import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class MonitorClient(AbstractClient):
    _apiVersion = '2025-01-01'
    _endpoint = 'monitor.api.ksyun.com'
    _service = 'monitor'
    def DescribeAlertingResources(self, request):
        """正在告警资源列表
        :param request: Request instance for DescribeAlertingResources.
        :type request: :class:`ksyun.client.monitor.v20250101.models.DescribeAlertingResourcesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeAlertingResources", params, "application/json")
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

    def DescribeSystemEventAttributes(self, request):
        """查询系统事件详情
        :param request: Request instance for DescribeSystemEventAttributes.
        :type request: :class:`ksyun.client.monitor.v20250101.models.DescribeSystemEventAttributesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeSystemEventAttributes", params, "application/x-www-form-urlencoded")
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
