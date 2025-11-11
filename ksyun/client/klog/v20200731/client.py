import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class KlogClient(AbstractClient):
    _apiVersion = '2020-07-31'
    _endpoint = 'klog.api.ksyun.com'
    _service = 'klog'
    def CreateProject(self, request):
        """创建新工程
        :param request: Request instance for CreateProject.
        :type request: :class:`ksyun.client.klog.v20200731.models.CreateProjectRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateProject", params, "application/json")
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


    def DescribeProject(self, request):
        """展示工程详情
        :param request: Request instance for DescribeProject.
        :type request: :class:`ksyun.client.klog.v20200731.models.DescribeProjectRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeProject", params, "application/json")
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


    def UpdateProject(self, request):
        """更新工程信息
        :param request: Request instance for UpdateProject.
        :type request: :class:`ksyun.client.klog.v20200731.models.UpdateProjectRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateProject", params, "application/json")
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


    def DeleteProject(self, request):
        """删除该工程
        :param request: Request instance for DeleteProject.
        :type request: :class:`ksyun.client.klog.v20200731.models.DeleteProjectRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteProject", params, "application/json")
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


    def ListProjects(self, request):
        """查看工程列表
        :param request: Request instance for ListProjects.
        :type request: :class:`ksyun.client.klog.v20200731.models.ListProjectsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListProjects", params, "application/json")
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


    def CreateLogPool(self, request):
        """创建日志池
        :param request: Request instance for CreateLogPool.
        :type request: :class:`ksyun.client.klog.v20200731.models.CreateLogPoolRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateLogPool", params, "application/json")
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


    def DescribeLogPool(self, request):
        """日志池详情
        :param request: Request instance for DescribeLogPool.
        :type request: :class:`ksyun.client.klog.v20200731.models.DescribeLogPoolRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeLogPool", params, "application/json")
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


    def UpdateLogPool(self, request):
        """修改日志池
        :param request: Request instance for UpdateLogPool.
        :type request: :class:`ksyun.client.klog.v20200731.models.UpdateLogPoolRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateLogPool", params, "application/json")
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


    def DeleteLogPool(self, request):
        """删除日志池
        :param request: Request instance for DeleteLogPool.
        :type request: :class:`ksyun.client.klog.v20200731.models.DeleteLogPoolRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteLogPool", params, "application/json")
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


    def ListLogPools(self, request):
        """获取日志池列表
        :param request: Request instance for ListLogPools.
        :type request: :class:`ksyun.client.klog.v20200731.models.ListLogPoolsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListLogPools", params, "application/json")
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


    def GetLogs(self, request):
        """查询日志池
        :param request: Request instance for GetLogs.
        :type request: :class:`ksyun.client.klog.v20200731.models.GetLogsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetLogs", params, "application/json")
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


    def CreateQuickSearch(self, request):
        """存为快速查询
        :param request: Request instance for CreateQuickSearch.
        :type request: :class:`ksyun.client.klog.v20200731.models.CreateQuickSearchRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateQuickSearch", params, "application/json")
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


    def ListQuickSearchs(self, request):
        """获取快速查询列表
        :param request: Request instance for ListQuickSearchs.
        :type request: :class:`ksyun.client.klog.v20200731.models.ListQuickSearchsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListQuickSearchs", params, "application/json")
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


    def DeleteQuickSearchs(self, request):
        """删除快速查询
        :param request: Request instance for DeleteQuickSearchs.
        :type request: :class:`ksyun.client.klog.v20200731.models.DeleteQuickSearchsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteQuickSearchs", params, "application/json")
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


    def CreateDownloadTask(self, request):
        """创建日志下载任务
        :param request: Request instance for CreateDownloadTask.
        :type request: :class:`ksyun.client.klog.v20200731.models.CreateDownloadTaskRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateDownloadTask", params, "application/json")
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


    def ListDownloadTasks(self, request):
        """查看日志下载任务
        :param request: Request instance for ListDownloadTasks.
        :type request: :class:`ksyun.client.klog.v20200731.models.ListDownloadTasksRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListDownloadTasks", params, "application/json")
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


