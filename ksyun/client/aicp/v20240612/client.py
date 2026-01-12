import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class AicpClient(AbstractClient):
    _apiVersion = '2024-06-12'
    _endpoint = 'aicp.api.ksyun.com'
    _service = 'aicp'
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
                raise KsyunSDKException(e.message, e.message)


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
                raise KsyunSDKException(e.message, e.message)


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
                raise KsyunSDKException(e.message, e.message)


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
                raise KsyunSDKException(e.message, e.message)


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
                raise KsyunSDKException(e.message, e.message)


    def StopNotebook(self, request):
        """停止开发任务
        :param request: Request instance for StopNotebook.
        :type request: :class:`ksyun.client.aicp.v20240612.models.StopNotebookRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("StopNotebook", params, "application/json")
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
                raise KsyunSDKException(e.message, e.message)


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
                raise KsyunSDKException(e.message, e.message)


    def DescribeNotebookEvents(self, request):
        """查询开发任务事件列表
        :param request: Request instance for DescribeNotebookEvents.
        :type request: :class:`ksyun.client.aicp.v20240612.models.DescribeNotebookEventsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeNotebookEvents", params, "application/x-www-form-urlencoded")
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


    def DescribeNotebookLog(self, request):
        """查看开发机日志
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
                raise KsyunSDKException(e.message, e.message)


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
                raise KsyunSDKException(e.message, e.message)


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
                raise KsyunSDKException(e.message, e.message)


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
                raise KsyunSDKException(e.message, e.message)


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
                raise KsyunSDKException(e.message, e.message)


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
                raise KsyunSDKException(e.message, e.message)


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
                raise KsyunSDKException(e.message, e.message)


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
                raise KsyunSDKException(e.message, e.message)


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
                raise KsyunSDKException(e.message, e.message)


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
                raise KsyunSDKException(e.message, e.message)


    def QueryTokenData(self, request):
        """查询模型API token用量
        :param request: Request instance for QueryTokenData.
        :type request: :class:`ksyun.client.aicp.v20240612.models.QueryTokenDataRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("QueryTokenData", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


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
                raise KsyunSDKException(e.message, e.message)


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
                raise KsyunSDKException(e.message, e.message)


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
                raise KsyunSDKException(e.message, e.message)


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
                raise KsyunSDKException(e.message, e.message)


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
                raise KsyunSDKException(e.message, e.message)


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
                raise KsyunSDKException(e.message, e.message)


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
                raise KsyunSDKException(e.message, e.message)


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
                raise KsyunSDKException(e.message, e.message)


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
                raise KsyunSDKException(e.message, e.message)


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
                raise KsyunSDKException(e.message, e.message)


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
                raise KsyunSDKException(e.message, e.message)


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
                raise KsyunSDKException(e.message, e.message)


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
                raise KsyunSDKException(e.message, e.message)


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
                raise KsyunSDKException(e.message, e.message)


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
                raise KsyunSDKException(e.message, e.message)


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
                raise KsyunSDKException(e.message, e.message)


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
                raise KsyunSDKException(e.message, e.message)


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
                raise KsyunSDKException(e.message, e.message)


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
                raise KsyunSDKException(e.message, e.message)


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
                raise KsyunSDKException(e.message, e.message)


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
                raise KsyunSDKException(e.message, e.message)


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
                raise KsyunSDKException(e.message, e.message)


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
                raise KsyunSDKException(e.message, e.message)


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
                raise KsyunSDKException(e.message, e.message)


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
                raise KsyunSDKException(e.message, e.message)


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
                raise KsyunSDKException(e.message, e.message)


    def StartInferenceEndpoint(self, request):
        """关闭接入点
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
                raise KsyunSDKException(e.message, e.message)


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
                raise KsyunSDKException(e.message, e.message)


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
                raise KsyunSDKException(e.message, e.message)


