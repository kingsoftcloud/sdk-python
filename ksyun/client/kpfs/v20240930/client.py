import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class KpfsClient(AbstractClient):
    _apiVersion = '2024-09-30'
    _endpoint = 'kpfs.api.ksyun.com'
    _service = 'kpfs'
    def UpdatePerformanceOnePosixAcl(self, request):
        """修改访问授权
        :param request: Request instance for UpdatePerformanceOnePosixAcl.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.UpdatePerformanceOnePosixAclRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdatePerformanceOnePosixAcl", params, "application/json")
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


    def DescribePerformanceOnePosixAclList(self, request):
        """查询访问授权列表
        :param request: Request instance for DescribePerformanceOnePosixAclList.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.DescribePerformanceOnePosixAclListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribePerformanceOnePosixAclList", params, "application/json")
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


    def ManageDataFlowTask(self, request):
        """变更数据流动任务
        :param request: Request instance for ManageDataFlowTask.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.ManageDataFlowTaskRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ManageDataFlowTask", params, "application/x-www-form-urlencoded")
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


    def CreateDataFlowStrategy(self, request):
        """创建数据流动策略
        :param request: Request instance for CreateDataFlowStrategy.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.CreateDataFlowStrategyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateDataFlowStrategy", params, "application/x-www-form-urlencoded")
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


    def ModifyDataFlowTask(self, request):
        """变更数据流动任务
        :param request: Request instance for ModifyDataFlowTask.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.ModifyDataFlowTaskRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyDataFlowTask", params, "application/x-www-form-urlencoded")
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


    def DescribeDataFlowTaskList(self, request):
        """创建数据流动策略
        :param request: Request instance for DescribeDataFlowTaskList.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.DescribeDataFlowTaskListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDataFlowTaskList", params, "application/x-www-form-urlencoded")
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


    def ActivateDataFlowTask(self, request):
        """启动数据流动导入任务
        :param request: Request instance for ActivateDataFlowTask.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.ActivateDataFlowTaskRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ActivateDataFlowTask", params, "application/x-www-form-urlencoded")
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


    def DeleteDataFlowStrategy(self, request):
        """删除数据流动策略
        :param request: Request instance for DeleteDataFlowStrategy.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.DeleteDataFlowStrategyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteDataFlowStrategy", params, "application/x-www-form-urlencoded")
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


    def DescribeDataFlowStrategyList(self, request):
        """创建数据流动列表
        :param request: Request instance for DescribeDataFlowStrategyList.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.DescribeDataFlowStrategyListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDataFlowStrategyList", params, "application/x-www-form-urlencoded")
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


