import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class InfluxdbClient(AbstractClient):
    _apiVersion = '2019-10-10'
    _endpoint = 'Influxdb.api.ksyun.com'
    _service = 'Influxdb'
    def CreateInstance(self, request):
        """创建实例
        :param request: Request instance for CreateInstance.
        :type request: :class:`ksyun.client.influxdb.v20191010.models.CreateInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateInstance", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """删除实例
        :param request: Request instance for DeleteInstance.
        :type request: :class:`ksyun.client.influxdb.v20191010.models.DeleteInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteInstance", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """查看实例详情
        :param request: Request instance for DescribeInstance.
        :type request: :class:`ksyun.client.influxdb.v20191010.models.DescribeInstanceRequest`
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


    def DescribeInstances(self, request):
        """查看实例列表
        :param request: Request instance for DescribeInstances.
        :type request: :class:`ksyun.client.influxdb.v20191010.models.DescribeInstancesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeInstances", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeInstanceNode(self, request):
        """查看实例节点
        :param request: Request instance for DescribeInstanceNode.
        :type request: :class:`ksyun.client.influxdb.v20191010.models.DescribeInstanceNodeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeInstanceNode", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """重命名实例
        :param request: Request instance for RenameInstance.
        :type request: :class:`ksyun.client.influxdb.v20191010.models.RenameInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RenameInstance", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeValidRegions(self, request):
        """查看有效机房及可用区
        :param request: Request instance for DescribeValidRegions.
        :type request: :class:`ksyun.client.influxdb.v20191010.models.DescribeValidRegionsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeValidRegions", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """查看安全组
        :param request: Request instance for DescribeSecurityGroup.
        :type request: :class:`ksyun.client.influxdb.v20191010.models.DescribeSecurityGroupRequest`
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


    def CreateSecurityRule(self, request):
        """创建安全规则
        :param request: Request instance for CreateSecurityRule.
        :type request: :class:`ksyun.client.influxdb.v20191010.models.CreateSecurityRuleRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateSecurityRule", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """删除安全规则
        :param request: Request instance for DeleteSecurityRule.
        :type request: :class:`ksyun.client.influxdb.v20191010.models.DeleteSecurityRuleRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteSecurityRule", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """查看数据库列表
        :param request: Request instance for DescribeDatabases.
        :type request: :class:`ksyun.client.influxdb.v20191010.models.DescribeDatabasesRequest`
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


    def CreateDatabase(self, request):
        """创建数据库
        :param request: Request instance for CreateDatabase.
        :type request: :class:`ksyun.client.influxdb.v20191010.models.CreateDatabaseRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateDatabase", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DeleteDatabase(self, request):
        """删除数据库
        :param request: Request instance for DeleteDatabase.
        :type request: :class:`ksyun.client.influxdb.v20191010.models.DeleteDatabaseRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteDatabase", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeRetentionPolicyList(self, request):
        """查看数据保留策略列表
        :param request: Request instance for DescribeRetentionPolicyList.
        :type request: :class:`ksyun.client.influxdb.v20191010.models.DescribeRetentionPolicyListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeRetentionPolicyList", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def CreateRetentionPolicy(self, request):
        """创建数据保留策略
        :param request: Request instance for CreateRetentionPolicy.
        :type request: :class:`ksyun.client.influxdb.v20191010.models.CreateRetentionPolicyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateRetentionPolicy", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DeleteRetentionPolicy(self, request):
        """删除数据保留策略
        :param request: Request instance for DeleteRetentionPolicy.
        :type request: :class:`ksyun.client.influxdb.v20191010.models.DeleteRetentionPolicyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteRetentionPolicy", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ModifyRetentionPolicy(self, request):
        """修改数据保留策略
        :param request: Request instance for ModifyRetentionPolicy.
        :type request: :class:`ksyun.client.influxdb.v20191010.models.ModifyRetentionPolicyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyRetentionPolicy", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeMeasurements(self, request):
        """查看measurement列表
        :param request: Request instance for DescribeMeasurements.
        :type request: :class:`ksyun.client.influxdb.v20191010.models.DescribeMeasurementsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeMeasurements", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DeleteMeasurement(self, request):
        """删除measurement
        :param request: Request instance for DeleteMeasurement.
        :type request: :class:`ksyun.client.influxdb.v20191010.models.DeleteMeasurementRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteMeasurement", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """查看账户列表
        :param request: Request instance for DescribeAccounts.
        :type request: :class:`ksyun.client.influxdb.v20191010.models.DescribeAccountsRequest`
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
        """创建账户
        :param request: Request instance for CreateAccount.
        :type request: :class:`ksyun.client.influxdb.v20191010.models.CreateAccountRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateAccount", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """删除账户
        :param request: Request instance for DeleteAccount.
        :type request: :class:`ksyun.client.influxdb.v20191010.models.DeleteAccountRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteAccount", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeAccountPrivileges(self, request):
        """查看账户权限列表
        :param request: Request instance for DescribeAccountPrivileges.
        :type request: :class:`ksyun.client.influxdb.v20191010.models.DescribeAccountPrivilegesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeAccountPrivileges", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def GrantAccountPrivilege(self, request):
        """授予账户权限
        :param request: Request instance for GrantAccountPrivilege.
        :type request: :class:`ksyun.client.influxdb.v20191010.models.GrantAccountPrivilegeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GrantAccountPrivilege", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def RevokeAccountPrivilege(self, request):
        """回收账户权限
        :param request: Request instance for RevokeAccountPrivilege.
        :type request: :class:`ksyun.client.influxdb.v20191010.models.RevokeAccountPrivilegeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RevokeAccountPrivilege", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ResetAccountPassword(self, request):
        """重置账户密码
        :param request: Request instance for ResetAccountPassword.
        :type request: :class:`ksyun.client.influxdb.v20191010.models.ResetAccountPasswordRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ResetAccountPassword", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeAccountDetailList(self, request):
        """查看账户详情列表
        :param request: Request instance for DescribeAccountDetailList.
        :type request: :class:`ksyun.client.influxdb.v20191010.models.DescribeAccountDetailListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeAccountDetailList", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


