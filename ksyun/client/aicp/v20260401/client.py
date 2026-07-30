import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class AicpClient(AbstractClient):
    _apiVersion = '2026-04-01'
    _endpoint = 'aicp.api.ksyun.com'
    _service = 'aicp'
    def CreateSandboxTemplate(self, request):
        """创建沙箱模板
        :param request: Request instance for CreateSandboxTemplate.
        :type request: :class:`ksyun.client.aicp.v20260401.models.CreateSandboxTemplateRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateSandboxTemplate", params, "application/json")
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
                raise KsyunSDKException(message=str(e))


    def UpdateSandboxTemplate(self, request):
        """更新沙箱模板
        :param request: Request instance for UpdateSandboxTemplate.
        :type request: :class:`ksyun.client.aicp.v20260401.models.UpdateSandboxTemplateRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateSandboxTemplate", params, "application/json")
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
                raise KsyunSDKException(message=str(e))


    def DeleteSandboxInstance(self, request):
        """删除沙箱实例
        :param request: Request instance for DeleteSandboxInstance.
        :type request: :class:`ksyun.client.aicp.v20260401.models.DeleteSandboxInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteSandboxInstance", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(message=str(e))


    def GetSandboxInstance(self, request):
        """获取沙箱实例信息
        :param request: Request instance for GetSandboxInstance.
        :type request: :class:`ksyun.client.aicp.v20260401.models.GetSandboxInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetSandboxInstance", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(message=str(e))


    def GetSandboxInstanceList(self, request):
        """查询沙箱实例列表
        :param request: Request instance for GetSandboxInstanceList.
        :type request: :class:`ksyun.client.aicp.v20260401.models.GetSandboxInstanceListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetSandboxInstanceList", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(message=str(e))


    def GetSandboxTemplateList(self, request):
        """查询沙箱模板列表
        :param request: Request instance for GetSandboxTemplateList.
        :type request: :class:`ksyun.client.aicp.v20260401.models.GetSandboxTemplateListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetSandboxTemplateList", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(message=str(e))


    def StartSandboxInstance(self, request):
        """启动沙箱实例
        :param request: Request instance for StartSandboxInstance.
        :type request: :class:`ksyun.client.aicp.v20260401.models.StartSandboxInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("StartSandboxInstance", params, "application/json")
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
                raise KsyunSDKException(message=str(e))


    def DeleteSandboxTemplate(self, request):
        """删除沙箱模板
        :param request: Request instance for DeleteSandboxTemplate.
        :type request: :class:`ksyun.client.aicp.v20260401.models.DeleteSandboxTemplateRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteSandboxTemplate", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(message=str(e))


    def GetSandboxTemplate(self, request):
        """获取沙箱模板详情
        :param request: Request instance for GetSandboxTemplate.
        :type request: :class:`ksyun.client.aicp.v20260401.models.GetSandboxTemplateRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetSandboxTemplate", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(message=str(e))


    def GetPublicImageList(self, request):
        """获取公共镜像列表
        :param request: Request instance for GetPublicImageList.
        :type request: :class:`ksyun.client.aicp.v20260401.models.GetPublicImageListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetPublicImageList", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(message=str(e))


    def UpdateSandboxInstance(self, request):
        """更新沙箱实例
        :param request: Request instance for UpdateSandboxInstance.
        :type request: :class:`ksyun.client.aicp.v20260401.models.UpdateSandboxInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateSandboxInstance", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(message=str(e))


