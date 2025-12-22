import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class ClickhouseClient(AbstractClient):
    _apiVersion = '2021-01-01'
    _endpoint = 'clickhouse.api.ksyun.com'
    _service = 'clickhouse'
    def ListInstance(self, request):
        """查询实例列表
        :param request: Request instance for ListInstance.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.ListInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListInstance", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.DescribeInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeInstance", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def CreateInstance(self, request):
        """创建实例(支持指定计费方式)
        :param request: Request instance for CreateInstance.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.CreateInstanceRequest`
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
        """删除实例(默认放入回收站)
        :param request: Request instance for DeleteInstance.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.DeleteInstanceRequest`
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


    def RestartInstance(self, request):
        """重启实例(指定实例ID重启)
        :param request: Request instance for RestartInstance.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.RestartInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RestartInstance", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """修改实例名称
        :param request: Request instance for RenameInstance.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.RenameInstanceRequest`
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


    def ListSecurityGroup(self, request):
        """查看安全组列表
        :param request: Request instance for ListSecurityGroup.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.ListSecurityGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListSecurityGroup", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """查看安全组详情
        :param request: Request instance for DescribeSecurityGroup.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.DescribeSecurityGroupRequest`
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


    def CreateSecurityGroup(self, request):
        """创建安全组
        :param request: Request instance for CreateSecurityGroup.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.CreateSecurityGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateSecurityGroup", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.DeleteSecurityGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteSecurityGroup", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def RenameSecurityGroup(self, request):
        """重命名安全组
        :param request: Request instance for RenameSecurityGroup.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.RenameSecurityGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RenameSecurityGroup", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.CloneSecurityGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CloneSecurityGroup", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """绑定安全组
        :param request: Request instance for BindSecurityGroup.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.BindSecurityGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("BindSecurityGroup", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """解绑安全组
        :param request: Request instance for UnbindSecurityGroup.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.UnbindSecurityGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UnbindSecurityGroup", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """创建安全规则(添加自定义IP地址+绑定云主机IP)
        :param request: Request instance for CreateSecurityRule.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.CreateSecurityRuleRequest`
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
        """删除安全规则(移除IP地址)
        :param request: Request instance for DeleteSecurityRule.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.DeleteSecurityRuleRequest`
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


    def ListSecuredInstance(self, request):
        """查询已绑定安全组的实例列表
        :param request: Request instance for ListSecuredInstance.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.ListSecuredInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListSecuredInstance", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """查询未绑定安全组的实例列表
        :param request: Request instance for ListUnsecuredInstance.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.ListUnsecuredInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListUnsecuredInstance", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ListRecycledInstance(self, request):
        """查询实例列表(回收站)
        :param request: Request instance for ListRecycledInstance.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.ListRecycledInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListRecycledInstance", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def RecoverRecycledInstance(self, request):
        """恢复实例(回收站实例重新移入正常实例列表)
        :param request: Request instance for RecoverRecycledInstance.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.RecoverRecycledInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RecoverRecycledInstance", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DropRecycledInstance(self, request):
        """彻底删除实例(回收站清空)
        :param request: Request instance for DropRecycledInstance.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.DropRecycledInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DropRecycledInstance", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.ListRegionRequest`
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
        """查询可用区详情
        :param request: Request instance for DescRegion.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.DescRegionRequest`
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


    def UpdateSecurityRule(self, request):
        """修改安全规则备注(具体的IP规则描述)
        :param request: Request instance for UpdateSecurityRule.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.UpdateSecurityRuleRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateSecurityRule", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """重新绑定安全组
        :param request: Request instance for RebindSecurityGroup.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.RebindSecurityGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RebindSecurityGroup", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """查询实例默认参数
        :param request: Request instance for DescribeEngineDefaultParameters.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.DescribeEngineDefaultParametersRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeEngineDefaultParameters", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """修改实例参数
        :param request: Request instance for ModifyDBParameterGroup.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.ModifyDBParameterGroupRequest`
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


    def DescribeDBInstanceParameters(self, request):
        """查询实例当前参数
        :param request: Request instance for DescribeDBInstanceParameters.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.DescribeDBInstanceParametersRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDBInstanceParameters", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ResetDBParameter(self, request):
        """重置实例参数
        :param request: Request instance for ResetDBParameter.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.ResetDBParameterRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ResetDBParameter", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeBuckets(self, request):
        """查询当前用桶列表
        :param request: Request instance for DescribeBuckets.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.DescribeBucketsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeBuckets", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def OperateHotAndColdSeparation(self, request):
        """冷热数据分层配置
        :param request: Request instance for OperateHotAndColdSeparation.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.OperateHotAndColdSeparationRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("OperateHotAndColdSeparation", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """创建指定实例的数据库账号(普通用户)
        :param request: Request instance for CreateInstanceAccount.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.CreateInstanceAccountRequest`
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


    def ModifyInstanceAccountPrivileges(self, request):
        """修改实例指定用户的数据库权限
        :param request: Request instance for ModifyInstanceAccountPrivileges.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.ModifyInstanceAccountPrivilegesRequest`
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
        """删除指定实例数据库账号
        :param request: Request instance for DeleteInstanceAccount.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.DeleteInstanceAccountRequest`
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


    def DescribeInstanceAccounts(self, request):
        """查询指定实例数据库账号列表
        :param request: Request instance for DescribeInstanceAccounts.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.DescribeInstanceAccountsRequest`
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


    def DescribeInstanceDatabases(self, request):
        """查询库表列表
        :param request: Request instance for DescribeInstanceDatabases.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.DescribeInstanceDatabasesRequest`
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


    def ModifyInstanceAccountInfo(self, request):
        """修改实例账号密码或者描述
        :param request: Request instance for ModifyInstanceAccountInfo.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.ModifyInstanceAccountInfoRequest`
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


    def DescribeInstanceShardInfo(self, request):
        """查询集群拓扑图(拓扑关系数据)
        :param request: Request instance for DescribeInstanceShardInfo.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.DescribeInstanceShardInfoRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeInstanceShardInfo", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.UpdateInstanceTrialOrderRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateInstanceTrialOrder", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


