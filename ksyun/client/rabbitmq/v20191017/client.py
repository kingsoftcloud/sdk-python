import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class RabbitmqClient(AbstractClient):
    _apiVersion = '2019-10-17'
    _endpoint = 'rabbitmq.api.ksyun.com'
    _service = 'rabbitmq'
    def CreateInstance(self, request):
        """创建实例
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
        """删除实例
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
        """实例列表
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
        """实例明细
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
        """实例节点列表
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
        """控制台有效机房列表
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
        """客户获取机房列表信息
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
        """实例白名单列表
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
        """添加实例白名单
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
        """删除实例白名单
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


