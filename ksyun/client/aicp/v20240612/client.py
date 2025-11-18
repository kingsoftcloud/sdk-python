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


