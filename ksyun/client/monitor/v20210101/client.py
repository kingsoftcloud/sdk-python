import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class MonitorClient(AbstractClient):
    _apiVersion = '2021-01-01'
    _endpoint = 'monitor.api.ksyun.com'
    _service = 'monitor'
    def ListAlarmPolicy(self, request):
        """查询告警策略
        :param request: Request instance for ListAlarmPolicy.
        :type request: :class:`ksyun.client.monitor.v20210101.models.ListAlarmPolicyRequest`
        """
        try:
            params = request._serialize()
            body = self.call("ListAlarmPolicy", params)
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


    def DescribeAlarmPolicy(self, request):
        """查询告警策略详细信息
        :param request: Request instance for DescribeAlarmPolicy.
        :type request: :class:`ksyun.client.monitor.v20210101.models.DescribeAlarmPolicyRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DescribeAlarmPolicy", params)
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


    def DescribePolicyObject(self, request):
        """查询告警策略关联实例明细
        :param request: Request instance for DescribePolicyObject.
        :type request: :class:`ksyun.client.monitor.v20210101.models.DescribePolicyObjectRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DescribePolicyObject", params)
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


    def DescribeAlarmReceives(self, request):
        """查询告警策略关联的接收人
        :param request: Request instance for DescribeAlarmReceives.
        :type request: :class:`ksyun.client.monitor.v20210101.models.DescribeAlarmReceivesRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DescribeAlarmReceives", params)
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


    def AddAlarmReceives(self, request):
        """添加告警策略关联的接收人
        :param request: Request instance for AddAlarmReceives.
        :type request: :class:`ksyun.client.monitor.v20210101.models.AddAlarmReceivesRequest`
        """
        try:
            params = request._serialize()
            body = self.call("AddAlarmReceives", params)
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


    def DeleteAlarmReceives(self, request):
        """删除告警策略关联的接收人
        :param request: Request instance for DeleteAlarmReceives.
        :type request: :class:`ksyun.client.monitor.v20210101.models.DeleteAlarmReceivesRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DeleteAlarmReceives", params)
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


    def GetUserGroup(self, request):
        """查询联系组
        :param request: Request instance for GetUserGroup.
        :type request: :class:`ksyun.client.monitor.v20210101.models.GetUserGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call("GetUserGroup", params)
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


    def GetAlertUser(self, request):
        """查询联系人
        :param request: Request instance for GetAlertUser.
        :type request: :class:`ksyun.client.monitor.v20210101.models.GetAlertUserRequest`
        """
        try:
            params = request._serialize()
            body = self.call("GetAlertUser", params)
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
        """获取指标接口
        :param request: Request instance for ListMetrics.
        :type request: :class:`ksyun.client.monitor.v20210101.models.ListMetricsRequest`
        """
        try:
            params = request._serialize()
            body = self.call("ListMetrics", params)
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


