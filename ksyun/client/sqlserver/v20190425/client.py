import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class SqlserverClient(AbstractClient):
    _apiVersion = '2019-04-25'
    _endpoint = 'sqlserver.api.ksyun.com'
    _service = 'sqlserver'
    def CreateDBInstance(self, request):
        """创建实例(指定实例类型)
        :param request: Request instance for CreateDBInstance.
        :type request: :class:`ksyun.client.sqlserver.v20190425.models.CreateDBInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateDBInstance", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeDBInstances(self, request):
        """查询实例列表/详情
        :param request: Request instance for DescribeDBInstances.
        :type request: :class:`ksyun.client.sqlserver.v20190425.models.DescribeDBInstancesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDBInstances", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DeleteDBInstance(self, request):
        """删除实例(不支持批量)
        :param request: Request instance for DeleteDBInstance.
        :type request: :class:`ksyun.client.sqlserver.v20190425.models.DeleteDBInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteDBInstance", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def ModifyDBInstance(self, request):
        """修改实例名称
        :param request: Request instance for ModifyDBInstance.
        :type request: :class:`ksyun.client.sqlserver.v20190425.models.ModifyDBInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyDBInstance", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        :type request: :class:`ksyun.client.sqlserver.v20190425.models.CreateSecurityGroupRequest`
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


    def DescribeSecurityGroup(self, request):
        """查询安全组列表/详情
        :param request: Request instance for DescribeSecurityGroup.
        :type request: :class:`ksyun.client.sqlserver.v20190425.models.DescribeSecurityGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeSecurityGroup", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """删除安全组
        :param request: Request instance for DeleteSecurityGroup.
        :type request: :class:`ksyun.client.sqlserver.v20190425.models.DeleteSecurityGroupRequest`
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


    def ModifySecurityGroup(self, request):
        """修改安全组名称/描述
        :param request: Request instance for ModifySecurityGroup.
        :type request: :class:`ksyun.client.sqlserver.v20190425.models.ModifySecurityGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifySecurityGroup", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """克隆安全组
        :param request: Request instance for CloneSecurityGroup.
        :type request: :class:`ksyun.client.sqlserver.v20190425.models.CloneSecurityGroupRequest`
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


    def ModifySecurityGroupRule(self, request):
        """修改安全组CIDR规则
        :param request: Request instance for ModifySecurityGroupRule.
        :type request: :class:`ksyun.client.sqlserver.v20190425.models.ModifySecurityGroupRuleRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifySecurityGroupRule", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def SecurityGroupRelation(self, request):
        """实例绑定/移除安全组
        :param request: Request instance for SecurityGroupRelation.
        :type request: :class:`ksyun.client.sqlserver.v20190425.models.SecurityGroupRelationRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("SecurityGroupRelation", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def ModifySecurityGroupRuleName(self, request):
        """修改安全组规则备注
        :param request: Request instance for ModifySecurityGroupRuleName.
        :type request: :class:`ksyun.client.sqlserver.v20190425.models.ModifySecurityGroupRuleNameRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifySecurityGroupRuleName", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeCollations(self, request):
        """查询支持字符集
        :param request: Request instance for DescribeCollations.
        :type request: :class:`ksyun.client.sqlserver.v20190425.models.DescribeCollationsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeCollations", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def CreateInstanceDatabase(self, request):
        """创建数据库
        :param request: Request instance for CreateInstanceDatabase.
        :type request: :class:`ksyun.client.sqlserver.v20190425.models.CreateInstanceDatabaseRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateInstanceDatabase", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def ModifyInstanceDatabasePrivileges(self, request):
        """编辑数据库权限
        :param request: Request instance for ModifyInstanceDatabasePrivileges.
        :type request: :class:`ksyun.client.sqlserver.v20190425.models.ModifyInstanceDatabasePrivilegesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyInstanceDatabasePrivileges", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeInstanceDatabases(self, request):
        """查询数据库列表/详情
        :param request: Request instance for DescribeInstanceDatabases.
        :type request: :class:`ksyun.client.sqlserver.v20190425.models.DescribeInstanceDatabasesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeInstanceDatabases", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def CreateInstanceAccount(self, request):
        """创建账号(可同时指定对应库权限)
        :param request: Request instance for CreateInstanceAccount.
        :type request: :class:`ksyun.client.sqlserver.v20190425.models.CreateInstanceAccountRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateInstanceAccount", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeInstanceAccounts(self, request):
        """查询账号列表/详情
        :param request: Request instance for DescribeInstanceAccounts.
        :type request: :class:`ksyun.client.sqlserver.v20190425.models.DescribeInstanceAccountsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeInstanceAccounts", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def ModifyInstanceAccountInfo(self, request):
        """修改账号密码/描述
        :param request: Request instance for ModifyInstanceAccountInfo.
        :type request: :class:`ksyun.client.sqlserver.v20190425.models.ModifyInstanceAccountInfoRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyInstanceAccountInfo", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def ModifyInstanceAccountPrivileges(self, request):
        """编辑账号权限
        :param request: Request instance for ModifyInstanceAccountPrivileges.
        :type request: :class:`ksyun.client.sqlserver.v20190425.models.ModifyInstanceAccountPrivilegesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyInstanceAccountPrivileges", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DeleteInstanceAccount(self, request):
        """删除账号(不支持批量)
        :param request: Request instance for DeleteInstanceAccount.
        :type request: :class:`ksyun.client.sqlserver.v20190425.models.DeleteInstanceAccountRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteInstanceAccount", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DeleteInstanceDatabase(self, request):
        """删除数据库
        :param request: Request instance for DeleteInstanceDatabase.
        :type request: :class:`ksyun.client.sqlserver.v20190425.models.DeleteInstanceDatabaseRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteInstanceDatabase", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def ModifyInstanceDatabaseInfo(self, request):
        """修改数据库描述
        :param request: Request instance for ModifyInstanceDatabaseInfo.
        :type request: :class:`ksyun.client.sqlserver.v20190425.models.ModifyInstanceDatabaseInfoRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyInstanceDatabaseInfo", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def OverrideDBInstance(self, request):
        """恢复到当前实例(指定备份覆盖)
        :param request: Request instance for OverrideDBInstance.
        :type request: :class:`ksyun.client.sqlserver.v20190425.models.OverrideDBInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("OverrideDBInstance", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def RestoreDBInstanceFromDBBackup(self, request):
        """恢复至新实例(基于备份)
        :param request: Request instance for RestoreDBInstanceFromDBBackup.
        :type request: :class:`ksyun.client.sqlserver.v20190425.models.RestoreDBInstanceFromDBBackupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RestoreDBInstanceFromDBBackup", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def CreateDBBackup(self, request):
        """创建备份(手动备份)
        :param request: Request instance for CreateDBBackup.
        :type request: :class:`ksyun.client.sqlserver.v20190425.models.CreateDBBackupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateDBBackup", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DeleteDBBackup(self, request):
        """删除备份(不支持批量)
        :param request: Request instance for DeleteDBBackup.
        :type request: :class:`ksyun.client.sqlserver.v20190425.models.DeleteDBBackupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteDBBackup", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeDBBackups(self, request):
        """查询备份列表/详情
        :param request: Request instance for DescribeDBBackups.
        :type request: :class:`ksyun.client.sqlserver.v20190425.models.DescribeDBBackupsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDBBackups", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def ModifyDBBackupPolicy(self, request):
        """修改备份策略
        :param request: Request instance for ModifyDBBackupPolicy.
        :type request: :class:`ksyun.client.sqlserver.v20190425.models.ModifyDBBackupPolicyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyDBBackupPolicy", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def AllocateDBInstanceEip(self, request):
        """申请外网EIP
        :param request: Request instance for AllocateDBInstanceEip.
        :type request: :class:`ksyun.client.sqlserver.v20190425.models.AllocateDBInstanceEipRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AllocateDBInstanceEip", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def ReleaseDBInstanceEip(self, request):
        """释放外网EIP
        :param request: Request instance for ReleaseDBInstanceEip.
        :type request: :class:`ksyun.client.sqlserver.v20190425.models.ReleaseDBInstanceEipRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ReleaseDBInstanceEip", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def ListSlowLogs(self, request):
        """查询慢日志列表信息
        :param request: Request instance for ListSlowLogs.
        :type request: :class:`ksyun.client.sqlserver.v20190425.models.ListSlowLogsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListSlowLogs", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def ListErrorLogs(self, request):
        """查询错误日志列表信息
        :param request: Request instance for ListErrorLogs.
        :type request: :class:`ksyun.client.sqlserver.v20190425.models.ListErrorLogsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListErrorLogs", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def ModifyDBInstanceSpec(self, request):
        """更配实例配置
        :param request: Request instance for ModifyDBInstanceSpec.
        :type request: :class:`ksyun.client.sqlserver.v20190425.models.ModifyDBInstanceSpecRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyDBInstanceSpec", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeImportTask(self, request):
        """查询任务列表
        :param request: Request instance for DescribeImportTask.
        :type request: :class:`ksyun.client.sqlserver.v20190425.models.DescribeImportTaskRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeImportTask", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeImportFile(self, request):
        """查询任务详情
        :param request: Request instance for DescribeImportFile.
        :type request: :class:`ksyun.client.sqlserver.v20190425.models.DescribeImportFileRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeImportFile", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def CreateImportTask(self, request):
        """创建任务(指定KS3桶备份)
        :param request: Request instance for CreateImportTask.
        :type request: :class:`ksyun.client.sqlserver.v20190425.models.CreateImportTaskRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateImportTask", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def FinishImportTask(self, request):
        """结束导入任务
        :param request: Request instance for FinishImportTask.
        :type request: :class:`ksyun.client.sqlserver.v20190425.models.FinishImportTaskRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("FinishImportTask", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeDBInstanceRestorableTime(self, request):
        """查看实例恢复时间(库表恢复用)
        :param request: Request instance for DescribeDBInstanceRestorableTime.
        :type request: :class:`ksyun.client.sqlserver.v20190425.models.DescribeDBInstanceRestorableTimeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDBInstanceRestorableTime", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def GetHistoryDatabaseInfo(self, request):
        """查询指定时间点/备份集附近的库表信息(库表恢复用)
        :param request: Request instance for GetHistoryDatabaseInfo.
        :type request: :class:`ksyun.client.sqlserver.v20190425.models.GetHistoryDatabaseInfoRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetHistoryDatabaseInfo", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def RestoreToCurInstance(self, request):
        """恢复至源实例(指定具体库表)
        :param request: Request instance for RestoreToCurInstance.
        :type request: :class:`ksyun.client.sqlserver.v20190425.models.RestoreToCurInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RestoreToCurInstance", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def ModifyInstanceDatabaseName(self, request):
        """修改数据库名称
        :param request: Request instance for ModifyInstanceDatabaseName.
        :type request: :class:`ksyun.client.sqlserver.v20190425.models.ModifyInstanceDatabaseNameRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyInstanceDatabaseName", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def RebootDBInstance(self, request):
        """重启实例(指定实例)
        :param request: Request instance for RebootDBInstance.
        :type request: :class:`ksyun.client.sqlserver.v20190425.models.RebootDBInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RebootDBInstance", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeDBBackupPolicy(self, request):
        """查询备份配置信息
        :param request: Request instance for DescribeDBBackupPolicy.
        :type request: :class:`ksyun.client.sqlserver.v20190425.models.DescribeDBBackupPolicyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDBBackupPolicy", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def UpdateDBInstanceOrder(self, request):
        """试用订单延期/转正
        :param request: Request instance for UpdateDBInstanceOrder.
        :type request: :class:`ksyun.client.sqlserver.v20190425.models.UpdateDBInstanceOrderRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateDBInstanceOrder", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def UpdateResourceProtection(self, request):
        """删除保护设置
        :param request: Request instance for UpdateResourceProtection.
        :type request: :class:`ksyun.client.sqlserver.v20190425.models.UpdateResourceProtectionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateResourceProtection", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


