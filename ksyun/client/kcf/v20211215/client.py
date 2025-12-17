import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class KcfClient(AbstractClient):
    _apiVersion = '2021-12-15'
    _endpoint = 'kcf.api.ksyun.com'
    _service = 'kcf'
    def GetLogDate(self, request):
        """查询云函数日志信息
        :param request: Request instance for GetLogDate.
        :type request: :class:`ksyun.client.kcf.v20211215.models.GetLogDateRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetLogDate", params, "application/x-www-form-urlencoded")
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


    def CreateFunction(self, request):
        """创建云函数
        :param request: Request instance for CreateFunction.
        :type request: :class:`ksyun.client.kcf.v20211215.models.CreateFunctionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateFunction", params, "application/json")
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


    def CheckFunctionService(self, request):
        """检测用户是否开通函数服务
        :param request: Request instance for CheckFunctionService.
        :type request: :class:`ksyun.client.kcf.v20211215.models.CheckFunctionServiceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CheckFunctionService", params, "application/x-www-form-urlencoded")
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


    def OpenFunctionService(self, request):
        """开通函数服务
        :param request: Request instance for OpenFunctionService.
        :type request: :class:`ksyun.client.kcf.v20211215.models.OpenFunctionServiceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("OpenFunctionService", params, "application/x-www-form-urlencoded")
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


    def DeleteFunction(self, request):
        """删除云函数
        :param request: Request instance for DeleteFunction.
        :type request: :class:`ksyun.client.kcf.v20211215.models.DeleteFunctionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteFunction", params, "application/x-www-form-urlencoded")
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


    def CreateTrigger(self, request):
        """创建触发器
        :param request: Request instance for CreateTrigger.
        :type request: :class:`ksyun.client.kcf.v20211215.models.CreateTriggerRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateTrigger", params, "application/json")
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


    def DeleteTrigger(self, request):
        """删除触发器
        :param request: Request instance for DeleteTrigger.
        :type request: :class:`ksyun.client.kcf.v20211215.models.DeleteTriggerRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteTrigger", params, "application/x-www-form-urlencoded")
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


    def ModifyFunction(self, request):
        """更新函数配置
        :param request: Request instance for ModifyFunction.
        :type request: :class:`ksyun.client.kcf.v20211215.models.ModifyFunctionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyFunction", params, "application/json")
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


    def DescribeTriggers(self, request):
        """获取触发器列表
        :param request: Request instance for DescribeTriggers.
        :type request: :class:`ksyun.client.kcf.v20211215.models.DescribeTriggersRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeTriggers", params, "application/x-www-form-urlencoded")
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


