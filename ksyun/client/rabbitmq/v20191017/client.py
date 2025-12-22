import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class RabbitmqClient(AbstractClient):
    _apiVersion = '2019-10-17'
    _endpoint = 'rabbitmq.api.ksyun.com'
    _service = 'rabbitmq'
    def CreateInstance(self, request):
        """创建实例。
        :param request: Request instance for CreateInstance.
        :type request: :class:`ksyun.client.rabbitmq.v20191017.models.CreateInstanceRequest`
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
        """删除实例。
        :param request: Request instance for DeleteInstance.
        :type request: :class:`ksyun.client.rabbitmq.v20191017.models.DeleteInstanceRequest`
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


    def DescribeInstances(self, request):
        """查询实例列表
        :param request: Request instance for DescribeInstances.
        :type request: :class:`ksyun.client.rabbitmq.v20191017.models.DescribeInstancesRequest`
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


    def DescribeInstance(self, request):
        """查询实例详情
        :param request: Request instance for DescribeInstance.
        :type request: :class:`ksyun.client.rabbitmq.v20191017.models.DescribeInstanceRequest`
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


    def DescribeInstanceNodes(self, request):
        """查询实例节点列表
        :param request: Request instance for DescribeInstanceNodes.
        :type request: :class:`ksyun.client.rabbitmq.v20191017.models.DescribeInstanceNodesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeInstanceNodes", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeValidRegion(self, request):
        """查询地域列表
        :param request: Request instance for DescribeValidRegion.
        :type request: :class:`ksyun.client.rabbitmq.v20191017.models.DescribeValidRegionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeValidRegion", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeRegions(self, request):
        """查询可用区列表
        :param request: Request instance for DescribeRegions.
        :type request: :class:`ksyun.client.rabbitmq.v20191017.models.DescribeRegionsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeRegions", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeSecurityGroupRules(self, request):
        """查询安全组列表
        :param request: Request instance for DescribeSecurityGroupRules.
        :type request: :class:`ksyun.client.rabbitmq.v20191017.models.DescribeSecurityGroupRulesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeSecurityGroupRules", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def AddSecurityGroupRule(self, request):
        """添加安全组规则
        :param request: Request instance for AddSecurityGroupRule.
        :type request: :class:`ksyun.client.rabbitmq.v20191017.models.AddSecurityGroupRuleRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AddSecurityGroupRule", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DeleteSecurityGroupRules(self, request):
        """删除安全组规则
        :param request: Request instance for DeleteSecurityGroupRules.
        :type request: :class:`ksyun.client.rabbitmq.v20191017.models.DeleteSecurityGroupRulesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteSecurityGroupRules", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ResetPassword(self, request):
        """实例重置密码
        :param request: Request instance for ResetPassword.
        :type request: :class:`ksyun.client.rabbitmq.v20191017.models.ResetPasswordRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ResetPassword", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def Rename(self, request):
        """实例修改名称
        :param request: Request instance for Rename.
        :type request: :class:`ksyun.client.rabbitmq.v20191017.models.RenameRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("Rename", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def AllocateEip(self, request):
        """申请外网EIP
        :param request: Request instance for AllocateEip.
        :type request: :class:`ksyun.client.rabbitmq.v20191017.models.AllocateEipRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AllocateEip", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DeallocateEip(self, request):
        """释放外网eip
        :param request: Request instance for DeallocateEip.
        :type request: :class:`ksyun.client.rabbitmq.v20191017.models.DeallocateEipRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeallocateEip", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def SupportPlugins(self, request):
        """查询实例支持的插件列表
        :param request: Request instance for SupportPlugins.
        :type request: :class:`ksyun.client.rabbitmq.v20191017.models.SupportPluginsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("SupportPlugins", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """重启实例。
        :param request: Request instance for RestartInstance.
        :type request: :class:`ksyun.client.rabbitmq.v20191017.models.RestartInstanceRequest`
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


    def ListInstancePlugins(self, request):
        """查询实例插件列表
        :param request: Request instance for ListInstancePlugins.
        :type request: :class:`ksyun.client.rabbitmq.v20191017.models.ListInstancePluginsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListInstancePlugins", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def EnableInstancePlugins(self, request):
        """实例启用插件
        :param request: Request instance for EnableInstancePlugins.
        :type request: :class:`ksyun.client.rabbitmq.v20191017.models.EnableInstancePluginsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("EnableInstancePlugins", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DisableInstancePlugins(self, request):
        """实例插件列表
        :param request: Request instance for DisableInstancePlugins.
        :type request: :class:`ksyun.client.rabbitmq.v20191017.models.DisableInstancePluginsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DisableInstancePlugins", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


