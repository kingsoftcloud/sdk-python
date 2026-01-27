import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class AicpClient(AbstractClient):
    _apiVersion = '2025-12-12'
    _endpoint = 'aicp.api.ksyun.com'
    _service = 'aicp'
    def CreateTrainJob(self, request):
        """创建训练任务
        :param request: Request instance for CreateTrainJob.
        :type request: :class:`ksyun.client.aicp.v20251212.models.CreateTrainJobRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateTrainJob", params, "application/json")
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


    def DescribeTrainJobs(self, request):
        """查询训练任务
        :param request: Request instance for DescribeTrainJobs.
        :type request: :class:`ksyun.client.aicp.v20251212.models.DescribeTrainJobsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeTrainJobs", params, "application/x-www-form-urlencoded")
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


    def ModifyModelAccess(self, request):
        """更新模型访问权限
        :param request: Request instance for ModifyModelAccess.
        :type request: :class:`ksyun.client.aicp.v20251212.models.ModifyModelAccessRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyModelAccess", params, "application/json")
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


    def CreateModelAndVersion(self, request):
        """创建模型及版本
        :param request: Request instance for CreateModelAndVersion.
        :type request: :class:`ksyun.client.aicp.v20251212.models.CreateModelAndVersionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateModelAndVersion", params, "application/json")
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


    def ModifyModel(self, request):
        """更新模型信息
        :param request: Request instance for ModifyModel.
        :type request: :class:`ksyun.client.aicp.v20251212.models.ModifyModelRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyModel", params, "application/x-www-form-urlencoded")
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


    def DescribeModels(self, request):
        """查询模型列表
        :param request: Request instance for DescribeModels.
        :type request: :class:`ksyun.client.aicp.v20251212.models.DescribeModelsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeModels", params, "application/x-www-form-urlencoded")
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


    def DeleteModel(self, request):
        """删除指定模型
        :param request: Request instance for DeleteModel.
        :type request: :class:`ksyun.client.aicp.v20251212.models.DeleteModelRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteModel", params, "application/x-www-form-urlencoded")
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


    def CreateModelVersion(self, request):
        """创建推理模型版本
        :param request: Request instance for CreateModelVersion.
        :type request: :class:`ksyun.client.aicp.v20251212.models.CreateModelVersionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateModelVersion", params, "application/json")
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


    def DeleteModelVersion(self, request):
        """删除模型版本
        :param request: Request instance for DeleteModelVersion.
        :type request: :class:`ksyun.client.aicp.v20251212.models.DeleteModelVersionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteModelVersion", params, "application/x-www-form-urlencoded")
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


    def ModifyModelVersion(self, request):
        """更新模型版本
        :param request: Request instance for ModifyModelVersion.
        :type request: :class:`ksyun.client.aicp.v20251212.models.ModifyModelVersionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyModelVersion", params, "application/json")
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


    def DescribeModelVersions(self, request):
        """查询模型版本
        :param request: Request instance for DescribeModelVersions.
        :type request: :class:`ksyun.client.aicp.v20251212.models.DescribeModelVersionsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeModelVersions", params, "application/x-www-form-urlencoded")
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


    def DescribeFormatAndFrameworks(self, request):
        """描述模型格式及框架
        :param request: Request instance for DescribeFormatAndFrameworks.
        :type request: :class:`ksyun.client.aicp.v20251212.models.DescribeFormatAndFrameworksRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeFormatAndFrameworks", params, "application/x-www-form-urlencoded")
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


