import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class ClickhouseClient(AbstractClient):
    _apiVersion = '2021-01-01'
    _endpoint = 'clickhouse.api.ksyun.com'
    _service = 'clickhouse'

    def ListInstance(self, request):
        """Clickhouse查询实例列表
        :param request: Request instance for ListInstance.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.ListInstanceRequest`
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
        """Clickhouse查看实例详情
        :param request: Request instance for DescribeInstance.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.DescribeInstanceRequest`
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

    def CreateInstance(self, request):
        """Clickhouse创建实例
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
        """Clickhouse删除实例
        :param request: Request instance for DeleteInstance.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.DeleteInstanceRequest`
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
        """Clickhouse重命名实例
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
        """Clickhouse查看安全组列表
        :param request: Request instance for ListSecurityGroup.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.ListSecurityGroupRequest`
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
        """Clickhouse查看安全组详情
        :param request: Request instance for DescribeSecurityGroup.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.DescribeSecurityGroupRequest`
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

    def CreateSecurityGroup(self, request):
        """Clickhouse创建安全组
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
        """Clickhouse删除安全组接口
        :param request: Request instance for DeleteSecurityGroup.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.DeleteSecurityGroupRequest`
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

    def RenameSecurityGroup(self, request):
        """Clickhouse重命名安全组
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
        """Clickhouse克隆安全组
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
        """Clickhouse绑定安全组
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
        """Clickhouse解绑安全组
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
        """Clickhouse创建安全规则
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
        """Clickhouse删除安全规则
        :param request: Request instance for DeleteSecurityRule.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.DeleteSecurityRuleRequest`
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
        """Clickhouse查询已绑定安全组的实例列表
        :param request: Request instance for ListSecuredInstance.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.ListSecuredInstanceRequest`
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
        """Clickhouse查询未绑定安全组的实例列表
        :param request: Request instance for ListUnsecuredInstance.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.ListUnsecuredInstanceRequest`
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

    def ListRecycledInstance(self, request):
        """Clickhouse查询回收站实例列表
        :param request: Request instance for ListRecycledInstance.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.ListRecycledInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListRecycledInstance", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """Clickhouse恢复实例
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
        """Clickhouse彻底删除实例
        :param request: Request instance for DropRecycledInstance.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.DropRecycledInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DropRecycledInstance", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """Clickhouse查询地域列表
        :param request: Request instance for ListRegion.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.ListRegionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListRegion", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """Clickhouse查询地域详情
        :param request: Request instance for DescRegion.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.DescRegionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescRegion", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """Clickhouse更新安全规则备注
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
        """Clickhouse实例重新绑定安全组
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
        """Clickhouse根据版本查询实例默认参数配置
        :param request: Request instance for DescribeEngineDefaultParameters.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.DescribeEngineDefaultParametersRequest`
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

    def ModifyDBParameterGroup(self, request):
        """Clickhouse修改实例参数
        :param request: Request instance for ModifyDBParameterGroup.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.ModifyDBParameterGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyDBParameterGroup", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """Clickhouse查询当前实例参数配置
        :param request: Request instance for DescribeDBInstanceParameters.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.DescribeDBInstanceParametersRequest`
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

    def ResetDBParameter(self, request):
        """Clickhouse重置实例参数
        :param request: Request instance for ResetDBParameter.
        :type request: :class:`ksyun.client.clickhouse.v20210101.models.ResetDBParameterRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ResetDBParameter", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)
