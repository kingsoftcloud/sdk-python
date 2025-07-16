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
            body = self.call_judge("ListAlarmPolicy", params, "application/json")
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
            body = self.call_judge("DescribeAlarmPolicy", params, "application/json")
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
            body = self.call_judge("DescribePolicyObject", params, "application/json")
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
            body = self.call_judge("DescribeAlarmReceives", params, "application/json")
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
            body = self.call_judge("AddAlarmReceives", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("DeleteAlarmReceives", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("GetUserGroup", params, "application/json")
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
            body = self.call_judge("GetAlertUser", params, "application/json")
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

    def UpdateAlertUserStatus(self, request):
        """启用或禁用联系人
        :param request: Request instance for UpdateAlertUserStatus.
        :type request: :class:`ksyun.client.monitor.v20210101.models.UpdateAlertUserStatusRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateAlertUserStatus", params, "application/x-www-form-urlencoded")
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

    def DescribeSysEventGroupList(self, request):
        """查询事件分组列表
        :param request: Request instance for DescribeSysEventGroupList.
        :type request: :class:`ksyun.client.monitor.v20210101.models.DescribeSysEventGroupListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeSysEventGroupList", params, "application/json")
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

    def DescribeMonitorProductList(self, request):
        """描述监控云服务类别，支持项目
        :param request: Request instance for DescribeMonitorProductList.
        :type request: :class:`ksyun.client.monitor.v20210101.models.DescribeMonitorProductListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeMonitorProductList", params, "application/json")
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
