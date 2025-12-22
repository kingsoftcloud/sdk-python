import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class TidbClient(AbstractClient):
    _apiVersion = '2021-05-20'
    _endpoint = 'tidb.api.ksyun.com'
    _service = 'tidb'
    def CreateInstance(self, request):
        """创建实例(支持基于备份及指定时间点)
        :param request: Request instance for CreateInstance.
        :type request: :class:`ksyun.client.tidb.v20210520.models.CreateInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateInstance", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def ListInstance(self, request):
        """查询实例列表(区分Region)
        :param request: Request instance for ListInstance.
        :type request: :class:`ksyun.client.tidb.v20210520.models.ListInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListInstance", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeInstance(self, request):
        """查询实例详情
        :param request: Request instance for DescribeInstance.
        :type request: :class:`ksyun.client.tidb.v20210520.models.DescribeInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeInstance", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DeleteInstance(self, request):
        """删除实例(支持批量)
        :param request: Request instance for DeleteInstance.
        :type request: :class:`ksyun.client.tidb.v20210520.models.DeleteInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteInstance", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def RenameInstance(self, request):
        """修改名称(重命名)
        :param request: Request instance for RenameInstance.
        :type request: :class:`ksyun.client.tidb.v20210520.models.RenameInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RenameInstance", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def ListRegion(self, request):
        """查询地域列表
        :param request: Request instance for ListRegion.
        :type request: :class:`ksyun.client.tidb.v20210520.models.ListRegionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListRegion", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescRegion(self, request):
        """查询指定地域详情
        :param request: Request instance for DescRegion.
        :type request: :class:`ksyun.client.tidb.v20210520.models.DescRegionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescRegion", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def CreateSecurityGroup(self, request):
        """创建安全组
        :param request: Request instance for CreateSecurityGroup.
        :type request: :class:`ksyun.client.tidb.v20210520.models.CreateSecurityGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateSecurityGroup", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def ListSecurityGroup(self, request):
        """查询安全组列表
        :param request: Request instance for ListSecurityGroup.
        :type request: :class:`ksyun.client.tidb.v20210520.models.ListSecurityGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListSecurityGroup", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeSecurityGroup(self, request):
        """查询安全组详情
        :param request: Request instance for DescribeSecurityGroup.
        :type request: :class:`ksyun.client.tidb.v20210520.models.DescribeSecurityGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeSecurityGroup", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DeleteSecurityGroup(self, request):
        """删除安全组(支持批量)
        :param request: Request instance for DeleteSecurityGroup.
        :type request: :class:`ksyun.client.tidb.v20210520.models.DeleteSecurityGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteSecurityGroup", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def UpdateSecurityGroup(self, request):
        """更新安全组
        :param request: Request instance for UpdateSecurityGroup.
        :type request: :class:`ksyun.client.tidb.v20210520.models.UpdateSecurityGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateSecurityGroup", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def CloneSecurityGroup(self, request):
        """复制安全组(仅规则)
        :param request: Request instance for CloneSecurityGroup.
        :type request: :class:`ksyun.client.tidb.v20210520.models.CloneSecurityGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CloneSecurityGroup", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def BindSecurityGroup(self, request):
        """实例绑定安全组
        :param request: Request instance for BindSecurityGroup.
        :type request: :class:`ksyun.client.tidb.v20210520.models.BindSecurityGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("BindSecurityGroup", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def UnbindSecurityGroup(self, request):
        """实例解绑安全组
        :param request: Request instance for UnbindSecurityGroup.
        :type request: :class:`ksyun.client.tidb.v20210520.models.UnbindSecurityGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UnbindSecurityGroup", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def RebindSecurityGroup(self, request):
        """重新绑定实例安全组
        :param request: Request instance for RebindSecurityGroup.
        :type request: :class:`ksyun.client.tidb.v20210520.models.RebindSecurityGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RebindSecurityGroup", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def CreateSecurityRule(self, request):
        """创建安全规则(CIDR)
        :param request: Request instance for CreateSecurityRule.
        :type request: :class:`ksyun.client.tidb.v20210520.models.CreateSecurityRuleRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateSecurityRule", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def UpdateSecurityRule(self, request):
        """更新安全规则(CIDR)
        :param request: Request instance for UpdateSecurityRule.
        :type request: :class:`ksyun.client.tidb.v20210520.models.UpdateSecurityRuleRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateSecurityRule", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DeleteSecurityRule(self, request):
        """删除安全规则(CIDR)
        :param request: Request instance for DeleteSecurityRule.
        :type request: :class:`ksyun.client.tidb.v20210520.models.DeleteSecurityRuleRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteSecurityRule", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def ListSecuredInstance(self, request):
        """查询已绑定安全组实例列表
        :param request: Request instance for ListSecuredInstance.
        :type request: :class:`ksyun.client.tidb.v20210520.models.ListSecuredInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListSecuredInstance", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def ListUnsecuredInstance(self, request):
        """查询未绑定安全组实例列表
        :param request: Request instance for ListUnsecuredInstance.
        :type request: :class:`ksyun.client.tidb.v20210520.models.ListUnsecuredInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListUnsecuredInstance", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def ListBackup(self, request):
        """查询备份列表
        :param request: Request instance for ListBackup.
        :type request: :class:`ksyun.client.tidb.v20210520.models.ListBackupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListBackup", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def CreateBackup(self, request):
        """创建备份(手动)
        :param request: Request instance for CreateBackup.
        :type request: :class:`ksyun.client.tidb.v20210520.models.CreateBackupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateBackup", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def UpdateBackupRule(self, request):
        """更新自动备份规则
        :param request: Request instance for UpdateBackupRule.
        :type request: :class:`ksyun.client.tidb.v20210520.models.UpdateBackupRuleRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateBackupRule", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DeleteBackup(self, request):
        """批量删除备份记录
        :param request: Request instance for DeleteBackup.
        :type request: :class:`ksyun.client.tidb.v20210520.models.DeleteBackupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteBackup", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def CreateRestore(self, request):
        """创建恢复任务
        :param request: Request instance for CreateRestore.
        :type request: :class:`ksyun.client.tidb.v20210520.models.CreateRestoreRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateRestore", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def OpenTiMonitor(self, request):
        """打开timonitor监控
        :param request: Request instance for OpenTiMonitor.
        :type request: :class:`ksyun.client.tidb.v20210520.models.OpenTiMonitorRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("OpenTiMonitor", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """创建任务(TICDC)
        :param request: Request instance for CreateTask.
        :type request: :class:`ksyun.client.tidb.v20210520.models.CreateTaskRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateTask", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def OperationTasks(self, request):
        """任务操作(TICDC)
        :param request: Request instance for OperationTasks.
        :type request: :class:`ksyun.client.tidb.v20210520.models.OperationTasksRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("OperationTasks", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def CheckTaskName(self, request):
        """名称列表(TICDC)
        :param request: Request instance for CheckTaskName.
        :type request: :class:`ksyun.client.tidb.v20210520.models.CheckTaskNameRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CheckTaskName", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """任务详情(TICDC)
        :param request: Request instance for DescribeTask.
        :type request: :class:`ksyun.client.tidb.v20210520.models.DescribeTaskRequest`
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


    def ListTasks(self, request):
        """任务列表(TICDC)
        :param request: Request instance for ListTasks.
        :type request: :class:`ksyun.client.tidb.v20210520.models.ListTasksRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListTasks", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeDatabases(self, request):
        """查询库表列表
        :param request: Request instance for DescribeDatabases.
        :type request: :class:`ksyun.client.tidb.v20210520.models.DescribeDatabasesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDatabases", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeAccounts(self, request):
        """查询账号列表
        :param request: Request instance for DescribeAccounts.
        :type request: :class:`ksyun.client.tidb.v20210520.models.DescribeAccountsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeAccounts", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def CreateAccount(self, request):
        """创建账号(指定实例)
        :param request: Request instance for CreateAccount.
        :type request: :class:`ksyun.client.tidb.v20210520.models.CreateAccountRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateAccount", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DeleteAccount(self, request):
        """删除账号(支持批量)
        :param request: Request instance for DeleteAccount.
        :type request: :class:`ksyun.client.tidb.v20210520.models.DeleteAccountRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteAccount", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def ModifyAccountInfo(self, request):
        """编辑账号信息(修改密码)
        :param request: Request instance for ModifyAccountInfo.
        :type request: :class:`ksyun.client.tidb.v20210520.models.ModifyAccountInfoRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyAccountInfo", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def ModifyAccountPrivileges(self, request):
        """编辑账号权限
        :param request: Request instance for ModifyAccountPrivileges.
        :type request: :class:`ksyun.client.tidb.v20210520.models.ModifyAccountPrivilegesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyAccountPrivileges", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def ConfigurationInstanceEip(self, request):
        """申请/释放外网EIP
        :param request: Request instance for ConfigurationInstanceEip.
        :type request: :class:`ksyun.client.tidb.v20210520.models.ConfigurationInstanceEipRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ConfigurationInstanceEip", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def UpdateInstanceTrialOrder(self, request):
        """试用订单转正/延期
        :param request: Request instance for UpdateInstanceTrialOrder.
        :type request: :class:`ksyun.client.tidb.v20210520.models.UpdateInstanceTrialOrderRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateInstanceTrialOrder", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


