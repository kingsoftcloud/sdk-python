import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class KmrClient(AbstractClient):
    _apiVersion = '2024-08-14'
    _endpoint = 'kmr.api.ksyun.com'
    _service = 'kmr'
    def DetailWorkspace(self, request):
        """获取工作空间详情
        :param request: Request instance for DetailWorkspace.
        :type request: :class:`ksyun.client.kmr.v20240814.models.DetailWorkspaceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DetailWorkspace", params, "application/json")
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


    def ListWorkspaces(self, request):
        """获取工作空间列表
        :param request: Request instance for ListWorkspaces.
        :type request: :class:`ksyun.client.kmr.v20240814.models.ListWorkspacesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListWorkspaces", params, "application/json")
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


    def StartJobRun(self, request):
        """提交Spark作业
        :param request: Request instance for StartJobRun.
        :type request: :class:`ksyun.client.kmr.v20240814.models.StartJobRunRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("StartJobRun", params, "application/json")
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


    def GetJobRun(self, request):
        """获取Spark作业详情
        :param request: Request instance for GetJobRun.
        :type request: :class:`ksyun.client.kmr.v20240814.models.GetJobRunRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetJobRun", params, "application/json")
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


    def ListJobRuns(self, request):
        """获取Spark作业信息列表
        :param request: Request instance for ListJobRuns.
        :type request: :class:`ksyun.client.kmr.v20240814.models.ListJobRunsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListJobRuns", params, "application/json")
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


    def CancelJobRun(self, request):
        """停止Spark作业运行
        :param request: Request instance for CancelJobRun.
        :type request: :class:`ksyun.client.kmr.v20240814.models.CancelJobRunRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CancelJobRun", params, "application/json")
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


    def ListExecutor(self, request):
        """获取作业Executor列表
        :param request: Request instance for ListExecutor.
        :type request: :class:`ksyun.client.kmr.v20240814.models.ListExecutorRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListExecutor", params, "application/json")
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


    def StartRayJobRun(self, request):
        """提交Ray作业
        :param request: Request instance for StartRayJobRun.
        :type request: :class:`ksyun.client.kmr.v20240814.models.StartRayJobRunRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("StartRayJobRun", params, "application/json")
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


    def GetRayJobRun(self, request):
        """GetRayJobRun
        :param request: Request instance for GetRayJobRun.
        :type request: :class:`ksyun.client.kmr.v20240814.models.GetRayJobRunRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetRayJobRun", params, "application/json")
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


    def ListRayJobRuns(self, request):
        """ListRayJobRuns
        :param request: Request instance for ListRayJobRuns.
        :type request: :class:`ksyun.client.kmr.v20240814.models.ListRayJobRunsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListRayJobRuns", params, "application/json")
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


    def CancelRayJobRun(self, request):
        """停止Ray作业运行
        :param request: Request instance for CancelRayJobRun.
        :type request: :class:`ksyun.client.kmr.v20240814.models.CancelRayJobRunRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CancelRayJobRun", params, "application/json")
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


    def StartFlinkJobRun(self, request):
        """提交Flink作业
        :param request: Request instance for StartFlinkJobRun.
        :type request: :class:`ksyun.client.kmr.v20240814.models.StartFlinkJobRunRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("StartFlinkJobRun", params, "application/json")
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


    def GetFlinkJobRun(self, request):
        """获取Flink作业详情
        :param request: Request instance for GetFlinkJobRun.
        :type request: :class:`ksyun.client.kmr.v20240814.models.GetFlinkJobRunRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetFlinkJobRun", params, "application/json")
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


    def ListFlinkJobRuns(self, request):
        """获取Flink作业列表
        :param request: Request instance for ListFlinkJobRuns.
        :type request: :class:`ksyun.client.kmr.v20240814.models.ListFlinkJobRunsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListFlinkJobRuns", params, "application/json")
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


    def CancelFlinkJobRun(self, request):
        """停止Flink作业运行
        :param request: Request instance for CancelFlinkJobRun.
        :type request: :class:`ksyun.client.kmr.v20240814.models.CancelFlinkJobRunRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CancelFlinkJobRun", params, "application/json")
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


    def SuspendFlinkJobRun(self, request):
        """挂起Flink作业
        :param request: Request instance for SuspendFlinkJobRun.
        :type request: :class:`ksyun.client.kmr.v20240814.models.SuspendFlinkJobRunRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("SuspendFlinkJobRun", params, "application/json")
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


    def RestartFlinkJobRun(self, request):
        """重启Flink作业
        :param request: Request instance for RestartFlinkJobRun.
        :type request: :class:`ksyun.client.kmr.v20240814.models.RestartFlinkJobRunRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RestartFlinkJobRun", params, "application/json")
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


    def DescribeMetricList(self, request):
        """获取监控指标项
        :param request: Request instance for DescribeMetricList.
        :type request: :class:`ksyun.client.kmr.v20240814.models.DescribeMetricListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeMetricList", params, "application/json")
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


    def QueryMetrics(self, request):
        """获取监控指标详情
        :param request: Request instance for QueryMetrics.
        :type request: :class:`ksyun.client.kmr.v20240814.models.QueryMetricsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("QueryMetrics", params, "application/json")
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


