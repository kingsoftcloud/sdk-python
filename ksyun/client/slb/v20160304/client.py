import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class SlbClient(AbstractClient):
    _apiVersion = '2016-03-04'
    _endpoint = 'slb.api.ksyun.com'
    _service = 'slb'
    def DescribeListeners(self, request):
        """描述监听器
        :param request: Request instance for DescribeListeners.
        :type request: :class:`ksyun.client.slb.v20160304.models.DescribeListenersRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DescribeListeners", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ModifyListeners(self, request):
        """修改监听器配置
        :param request: Request instance for ModifyListeners.
        :type request: :class:`ksyun.client.slb.v20160304.models.ModifyListenersRequest`
        """
        try:
            params = request._serialize()
            body = self.call("ModifyListeners", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def CreateListeners(self, request):
        """创建监听器
        :param request: Request instance for CreateListeners.
        :type request: :class:`ksyun.client.slb.v20160304.models.CreateListenersRequest`
        """
        try:
            params = request._serialize()
            body = self.call("CreateListeners", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ModifyInstancesWithListener(self, request):
        """修改真实服务器信息
        :param request: Request instance for ModifyInstancesWithListener.
        :type request: :class:`ksyun.client.slb.v20160304.models.ModifyInstancesWithListenerRequest`
        """
        try:
            params = request._serialize()
            body = self.call("ModifyInstancesWithListener", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def RegisterInstancesWithListener(self, request):
        """监听器中绑定真实服务器
        :param request: Request instance for RegisterInstancesWithListener.
        :type request: :class:`ksyun.client.slb.v20160304.models.RegisterInstancesWithListenerRequest`
        """
        try:
            params = request._serialize()
            body = self.call("RegisterInstancesWithListener", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DeregisterInstancesFromListener(self, request):
        """解绑真实服务器
        :param request: Request instance for DeregisterInstancesFromListener.
        :type request: :class:`ksyun.client.slb.v20160304.models.DeregisterInstancesFromListenerRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DeregisterInstancesFromListener", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeInstancesWithListener(self, request):
        """描述监听器中的真实服务器
        :param request: Request instance for DescribeInstancesWithListener.
        :type request: :class:`ksyun.client.slb.v20160304.models.DescribeInstancesWithListenerRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstancesWithListener", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ModifyHealthCheck(self, request):
        """修改健康检查
        :param request: Request instance for ModifyHealthCheck.
        :type request: :class:`ksyun.client.slb.v20160304.models.ModifyHealthCheckRequest`
        """
        try:
            params = request._serialize()
            body = self.call("ModifyHealthCheck", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeHealthChecks(self, request):
        """描述健康检查
        :param request: Request instance for DescribeHealthChecks.
        :type request: :class:`ksyun.client.slb.v20160304.models.DescribeHealthChecksRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DescribeHealthChecks", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ConfigureHealthCheck(self, request):
        """创建健康检查
        :param request: Request instance for ConfigureHealthCheck.
        :type request: :class:`ksyun.client.slb.v20160304.models.ConfigureHealthCheckRequest`
        """
        try:
            params = request._serialize()
            body = self.call("ConfigureHealthCheck", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeLoadBalancers(self, request):
        """描述负载均衡
        :param request: Request instance for DescribeLoadBalancers.
        :type request: :class:`ksyun.client.slb.v20160304.models.DescribeLoadBalancersRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DescribeLoadBalancers", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ModifyLoadBalancer(self, request):
        """修改负载均衡信息
        :param request: Request instance for ModifyLoadBalancer.
        :type request: :class:`ksyun.client.slb.v20160304.models.ModifyLoadBalancerRequest`
        """
        try:
            params = request._serialize()
            body = self.call("ModifyLoadBalancer", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def CreateLoadBalancer(self, request):
        """创建负载均衡
        :param request: Request instance for CreateLoadBalancer.
        :type request: :class:`ksyun.client.slb.v20160304.models.CreateLoadBalancerRequest`
        """
        try:
            params = request._serialize()
            body = self.call("CreateLoadBalancer", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def CreateHostHeader(self, request):
        """创建应用型负载均衡域名
        :param request: Request instance for CreateHostHeader.
        :type request: :class:`ksyun.client.slb.v20160304.models.CreateHostHeaderRequest`
        """
        try:
            params = request._serialize()
            body = self.call("CreateHostHeader", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ModifyHostHeader(self, request):
        """修改应用型负载均衡域名
        :param request: Request instance for ModifyHostHeader.
        :type request: :class:`ksyun.client.slb.v20160304.models.ModifyHostHeaderRequest`
        """
        try:
            params = request._serialize()
            body = self.call("ModifyHostHeader", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DeleteHostHeader(self, request):
        """删除应用型负载均衡域名
        :param request: Request instance for DeleteHostHeader.
        :type request: :class:`ksyun.client.slb.v20160304.models.DeleteHostHeaderRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DeleteHostHeader", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeHostHeaders(self, request):
        """获取应用型负载均衡域名列表
        :param request: Request instance for DescribeHostHeaders.
        :type request: :class:`ksyun.client.slb.v20160304.models.DescribeHostHeadersRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DescribeHostHeaders", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DeleteRule(self, request):
        """删除应用型负载均衡规则
        :param request: Request instance for DeleteRule.
        :type request: :class:`ksyun.client.slb.v20160304.models.DeleteRuleRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DeleteRule", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeRules(self, request):
        """获取应用型负载均衡规则列表
        :param request: Request instance for DescribeRules.
        :type request: :class:`ksyun.client.slb.v20160304.models.DescribeRulesRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DescribeRules", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def CreateBackendServerGroup(self, request):
        """创建后端服务组
        :param request: Request instance for CreateBackendServerGroup.
        :type request: :class:`ksyun.client.slb.v20160304.models.CreateBackendServerGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call("CreateBackendServerGroup", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DeleteBackendServerGroup(self, request):
        """删除后端服务组
        :param request: Request instance for DeleteBackendServerGroup.
        :type request: :class:`ksyun.client.slb.v20160304.models.DeleteBackendServerGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DeleteBackendServerGroup", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ModifyBackendServerGroup(self, request):
        """修改后端服务组
        :param request: Request instance for ModifyBackendServerGroup.
        :type request: :class:`ksyun.client.slb.v20160304.models.ModifyBackendServerGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call("ModifyBackendServerGroup", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeBackendServerGroups(self, request):
        """获取后端服务器组列表
        :param request: Request instance for DescribeBackendServerGroups.
        :type request: :class:`ksyun.client.slb.v20160304.models.DescribeBackendServerGroupsRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DescribeBackendServerGroups", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def RegisterBackendServer(self, request):
        """注册后端服务
        :param request: Request instance for RegisterBackendServer.
        :type request: :class:`ksyun.client.slb.v20160304.models.RegisterBackendServerRequest`
        """
        try:
            params = request._serialize()
            body = self.call("RegisterBackendServer", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DeregisterBackendServer(self, request):
        """解除后端服务
        :param request: Request instance for DeregisterBackendServer.
        :type request: :class:`ksyun.client.slb.v20160304.models.DeregisterBackendServerRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DeregisterBackendServer", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeBackendServers(self, request):
        """获取后端服务器列表
        :param request: Request instance for DescribeBackendServers.
        :type request: :class:`ksyun.client.slb.v20160304.models.DescribeBackendServersRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DescribeBackendServers", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def CreateLoadBalancerAcl(self, request):
        """创建LoadBalancerAcl
        :param request: Request instance for CreateLoadBalancerAcl.
        :type request: :class:`ksyun.client.slb.v20160304.models.CreateLoadBalancerAclRequest`
        """
        try:
            params = request._serialize()
            body = self.call("CreateLoadBalancerAcl", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DeleteLoadBalancerAcl(self, request):
        """删除LoadBalancerAcl
        :param request: Request instance for DeleteLoadBalancerAcl.
        :type request: :class:`ksyun.client.slb.v20160304.models.DeleteLoadBalancerAclRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DeleteLoadBalancerAcl", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ModifyLoadBalancerAcl(self, request):
        """修改ACL信息
        :param request: Request instance for ModifyLoadBalancerAcl.
        :type request: :class:`ksyun.client.slb.v20160304.models.ModifyLoadBalancerAclRequest`
        """
        try:
            params = request._serialize()
            body = self.call("ModifyLoadBalancerAcl", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def CreateLoadBalancerAclEntry(self, request):
        """创建LoadBalancerAcl规则
        :param request: Request instance for CreateLoadBalancerAclEntry.
        :type request: :class:`ksyun.client.slb.v20160304.models.CreateLoadBalancerAclEntryRequest`
        """
        try:
            params = request._serialize()
            body = self.call("CreateLoadBalancerAclEntry", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DeleteLoadBalancerAclEntry(self, request):
        """删除LoadBalancerAcl规则
        :param request: Request instance for DeleteLoadBalancerAclEntry.
        :type request: :class:`ksyun.client.slb.v20160304.models.DeleteLoadBalancerAclEntryRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DeleteLoadBalancerAclEntry", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def AssociateLoadBalancerAcl(self, request):
        """关联负载均衡ACL
        :param request: Request instance for AssociateLoadBalancerAcl.
        :type request: :class:`ksyun.client.slb.v20160304.models.AssociateLoadBalancerAclRequest`
        """
        try:
            params = request._serialize()
            body = self.call("AssociateLoadBalancerAcl", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DisassociateLoadBalancerAcl(self, request):
        """解除关联负载均衡ACL
        :param request: Request instance for DisassociateLoadBalancerAcl.
        :type request: :class:`ksyun.client.slb.v20160304.models.DisassociateLoadBalancerAclRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DisassociateLoadBalancerAcl", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeLoadBalancerAcls(self, request):
        """查询LoadBalancerAcl
        :param request: Request instance for DescribeLoadBalancerAcls.
        :type request: :class:`ksyun.client.slb.v20160304.models.DescribeLoadBalancerAclsRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DescribeLoadBalancerAcls", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def CreateSlbRule(self, request):
        """创建域名规则
        :param request: Request instance for CreateSlbRule.
        :type request: :class:`ksyun.client.slb.v20160304.models.CreateSlbRuleRequest`
        """
        try:
            params = request._serialize()
            body = self.call("CreateSlbRule", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ModifySlbRule(self, request):
        """修改域名规则
        :param request: Request instance for ModifySlbRule.
        :type request: :class:`ksyun.client.slb.v20160304.models.ModifySlbRuleRequest`
        """
        try:
            params = request._serialize()
            body = self.call("ModifySlbRule", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def CreatePrivateLinkServer(self, request):
        """发布PrivateLink服务
        :param request: Request instance for CreatePrivateLinkServer.
        :type request: :class:`ksyun.client.slb.v20160304.models.CreatePrivateLinkServerRequest`
        """
        try:
            params = request._serialize()
            body = self.call("CreatePrivateLinkServer", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribePrivateLinkServer(self, request):
        """查看PrivateLink服务
        :param request: Request instance for DescribePrivateLinkServer.
        :type request: :class:`ksyun.client.slb.v20160304.models.DescribePrivateLinkServerRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DescribePrivateLinkServer", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DeletePrivateLinkServer(self, request):
        """删除PrivateLink服务
        :param request: Request instance for DeletePrivateLinkServer.
        :type request: :class:`ksyun.client.slb.v20160304.models.DeletePrivateLinkServerRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DeletePrivateLinkServer", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ModifyPrivateLinkServer(self, request):
        """更新PrivateLink服务
        :param request: Request instance for ModifyPrivateLinkServer.
        :type request: :class:`ksyun.client.slb.v20160304.models.ModifyPrivateLinkServerRequest`
        """
        try:
            params = request._serialize()
            body = self.call("ModifyPrivateLinkServer", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def AssociatePrivateLinkServer(self, request):
        """申请连接PrivateLink服务
        :param request: Request instance for AssociatePrivateLinkServer.
        :type request: :class:`ksyun.client.slb.v20160304.models.AssociatePrivateLinkServerRequest`
        """
        try:
            params = request._serialize()
            body = self.call("AssociatePrivateLinkServer", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribePrivateLink(self, request):
        """查询PrivateLink
        :param request: Request instance for DescribePrivateLink.
        :type request: :class:`ksyun.client.slb.v20160304.models.DescribePrivateLinkRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DescribePrivateLink", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DeletePrivateLink(self, request):
        """删除已建立的PrivateLink
        :param request: Request instance for DeletePrivateLink.
        :type request: :class:`ksyun.client.slb.v20160304.models.DeletePrivateLinkRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DeletePrivateLink", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ModifyLoadBalancerAclEntry(self, request):
        """修改LoadBalancerAcl规则
        :param request: Request instance for ModifyLoadBalancerAclEntry.
        :type request: :class:`ksyun.client.slb.v20160304.models.ModifyLoadBalancerAclEntryRequest`
        """
        try:
            params = request._serialize()
            body = self.call("ModifyLoadBalancerAclEntry", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def AcceptPrivateLink(self, request):
        """同意PrivateLink申请
        :param request: Request instance for AcceptPrivateLink.
        :type request: :class:`ksyun.client.slb.v20160304.models.AcceptPrivateLinkRequest`
        """
        try:
            params = request._serialize()
            body = self.call("AcceptPrivateLink", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def RejectPrivateLink(self, request):
        """RejectPrivateLink
        :param request: Request instance for RejectPrivateLink.
        :type request: :class:`ksyun.client.slb.v20160304.models.RejectPrivateLinkRequest`
        """
        try:
            params = request._serialize()
            body = self.call("RejectPrivateLink", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ListPrivateLinkServer(self, request):
        """查询已建立连接的privatelink列表
        :param request: Request instance for ListPrivateLinkServer.
        :type request: :class:`ksyun.client.slb.v20160304.models.ListPrivateLinkServerRequest`
        """
        try:
            params = request._serialize()
            body = self.call("ListPrivateLinkServer", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def RemovePrivateLink(self, request):
        """RemovePrivateLink
        :param request: Request instance for RemovePrivateLink.
        :type request: :class:`ksyun.client.slb.v20160304.models.RemovePrivateLinkRequest`
        """
        try:
            params = request._serialize()
            body = self.call("RemovePrivateLink", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


