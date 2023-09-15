import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class KlogClient(AbstractClient):
    _apiVersion = '2020-07-31'
    _endpoint = 'klog.api.ksyun.com'
    _service = 'klog'
    def CreateProject(self, request):
        """创建项目
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
        """项目详情
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
        """更新项目
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
        """删除项目
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
        """查看项目列表
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
        """修个日志池
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


    def PutLogs(self, request):
        """上传日志
        :param request: Request instance for PutLogs.
        :type request: :class:`ksyun.client.klog.v20200731.models.PutLogsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("PutLogs", params, "application/json")
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
        """查询日志
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


    def GetQuickSearch(self, request):
        """获取快速查询列表
        :param request: Request instance for GetQuickSearch.
        :type request: :class:`ksyun.client.klog.v20200731.models.GetQuickSearchRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetQuickSearch", params, "application/json")
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


    def CreateDashboard(self, request):
        """创建仪表盘
        :param request: Request instance for CreateDashboard.
        :type request: :class:`ksyun.client.klog.v20200731.models.CreateDashboardRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateDashboard", params, "application/json")
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


    def DeleteDashboard(self, request):
        """删除仪表盘
        :param request: Request instance for DeleteDashboard.
        :type request: :class:`ksyun.client.klog.v20200731.models.DeleteDashboardRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteDashboard", params, "application/json")
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


    def DescribeDashboard(self, request):
        """仪表盘信息
        :param request: Request instance for DescribeDashboard.
        :type request: :class:`ksyun.client.klog.v20200731.models.DescribeDashboardRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDashboard", params, "application/json")
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


    def ListDashboards(self, request):
        """获取仪表盘列表
        :param request: Request instance for ListDashboards.
        :type request: :class:`ksyun.client.klog.v20200731.models.ListDashboardsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListDashboards", params, "application/json")
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


    def CreateChart(self, request):
        """创建图表
        :param request: Request instance for CreateChart.
        :type request: :class:`ksyun.client.klog.v20200731.models.CreateChartRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateChart", params, "application/json")
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


    def DeleteChart(self, request):
        """删除图表
        :param request: Request instance for DeleteChart.
        :type request: :class:`ksyun.client.klog.v20200731.models.DeleteChartRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteChart", params, "application/json")
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


    def GetDashboardNamesByIds(self, request):
        """获取仪表盘名称
        :param request: Request instance for GetDashboardNamesByIds.
        :type request: :class:`ksyun.client.klog.v20200731.models.GetDashboardNamesByIdsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetDashboardNamesByIds", params, "application/json")
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


    def GetChartNamesByIds(self, request):
        """获取图表名称
        :param request: Request instance for GetChartNamesByIds.
        :type request: :class:`ksyun.client.klog.v20200731.models.GetChartNamesByIdsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetChartNamesByIds", params, "application/json")
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


    def UpdateDashboard(self, request):
        """修改仪表盘
        :param request: Request instance for UpdateDashboard.
        :type request: :class:`ksyun.client.klog.v20200731.models.UpdateDashboardRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateDashboard", params, "application/json")
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


    def GetUsage(self, request):
        """获取监控
        :param request: Request instance for GetUsage.
        :type request: :class:`ksyun.client.klog.v20200731.models.GetUsageRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetUsage", params, "application/json")
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


    def SetIndexTemplate(self, request):
        """配置索引规则
        :param request: Request instance for SetIndexTemplate.
        :type request: :class:`ksyun.client.klog.v20200731.models.SetIndexTemplateRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("SetIndexTemplate", params, "application/json")
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


    def GetIndexTemplate(self, request):
        """获取当前用户已经设置的索引配置
        :param request: Request instance for GetIndexTemplate.
        :type request: :class:`ksyun.client.klog.v20200731.models.GetIndexTemplateRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetIndexTemplate", params, "application/json")
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
        """创建下载任务
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
        """列举下载任务
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


    def GetDownloadUrls(self, request):
        """获取下载Url
        :param request: Request instance for GetDownloadUrls.
        :type request: :class:`ksyun.client.klog.v20200731.models.GetDownloadUrlsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetDownloadUrls", params, "application/json")
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


    def GetMonitorData(self, request):
        """获取监控数据
        :param request: Request instance for GetMonitorData.
        :type request: :class:`ksyun.client.klog.v20200731.models.GetMonitorDataRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetMonitorData", params, "application/json")
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


    def DescribeLogErrorReason(self, request):
        """获取日志数据错误原因
        :param request: Request instance for DescribeLogErrorReason.
        :type request: :class:`ksyun.client.klog.v20200731.models.DescribeLogErrorReasonRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeLogErrorReason", params, "application/json")
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


    def DeleteEtlTask(self, request):
        """删除加工任务
        :param request: Request instance for DeleteEtlTask.
        :type request: :class:`ksyun.client.klog.v20200731.models.DeleteEtlTaskRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteEtlTask", params, "application/x-www-form-urlencoded")
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


    def StopEtlTask(self, request):
        """停止加工任务
        :param request: Request instance for StopEtlTask.
        :type request: :class:`ksyun.client.klog.v20200731.models.StopEtlTaskRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("StopEtlTask", params, "application/x-www-form-urlencoded")
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


    def StartEtlTask(self, request):
        """开始加工任务
        :param request: Request instance for StartEtlTask.
        :type request: :class:`ksyun.client.klog.v20200731.models.StartEtlTaskRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("StartEtlTask", params, "application/x-www-form-urlencoded")
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


    def ListEtlTasks(self, request):
        """查询加工任务列表
        :param request: Request instance for ListEtlTasks.
        :type request: :class:`ksyun.client.klog.v20200731.models.ListEtlTasksRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListEtlTasks", params, "application/x-www-form-urlencoded")
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


    def DescribeEtlTask(self, request):
        """查询加工任务详情
        :param request: Request instance for DescribeEtlTask.
        :type request: :class:`ksyun.client.klog.v20200731.models.DescribeEtlTaskRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeEtlTask", params, "application/x-www-form-urlencoded")
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


    def ModifyEtlTask(self, request):
        """修改加工任务
        :param request: Request instance for ModifyEtlTask.
        :type request: :class:`ksyun.client.klog.v20200731.models.ModifyEtlTaskRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyEtlTask", params, "application/x-www-form-urlencoded")
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


    def CreateEtlTask(self, request):
        """创建加工任务
        :param request: Request instance for CreateEtlTask.
        :type request: :class:`ksyun.client.klog.v20200731.models.CreateEtlTaskRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateEtlTask", params, "application/x-www-form-urlencoded")
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


    def DescribeEtlException(self, request):
        """获取加工任务异常详情
        :param request: Request instance for DescribeEtlException.
        :type request: :class:`ksyun.client.klog.v20200731.models.DescribeEtlExceptionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeEtlException", params, "application/x-www-form-urlencoded")
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


    def DescribeEtlStats(self, request):
        """获取加工任务指标统计
        :param request: Request instance for DescribeEtlStats.
        :type request: :class:`ksyun.client.klog.v20200731.models.DescribeEtlStatsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeEtlStats", params, "application/x-www-form-urlencoded")
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


    def ExecuteEtlDemo(self, request):
        """执行加工函数预览
        :param request: Request instance for ExecuteEtlDemo.
        :type request: :class:`ksyun.client.klog.v20200731.models.ExecuteEtlDemoRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ExecuteEtlDemo", params, "application/x-www-form-urlencoded")
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


    def GetUserRegion(self, request):
        """获取region
        :param request: Request instance for GetUserRegion.
        :type request: :class:`ksyun.client.klog.v20200731.models.GetUserRegionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetUserRegion", params, "application/x-www-form-urlencoded")
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


    def GetClustersByType(self, request):
        """根据类型获取集群列表
        :param request: Request instance for GetClustersByType.
        :type request: :class:`ksyun.client.klog.v20200731.models.GetClustersByTypeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetClustersByType", params, "application/x-www-form-urlencoded")
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


