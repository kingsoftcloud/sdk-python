import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class Cloud_advisorClient(AbstractClient):
    _apiVersion = '2025-06-10'
    _endpoint = 'cloud-advisor.api.ksyun.com'
    _service = 'cloud-advisor'
    def GetReport(self, request):
        """下载巡检报告
        :param request: Request instance for GetReport.
        :type request: :class:`ksyun.client.cloud_advisor.v20250610.models.GetReportRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetReport", params, "application/json")
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


    def CreateTask(self, request):
        """发起巡检报告
        :param request: Request instance for CreateTask.
        :type request: :class:`ksyun.client.cloud_advisor.v20250610.models.CreateTaskRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateTask", params, "application/json")
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


    def ListInspectionItem(self, request):
        """查询巡检项列表
        :param request: Request instance for ListInspectionItem.
        :type request: :class:`ksyun.client.cloud_advisor.v20250610.models.ListInspectionItemRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListInspectionItem", params, "application/json")
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


