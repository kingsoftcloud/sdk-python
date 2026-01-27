import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class AicpClient(AbstractClient):
    _apiVersion = '2024-06-12'
    _endpoint = 'aicp.api.ksyun.com'
    _service = 'aicp'
    def CreateStorageConfig(self, request):
        """创建存储配置
        :param request: Request instance for CreateStorageConfig.
        :type request: :class:`ksyun.client.aicp.v20240612.models.CreateStorageConfigRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateStorageConfig", params, "application/json")
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


    def ModifyStorageConfig(self, request):
        """修改存储配置
        :param request: Request instance for ModifyStorageConfig.
        :type request: :class:`ksyun.client.aicp.v20240612.models.ModifyStorageConfigRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyStorageConfig", params, "application/json")
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


    def DescribeStorageConfigs(self, request):
        """查询存储配置
        :param request: Request instance for DescribeStorageConfigs.
        :type request: :class:`ksyun.client.aicp.v20240612.models.DescribeStorageConfigsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeStorageConfigs", params, "application/x-www-form-urlencoded")
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


    def DeleteStorageConfig(self, request):
        """删除存储配置
        :param request: Request instance for DeleteStorageConfig.
        :type request: :class:`ksyun.client.aicp.v20240612.models.DeleteStorageConfigRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteStorageConfig", params, "application/x-www-form-urlencoded")
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


    def SaveNotebookImage(self, request):
        """保存开发任务镜像
        :param request: Request instance for SaveNotebookImage.
        :type request: :class:`ksyun.client.aicp.v20240612.models.SaveNotebookImageRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("SaveNotebookImage", params, "application/x-www-form-urlencoded")
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


    def ModifyNotebook(self, request):
        """修改开发任务
        :param request: Request instance for ModifyNotebook.
        :type request: :class:`ksyun.client.aicp.v20240612.models.ModifyNotebookRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyNotebook", params, "application/json")
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


    def DeleteNotebook(self, request):
        """删除开发任务
        :param request: Request instance for DeleteNotebook.
        :type request: :class:`ksyun.client.aicp.v20240612.models.DeleteNotebookRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteNotebook", params, "application/x-www-form-urlencoded")
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


    def DescribeNotebooks(self, request):
        """查询开发任务
        :param request: Request instance for DescribeNotebooks.
        :type request: :class:`ksyun.client.aicp.v20240612.models.DescribeNotebooksRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeNotebooks", params, "application/x-www-form-urlencoded")
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


    def CreateNotebook(self, request):
        """创建开发任务
        :param request: Request instance for CreateNotebook.
        :type request: :class:`ksyun.client.aicp.v20240612.models.CreateNotebookRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateNotebook", params, "application/json")
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


    def CreateImage(self, request):
        """新建自定义镜像
        :param request: Request instance for CreateImage.
        :type request: :class:`ksyun.client.aicp.v20240612.models.CreateImageRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateImage", params, "application/json")
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


    def DeleteImage(self, request):
        """删除自定义镜像
        :param request: Request instance for DeleteImage.
        :type request: :class:`ksyun.client.aicp.v20240612.models.DeleteImageRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteImage", params, "application/x-www-form-urlencoded")
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


    def ModifyImage(self, request):
        """修改自定义镜像
        :param request: Request instance for ModifyImage.
        :type request: :class:`ksyun.client.aicp.v20240612.models.ModifyImageRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyImage", params, "application/x-www-form-urlencoded")
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


    def DescribeImages(self, request):
        """查询镜像列表
        :param request: Request instance for DescribeImages.
        :type request: :class:`ksyun.client.aicp.v20240612.models.DescribeImagesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeImages", params, "application/x-www-form-urlencoded")
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


    def StopNotebook(self, request):
        """停止开发任务
        :param request: Request instance for StopNotebook.
        :type request: :class:`ksyun.client.aicp.v20240612.models.StopNotebookRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("StopNotebook", params, "application/x-www-form-urlencoded")
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


    def StartNotebook(self, request):
        """启动开发任务
        :param request: Request instance for StartNotebook.
        :type request: :class:`ksyun.client.aicp.v20240612.models.StartNotebookRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("StartNotebook", params, "application/x-www-form-urlencoded")
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


    def GetWebIdeUrl(self, request):
        """获取开发任务连接地址
        :param request: Request instance for GetWebIdeUrl.
        :type request: :class:`ksyun.client.aicp.v20240612.models.GetWebIdeUrlRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetWebIdeUrl", params, "application/x-www-form-urlencoded")
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


    def DescribeNotebookLog(self, request):
        """查看开发机的pod日志
        :param request: Request instance for DescribeNotebookLog.
        :type request: :class:`ksyun.client.aicp.v20240612.models.DescribeNotebookLogRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeNotebookLog", params, "application/x-www-form-urlencoded")
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


    def StopNotebookSavingImage(self, request):
        """终止开发任务镜像保存
        :param request: Request instance for StopNotebookSavingImage.
        :type request: :class:`ksyun.client.aicp.v20240612.models.StopNotebookSavingImageRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("StopNotebookSavingImage", params, "application/x-www-form-urlencoded")
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


    def EnableApikeyStatus(self, request):
        """启用API Key
        :param request: Request instance for EnableApikeyStatus.
        :type request: :class:`ksyun.client.aicp.v20240612.models.EnableApikeyStatusRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("EnableApikeyStatus", params, "application/json")
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


    def ModifyApikey(self, request):
        """编辑API Key
        :param request: Request instance for ModifyApikey.
        :type request: :class:`ksyun.client.aicp.v20240612.models.ModifyApikeyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyApikey", params, "application/json")
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


    def ActivateApiService(self, request):
        """开通模型API服务
        :param request: Request instance for ActivateApiService.
        :type request: :class:`ksyun.client.aicp.v20240612.models.ActivateApiServiceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ActivateApiService", params, "application/json")
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


    def DeleteApikey(self, request):
        """删除API Key
        :param request: Request instance for DeleteApikey.
        :type request: :class:`ksyun.client.aicp.v20240612.models.DeleteApikeyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteApikey", params, "application/json")
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
        """查询模型列表(支持分页)
        :param request: Request instance for DescribeModels.
        :type request: :class:`ksyun.client.aicp.v20240612.models.DescribeModelsRequest`
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


    def CreateApikey(self, request):
        """创建API Key
        :param request: Request instance for CreateApikey.
        :type request: :class:`ksyun.client.aicp.v20240612.models.CreateApikeyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateApikey", params, "application/json")
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


    def GetModelDetail(self, request):
        """查询模型详情
        :param request: Request instance for GetModelDetail.
        :type request: :class:`ksyun.client.aicp.v20240612.models.GetModelDetailRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetModelDetail", params, "application/x-www-form-urlencoded")
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


    def DescribeApikeys(self, request):
        """查询API Key列表（分页）
        :param request: Request instance for DescribeApikeys.
        :type request: :class:`ksyun.client.aicp.v20240612.models.DescribeApikeysRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeApikeys", params, "application/x-www-form-urlencoded")
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


    def DisableApikeyStatus(self, request):
        """禁用API Key
        :param request: Request instance for DisableApikeyStatus.
        :type request: :class:`ksyun.client.aicp.v20240612.models.DisableApikeyStatusRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DisableApikeyStatus", params, "application/json")
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


    def GetApiService(self, request):
        """查询API服务开通状态
        :param request: Request instance for GetApiService.
        :type request: :class:`ksyun.client.aicp.v20240612.models.GetApiServiceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetApiService", params, "application/x-www-form-urlencoded")
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


    def GetBatchInferenceJobsFinalResultDownloadUrl(self, request):
        """查询批量推理任务最终结果下载链接
        :param request: Request instance for GetBatchInferenceJobsFinalResultDownloadUrl.
        :type request: :class:`ksyun.client.aicp.v20240612.models.GetBatchInferenceJobsFinalResultDownloadUrlRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetBatchInferenceJobsFinalResultDownloadUrl", params, "application/json")
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


    def DescribeInferenceJobsKs3AuthInfo(self, request):
        """查询批量推理任务Ks3鉴权信息
        :param request: Request instance for DescribeInferenceJobsKs3AuthInfo.
        :type request: :class:`ksyun.client.aicp.v20240612.models.DescribeInferenceJobsKs3AuthInfoRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeInferenceJobsKs3AuthInfo", params, "application/x-www-form-urlencoded")
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


    def StopBatchInferenceJob(self, request):
        """终止批量推理任务
        :param request: Request instance for StopBatchInferenceJob.
        :type request: :class:`ksyun.client.aicp.v20240612.models.StopBatchInferenceJobRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("StopBatchInferenceJob", params, "application/json")
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


    def CreateBatchInferenceJob(self, request):
        """创建批量推理任务
        :param request: Request instance for CreateBatchInferenceJob.
        :type request: :class:`ksyun.client.aicp.v20240612.models.CreateBatchInferenceJobRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateBatchInferenceJob", params, "application/json")
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


    def ModifyBatchInferenceJob(self, request):
        """更新批量推理任务（修改jobName和jobDesc）
        :param request: Request instance for ModifyBatchInferenceJob.
        :type request: :class:`ksyun.client.aicp.v20240612.models.ModifyBatchInferenceJobRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyBatchInferenceJob", params, "application/json")
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


    def DescribeBatchInferenceJobs(self, request):
        """查询批量推理任务(支持分页，按创建用户过滤)
        :param request: Request instance for DescribeBatchInferenceJobs.
        :type request: :class:`ksyun.client.aicp.v20240612.models.DescribeBatchInferenceJobsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeBatchInferenceJobs", params, "application/x-www-form-urlencoded")
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


    def DeleteBatchInferenceJob(self, request):
        """删除批量推理任务
        :param request: Request instance for DeleteBatchInferenceJob.
        :type request: :class:`ksyun.client.aicp.v20240612.models.DeleteBatchInferenceJobRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteBatchInferenceJob", params, "application/json")
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


    def EnableModels(self, request):
        """开通模型，支持批量
        :param request: Request instance for EnableModels.
        :type request: :class:`ksyun.client.aicp.v20240612.models.EnableModelsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("EnableModels", params, "application/json")
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


    def DescribeModelQuotas(self, request):
        """查询模型配额列表
        :param request: Request instance for DescribeModelQuotas.
        :type request: :class:`ksyun.client.aicp.v20240612.models.DescribeModelQuotasRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeModelQuotas", params, "application/x-www-form-urlencoded")
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


    def DisableModels(self, request):
        """禁用对应模型
        :param request: Request instance for DisableModels.
        :type request: :class:`ksyun.client.aicp.v20240612.models.DisableModelsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DisableModels", params, "application/json")
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


    def EnableOverFreeLimit(self, request):
        """免费配额用完后禁用对应模型
        :param request: Request instance for EnableOverFreeLimit.
        :type request: :class:`ksyun.client.aicp.v20240612.models.EnableOverFreeLimitRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("EnableOverFreeLimit", params, "application/json")
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


    def DisableOverFreeLimit(self, request):
        """即免费配额用完后继续使用计费配额
        :param request: Request instance for DisableOverFreeLimit.
        :type request: :class:`ksyun.client.aicp.v20240612.models.DisableOverFreeLimitRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DisableOverFreeLimit", params, "application/json")
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


    def CreateTrainJob(self, request):
        """创建训练任务
        :param request: Request instance for CreateTrainJob.
        :type request: :class:`ksyun.client.aicp.v20240612.models.CreateTrainJobRequest`
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


    def DescribeTrainJobEvents(self, request):
        """查询训练任务pod事件
        :param request: Request instance for DescribeTrainJobEvents.
        :type request: :class:`ksyun.client.aicp.v20240612.models.DescribeTrainJobEventsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeTrainJobEvents", params, "application/x-www-form-urlencoded")
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


    def StopTrainJob(self, request):
        """关停训练任务
        :param request: Request instance for StopTrainJob.
        :type request: :class:`ksyun.client.aicp.v20240612.models.StopTrainJobRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("StopTrainJob", params, "application/x-www-form-urlencoded")
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


    def DescribeTrainJob(self, request):
        """查询训练任务
        :param request: Request instance for DescribeTrainJob.
        :type request: :class:`ksyun.client.aicp.v20240612.models.DescribeTrainJobRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeTrainJob", params, "application/x-www-form-urlencoded")
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


    def StartTrainJob(self, request):
        """开启训练任务
        :param request: Request instance for StartTrainJob.
        :type request: :class:`ksyun.client.aicp.v20240612.models.StartTrainJobRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("StartTrainJob", params, "application/x-www-form-urlencoded")
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


    def DeleteTrainJob(self, request):
        """删除训练任务
        :param request: Request instance for DeleteTrainJob.
        :type request: :class:`ksyun.client.aicp.v20240612.models.DeleteTrainJobRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteTrainJob", params, "application/x-www-form-urlencoded")
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


    def ModifyTrainJob(self, request):
        """修改训练任务
        :param request: Request instance for ModifyTrainJob.
        :type request: :class:`ksyun.client.aicp.v20240612.models.ModifyTrainJobRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyTrainJob", params, "application/json")
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


    def DescribeTrainJobPodLogs(self, request):
        """查询训练任务pod日志
        :param request: Request instance for DescribeTrainJobPodLogs.
        :type request: :class:`ksyun.client.aicp.v20240612.models.DescribeTrainJobPodLogsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeTrainJobPodLogs", params, "application/x-www-form-urlencoded")
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


    def DescribeTrainJobPods(self, request):
        """查询训练任务pod列表
        :param request: Request instance for DescribeTrainJobPods.
        :type request: :class:`ksyun.client.aicp.v20240612.models.DescribeTrainJobPodsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeTrainJobPods", params, "application/x-www-form-urlencoded")
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


    def DescribeResourcePools(self, request):
        """查询资源组列表
        :param request: Request instance for DescribeResourcePools.
        :type request: :class:`ksyun.client.aicp.v20240612.models.DescribeResourcePoolsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeResourcePools", params, "application/x-www-form-urlencoded")
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


    def DescribeResourcePoolInstances(self, request):
        """查询资源组节点列表
        :param request: Request instance for DescribeResourcePoolInstances.
        :type request: :class:`ksyun.client.aicp.v20240612.models.DescribeResourcePoolInstancesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeResourcePoolInstances", params, "application/x-www-form-urlencoded")
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


    def CreateInferenceEndpoint(self, request):
        """创建接入点
        :param request: Request instance for CreateInferenceEndpoint.
        :type request: :class:`ksyun.client.aicp.v20240612.models.CreateInferenceEndpointRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateInferenceEndpoint", params, "application/json")
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


    def DescribeInferenceEndpoints(self, request):
        """查询接入点
        :param request: Request instance for DescribeInferenceEndpoints.
        :type request: :class:`ksyun.client.aicp.v20240612.models.DescribeInferenceEndpointsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeInferenceEndpoints", params, "application/x-www-form-urlencoded")
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


    def EnableEndpointRateLimit(self, request):
        """开启接入点限流
        :param request: Request instance for EnableEndpointRateLimit.
        :type request: :class:`ksyun.client.aicp.v20240612.models.EnableEndpointRateLimitRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("EnableEndpointRateLimit", params, "application/json")
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


    def UpdateInferenceEndpoint(self, request):
        """创建接入点
        :param request: Request instance for UpdateInferenceEndpoint.
        :type request: :class:`ksyun.client.aicp.v20240612.models.UpdateInferenceEndpointRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateInferenceEndpoint", params, "application/json")
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


    def StartInferenceEndpoint(self, request):
        """开启接入点
        :param request: Request instance for StartInferenceEndpoint.
        :type request: :class:`ksyun.client.aicp.v20240612.models.StartInferenceEndpointRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("StartInferenceEndpoint", params, "application/json")
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


    def StopInferenceEndpoint(self, request):
        """关闭接入点
        :param request: Request instance for StopInferenceEndpoint.
        :type request: :class:`ksyun.client.aicp.v20240612.models.StopInferenceEndpointRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("StopInferenceEndpoint", params, "application/json")
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


    def DeleteInferenceEndpoint(self, request):
        """删除接入点
        :param request: Request instance for DeleteInferenceEndpoint.
        :type request: :class:`ksyun.client.aicp.v20240612.models.DeleteInferenceEndpointRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteInferenceEndpoint", params, "application/json")
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


    def DisableEndpointRateLimit(self, request):
        """关闭接入点限流
        :param request: Request instance for DisableEndpointRateLimit.
        :type request: :class:`ksyun.client.aicp.v20240612.models.DisableEndpointRateLimitRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DisableEndpointRateLimit", params, "application/json")
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


    def DescribeResourcePoolInstanceTasks(self, request):
        """查询节点上运行的任务
        :param request: Request instance for DescribeResourcePoolInstanceTasks.
        :type request: :class:`ksyun.client.aicp.v20240612.models.DescribeResourcePoolInstanceTasksRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeResourcePoolInstanceTasks", params, "application/x-www-form-urlencoded")
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


    def SetKcrPersonalToken(self, request):
        """配置个人版镜像仓库访问凭证
        :param request: Request instance for SetKcrPersonalToken.
        :type request: :class:`ksyun.client.aicp.v20240612.models.SetKcrPersonalTokenRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("SetKcrPersonalToken", params, "application/json")
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


    def DescribeQueues(self, request):
        """查询资源组队列
        :param request: Request instance for DescribeQueues.
        :type request: :class:`ksyun.client.aicp.v20240612.models.DescribeQueuesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeQueues", params, "application/x-www-form-urlencoded")
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


