import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class MonitorClient(AbstractClient):
    _apiVersion = '2022-01-01'
    _endpoint = 'monitor.api.ksyun.com'
    _service = 'monitor'
    def CreateAlarmPolicy(self, request):
        """创建告警策略
        :param request: Request instance for CreateAlarmPolicy.
        :type request: :class:`ksyun.client.monitor.v20220101.models.CreateAlarmPolicyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateAlarmPolicy", params, "application/x-www-form-urlencoded")
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


    def DeleteAlarmPolicy(self, request):
        """删除告警策略
        :param request: Request instance for DeleteAlarmPolicy.
        :type request: :class:`ksyun.client.monitor.v20220101.models.DeleteAlarmPolicyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteAlarmPolicy", params, "application/json")
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
