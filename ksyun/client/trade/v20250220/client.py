import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class TradeClient(AbstractClient):
    _apiVersion = '2025-02-20'
    _endpoint = 'trade.api.ksyun.com'
    _service = 'trade'

    def ListInstanceSupportBillTypes(self, request):
        """实例转正，支持重新指定正式实例的计费方式，实例获取支持的计费方式列表
        :param request: Request instance for ListInstanceSupportBillTypes.
        :type request: :class:`ksyun.client.trade.v20250220.models.ListInstanceSupportBillTypesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListInstanceSupportBillTypes", params, "application/json")
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

    def AddTrialToBuyTask(self, request):
        """添加定时转正的任务，支持到期转正和指定时间点转正。 可重复提交，最后一次提交会覆盖之前的提交，相当于更新。
        :param request: Request instance for AddTrialToBuyTask.
        :type request: :class:`ksyun.client.trade.v20250220.models.AddTrialToBuyTaskRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AddTrialToBuyTask", params, "application/json")
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

    def DeleteTrialToBuyTask(self, request):
        """取消已经提交的转正任务。
        :param request: Request instance for DeleteTrialToBuyTask.
        :type request: :class:`ksyun.client.trade.v20250220.models.DeleteTrialToBuyTaskRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteTrialToBuyTask", params, "application/json")
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

    def CreateTrialToBuyNow(self, request):
        """创建转正订单，立即将实例转成正式实例。
        :param request: Request instance for CreateTrialToBuyNow.
        :type request: :class:`ksyun.client.trade.v20250220.models.CreateTrialToBuyNowRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateTrialToBuyNow", params, "application/json")
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
