import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class DtsClient(AbstractClient):
    _apiVersion = '2018-01-08'
    _endpoint = 'dts.api.ksyun.com'
    _service = 'dts'
    def SchemaStruct(self, request):
        """获取源库库表结构
        :param request: Request instance for SchemaStruct.
        :type request: :class:`ksyun.client.dts.v20180108.models.SchemaStructRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("SchemaStruct", params, "application/x-www-form-urlencoded")
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


    def ConnectivityCheck(self, request):
        """源库/目标库连通性
        :param request: Request instance for ConnectivityCheck.
        :type request: :class:`ksyun.client.dts.v20180108.models.ConnectivityCheckRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ConnectivityCheck", params, "application/x-www-form-urlencoded")
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


    def CreatePrecheck(self, request):
        """创建预检查
        :param request: Request instance for CreatePrecheck.
        :type request: :class:`ksyun.client.dts.v20180108.models.CreatePrecheckRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreatePrecheck", params, "application/json")
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


    def CreateTask(self, request):
        """创建任务(含迁移/同步/订阅)
        :param request: Request instance for CreateTask.
        :type request: :class:`ksyun.client.dts.v20180108.models.CreateTaskRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateTask", params, "application/x-www-form-urlencoded")
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


    def DescribeTask(self, request):
        """查询任务(列表/详情)
        :param request: Request instance for DescribeTask.
        :type request: :class:`ksyun.client.dts.v20180108.models.DescribeTaskRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeTask", params, "application/json")
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


    def OperateTask(self, request):
        """任务操作(启动/暂停/停止/删除)
        :param request: Request instance for OperateTask.
        :type request: :class:`ksyun.client.dts.v20180108.models.OperateTaskRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("OperateTask", params, "application/x-www-form-urlencoded")
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


    def DescribeConnConfig(self, request):
        """查询任务配置信息(通过配置ID获取)
        :param request: Request instance for DescribeConnConfig.
        :type request: :class:`ksyun.client.dts.v20180108.models.DescribeConnConfigRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeConnConfig", params, "application/x-www-form-urlencoded")
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


    def DescribePrecheck(self, request):
        """查询预检查结果(含未通过异常反馈)
        :param request: Request instance for DescribePrecheck.
        :type request: :class:`ksyun.client.dts.v20180108.models.DescribePrecheckRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribePrecheck", params, "application/x-www-form-urlencoded")
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


    def DescribeSourceUserConfig(self, request):
        """获取迁移账号配置信息
        :param request: Request instance for DescribeSourceUserConfig.
        :type request: :class:`ksyun.client.dts.v20180108.models.DescribeSourceUserConfigRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeSourceUserConfig", params, "application/json")
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


    def SetConsistencyCheck(self, request):
        """打开或关闭DTS一致性校验定时任务
        :param request: Request instance for SetConsistencyCheck.
        :type request: :class:`ksyun.client.dts.v20180108.models.SetConsistencyCheckRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("SetConsistencyCheck", params, "application/json")
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


    def DescribeConsistencyCheck(self, request):
        """查询定时一致性校验任务状态
        :param request: Request instance for DescribeConsistencyCheck.
        :type request: :class:`ksyun.client.dts.v20180108.models.DescribeConsistencyCheckRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeConsistencyCheck", params, "application/json")
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


    def DescribeDTSParameter(self, request):
        """获取迁移实例参数信息(参数对齐功能使用)
        :param request: Request instance for DescribeDTSParameter.
        :type request: :class:`ksyun.client.dts.v20180108.models.DescribeDTSParameterRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDTSParameter", params, "application/json")
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


    def DescribeDTSParameterConfig(self, request):
        """查询DTS任务的实例参数配置
        :param request: Request instance for DescribeDTSParameterConfig.
        :type request: :class:`ksyun.client.dts.v20180108.models.DescribeDTSParameterConfigRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDTSParameterConfig", params, "application/json")
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


    def DescribeSourceUser(self, request):
        """获取源端实例用户账号信息
        :param request: Request instance for DescribeSourceUser.
        :type request: :class:`ksyun.client.dts.v20180108.models.DescribeSourceUserRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeSourceUser", params, "application/json")
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


    def DescribeSubTask(self, request):
        """查询一致性校验任务(子任务/一致性校验任务)
        :param request: Request instance for DescribeSubTask.
        :type request: :class:`ksyun.client.dts.v20180108.models.DescribeSubTaskRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeSubTask", params, "application/json")
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


    def CreateConsistencyCheck(self, request):
        """创建一致性校验任务(子任务)
        :param request: Request instance for CreateConsistencyCheck.
        :type request: :class:`ksyun.client.dts.v20180108.models.CreateConsistencyCheckRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateConsistencyCheck", params, "application/json")
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


    def StopConsistencyCheck(self, request):
        """结束一致性校验任务(手动)
        :param request: Request instance for StopConsistencyCheck.
        :type request: :class:`ksyun.client.dts.v20180108.models.StopConsistencyCheckRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("StopConsistencyCheck", params, "application/json")
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


    def DescribeRegionConfig(self, request):
        """查询支持的地域信息
        :param request: Request instance for DescribeRegionConfig.
        :type request: :class:`ksyun.client.dts.v20180108.models.DescribeRegionConfigRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeRegionConfig", params, "application/x-www-form-urlencoded")
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


    def TaskBirdView(self, request):
        """分类型概览任务统计数据
        :param request: Request instance for TaskBirdView.
        :type request: :class:`ksyun.client.dts.v20180108.models.TaskBirdViewRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("TaskBirdView", params, "application/json")
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


