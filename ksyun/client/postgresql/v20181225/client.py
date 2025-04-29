import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class PostgresqlClient(AbstractClient):
    _apiVersion = '2018-12-25'
    _endpoint = 'postgresql.api.ksyun.com'
    _service = 'postgresql'

    def CreateDBInstance(self, request):
        """create db instance
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
        """describe db instances
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
        """delete db instance
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
        """statistic db instances
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
        """modify db instance
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
        """create security group
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
        """describe security group
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
        """delete security group
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
        """modify security group
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
        """clone security group
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
        """modify security grooup rule
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
        """security group relation
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
        """modify security group rule name
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
        """describe db log files
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
        """create db backup
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
        """delete db backup
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
        """describe db backups
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
        """modify db backup policy
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
        """override db instance
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
        """create db parameter group
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
        """modify db parameter group
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
        """delete db parameter group
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
        """reset db parameter grooup
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
        """describe db parameter group
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
        """describe engine default parameters
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
        """查看实例参数组
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
        """reboot db instance
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
        """describe db engine version
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
        """allocate db instance eip
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
        """release db instance eip
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
        """modify db instance spec
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
        """restore db instance from db backup
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
        """switch db instance ha
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
        """create db instance read replica
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
        """modify instance account info
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
        """获取实例数据库列表
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
        """describe db instance extensions
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
        """modify db instance extension
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
