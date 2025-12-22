import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class PostgresqlClient(AbstractClient):
    _apiVersion = '2018-12-25'
    _endpoint = 'postgresql.api.ksyun.com'
    _service = 'postgresql'
    def CreateDBInstance(self, request):
        """创建实例(可指定具体产品类型)
        :param request: Request instance for CreateDBInstance.
        :type request: :class:`ksyun.client.postgresql.v20181225.models.CreateDBInstanceRequest`
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
        :type request: :class:`ksyun.client.postgresql.v20181225.models.DescribeDBInstancesRequest`
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
        """删除指定实例(不支持批量)
        :param request: Request instance for DeleteDBInstance.
        :type request: :class:`ksyun.client.postgresql.v20181225.models.DeleteDBInstanceRequest`
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


    def StatisticDBInstances(self, request):
        """实例概览统计(全可用地域下单区分类统计)
        :param request: Request instance for StatisticDBInstances.
        :type request: :class:`ksyun.client.postgresql.v20181225.models.StatisticDBInstancesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("StatisticDBInstances", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """修改实例信息(实例名/账户密码/自动备份时间/参数组/安全组)
        :param request: Request instance for ModifyDBInstance.
        :type request: :class:`ksyun.client.postgresql.v20181225.models.ModifyDBInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyDBInstance", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """创建安全组(模版)
        :param request: Request instance for CreateSecurityGroup.
        :type request: :class:`ksyun.client.postgresql.v20181225.models.CreateSecurityGroupRequest`
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
        """查询安全组详情
        :param request: Request instance for DescribeSecurityGroup.
        :type request: :class:`ksyun.client.postgresql.v20181225.models.DescribeSecurityGroupRequest`
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
        """删除安全组(支持批量)
        :param request: Request instance for DeleteSecurityGroup.
        :type request: :class:`ksyun.client.postgresql.v20181225.models.DeleteSecurityGroupRequest`
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
        :type request: :class:`ksyun.client.postgresql.v20181225.models.ModifySecurityGroupRequest`
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
        :type request: :class:`ksyun.client.postgresql.v20181225.models.CloneSecurityGroupRequest`
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
        """修改CIDR规则
        :param request: Request instance for ModifySecurityGroupRule.
        :type request: :class:`ksyun.client.postgresql.v20181225.models.ModifySecurityGroupRuleRequest`
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
        """实例绑定/解绑安全组
        :param request: Request instance for SecurityGroupRelation.
        :type request: :class:`ksyun.client.postgresql.v20181225.models.SecurityGroupRelationRequest`
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
        :type request: :class:`ksyun.client.postgresql.v20181225.models.ModifySecurityGroupRuleNameRequest`
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


    def DescribeDBLogFiles(self, request):
        """查询日志文件列表
        :param request: Request instance for DescribeDBLogFiles.
        :type request: :class:`ksyun.client.postgresql.v20181225.models.DescribeDBLogFilesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDBLogFiles", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """创建指定实例手动备份
        :param request: Request instance for CreateDBBackup.
        :type request: :class:`ksyun.client.postgresql.v20181225.models.CreateDBBackupRequest`
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
        """删除实例备份(手动备份)
        :param request: Request instance for DeleteDBBackup.
        :type request: :class:`ksyun.client.postgresql.v20181225.models.DeleteDBBackupRequest`
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
        """查询备份列表
        :param request: Request instance for DescribeDBBackups.
        :type request: :class:`ksyun.client.postgresql.v20181225.models.DescribeDBBackupsRequest`
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
        :type request: :class:`ksyun.client.postgresql.v20181225.models.ModifyDBBackupPolicyRequest`
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


    def OverrideDBInstance(self, request):
        """恢复至源实例
        :param request: Request instance for OverrideDBInstance.
        :type request: :class:`ksyun.client.postgresql.v20181225.models.OverrideDBInstanceRequest`
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


    def CreateDBParameterGroup(self, request):
        """创建参数组(模版)
        :param request: Request instance for CreateDBParameterGroup.
        :type request: :class:`ksyun.client.postgresql.v20181225.models.CreateDBParameterGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateDBParameterGroup", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ModifyDBParameterGroup(self, request):
        """修改参数组
        :param request: Request instance for ModifyDBParameterGroup.
        :type request: :class:`ksyun.client.postgresql.v20181225.models.ModifyDBParameterGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyDBParameterGroup", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DeleteDBParameterGroup(self, request):
        """删除参数组(模版)
        :param request: Request instance for DeleteDBParameterGroup.
        :type request: :class:`ksyun.client.postgresql.v20181225.models.DeleteDBParameterGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteDBParameterGroup", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ResetDBParameterGroup(self, request):
        """重置实例参数
        :param request: Request instance for ResetDBParameterGroup.
        :type request: :class:`ksyun.client.postgresql.v20181225.models.ResetDBParameterGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ResetDBParameterGroup", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeDBParameterGroup(self, request):
        """查询参数组列表/详情
        :param request: Request instance for DescribeDBParameterGroup.
        :type request: :class:`ksyun.client.postgresql.v20181225.models.DescribeDBParameterGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDBParameterGroup", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeEngineDefaultParameters(self, request):
        """查询默认参数组详情
        :param request: Request instance for DescribeEngineDefaultParameters.
        :type request: :class:`ksyun.client.postgresql.v20181225.models.DescribeEngineDefaultParametersRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeEngineDefaultParameters", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeDBInstanceParameters(self, request):
        """查询实例参数(运行中参数)
        :param request: Request instance for DescribeDBInstanceParameters.
        :type request: :class:`ksyun.client.postgresql.v20181225.models.DescribeDBInstanceParametersRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDBInstanceParameters", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """重启指定实例
        :param request: Request instance for RebootDBInstance.
        :type request: :class:`ksyun.client.postgresql.v20181225.models.RebootDBInstanceRequest`
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


    def DescribeDBEngineVersions(self, request):
        """查询支持的引擎版本及最新小版本信息
        :param request: Request instance for DescribeDBEngineVersions.
        :type request: :class:`ksyun.client.postgresql.v20181225.models.DescribeDBEngineVersionsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDBEngineVersions", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        :type request: :class:`ksyun.client.postgresql.v20181225.models.AllocateDBInstanceEipRequest`
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
        :type request: :class:`ksyun.client.postgresql.v20181225.models.ReleaseDBInstanceEipRequest`
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


    def ModifyDBInstanceSpec(self, request):
        """更改实例配置
        :param request: Request instance for ModifyDBInstanceSpec.
        :type request: :class:`ksyun.client.postgresql.v20181225.models.ModifyDBInstanceSpecRequest`
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


    def RestoreDBInstanceFromDBBackup(self, request):
        """恢复至新实例
        :param request: Request instance for RestoreDBInstanceFromDBBackup.
        :type request: :class:`ksyun.client.postgresql.v20181225.models.RestoreDBInstanceFromDBBackupRequest`
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


    def SwitchDBInstanceHA(self, request):
        """主备切换(可用区)
        :param request: Request instance for SwitchDBInstanceHA.
        :type request: :class:`ksyun.client.postgresql.v20181225.models.SwitchDBInstanceHARequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("SwitchDBInstanceHA", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def CreateDBInstanceReadReplica(self, request):
        """创建只读实例
        :param request: Request instance for CreateDBInstanceReadReplica.
        :type request: :class:`ksyun.client.postgresql.v20181225.models.CreateDBInstanceReadReplicaRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateDBInstanceReadReplica", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """编辑账号信息
        :param request: Request instance for ModifyInstanceAccountInfo.
        :type request: :class:`ksyun.client.postgresql.v20181225.models.ModifyInstanceAccountInfoRequest`
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


    def DescribeInstanceDatabases(self, request):
        """查询数据库列表
        :param request: Request instance for DescribeInstanceDatabases.
        :type request: :class:`ksyun.client.postgresql.v20181225.models.DescribeInstanceDatabasesRequest`
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


    def DescribeDBInstanceExtensions(self, request):
        """查询插件列表
        :param request: Request instance for DescribeDBInstanceExtensions.
        :type request: :class:`ksyun.client.postgresql.v20181225.models.DescribeDBInstanceExtensionsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDBInstanceExtensions", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ModifyDBInstanceExtension(self, request):
        """安装/卸载用户实例插件
        :param request: Request instance for ModifyDBInstanceExtension.
        :type request: :class:`ksyun.client.postgresql.v20181225.models.ModifyDBInstanceExtensionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyDBInstanceExtension", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        :type request: :class:`ksyun.client.postgresql.v20181225.models.DescribeCollationsRequest`
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


    def ModifyInstanceDatabaseOwner(self, request):
        """修改数据库所有者
        :param request: Request instance for ModifyInstanceDatabaseOwner.
        :type request: :class:`ksyun.client.postgresql.v20181225.models.ModifyInstanceDatabaseOwnerRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyInstanceDatabaseOwner", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        :type request: :class:`ksyun.client.postgresql.v20181225.models.DeleteInstanceDatabaseRequest`
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


    def CreateInstanceDatabase(self, request):
        """创建数据库
        :param request: Request instance for CreateInstanceDatabase.
        :type request: :class:`ksyun.client.postgresql.v20181225.models.CreateInstanceDatabaseRequest`
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


    def DescribeInstanceAccounts(self, request):
        """查询账号列表
        :param request: Request instance for DescribeInstanceAccounts.
        :type request: :class:`ksyun.client.postgresql.v20181225.models.DescribeInstanceAccountsRequest`
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


    def CreateInstanceAccount(self, request):
        """创建账号(数据库账号)
        :param request: Request instance for CreateInstanceAccount.
        :type request: :class:`ksyun.client.postgresql.v20181225.models.CreateInstanceAccountRequest`
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


    def DeleteInstanceAccount(self, request):
        """删除账号(不支持批量)
        :param request: Request instance for DeleteInstanceAccount.
        :type request: :class:`ksyun.client.postgresql.v20181225.models.DeleteInstanceAccountRequest`
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


    def ModifyDBNetwork(self, request):
        """变更网络(修改VPC信息)
        :param request: Request instance for ModifyDBNetwork.
        :type request: :class:`ksyun.client.postgresql.v20181225.models.ModifyDBNetworkRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyDBNetwork", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def UpdateDBInstanceVersion(self, request):
        """升级至当前实例最新小版本
        :param request: Request instance for UpdateDBInstanceVersion.
        :type request: :class:`ksyun.client.postgresql.v20181225.models.UpdateDBInstanceVersionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateDBInstanceVersion", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ModifyDBInstanceAvailabilityZone(self, request):
        """迁移可用区(迁移备库可用区)
        :param request: Request instance for ModifyDBInstanceAvailabilityZone.
        :type request: :class:`ksyun.client.postgresql.v20181225.models.ModifyDBInstanceAvailabilityZoneRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyDBInstanceAvailabilityZone", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        :type request: :class:`ksyun.client.postgresql.v20181225.models.UpdateDBInstanceOrderRequest`
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
        :type request: :class:`ksyun.client.postgresql.v20181225.models.UpdateResourceProtectionRequest`
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


