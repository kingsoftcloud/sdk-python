import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class KmrClient(AbstractClient):
    _apiVersion = '2023-12-31'
    _endpoint = 'kmr.api.ksyun.com'
    _service = 'kmr'
    def ListInstances(self, request):
        """实例列表
        :param request: Request instance for ListInstances.
        :type request: :class:`ksyun.client.kmr.v20231231.models.ListInstancesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListInstances", params, "application/x-www-form-urlencoded")
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


    def GetInstanceDetail(self, request):
        """实例信息
        :param request: Request instance for GetInstanceDetail.
        :type request: :class:`ksyun.client.kmr.v20231231.models.GetInstanceDetailRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetInstanceDetail", params, "application/x-www-form-urlencoded")
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


    def ListAutoScaleHistory(self, request):
        """查看弹性伸缩策略历史
        :param request: Request instance for ListAutoScaleHistory.
        :type request: :class:`ksyun.client.kmr.v20231231.models.ListAutoScaleHistoryRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListAutoScaleHistory", params, "application/x-www-form-urlencoded")
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


    def CreateAutoScalePolicy(self, request):
        """新增弹性伸缩策略
        :param request: Request instance for CreateAutoScalePolicy.
        :type request: :class:`ksyun.client.kmr.v20231231.models.CreateAutoScalePolicyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateAutoScalePolicy", params, "application/x-www-form-urlencoded")
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


    def ListAutoScalePolicy(self, request):
        """查看弹性伸缩策略
        :param request: Request instance for ListAutoScalePolicy.
        :type request: :class:`ksyun.client.kmr.v20231231.models.ListAutoScalePolicyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListAutoScalePolicy", params, "application/x-www-form-urlencoded")
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


    def DeleteAutoScalePolicy(self, request):
        """删除弹性伸缩策略
        :param request: Request instance for DeleteAutoScalePolicy.
        :type request: :class:`ksyun.client.kmr.v20231231.models.DeleteAutoScalePolicyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteAutoScalePolicy", params, "application/x-www-form-urlencoded")
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


