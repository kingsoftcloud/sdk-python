import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class SlbClient(AbstractClient):
    _apiVersion = '2025-04-30'
    _endpoint = 'slb.api.ksyun.com'
    _service = 'slb'

    def DescribeBackendServers(self, request):
        """查询服务器信息
        :param request: Request instance for DescribeBackendServers.
        :type request: :class:`ksyun.client.slb.v20250430.models.DescribeBackendServersRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeBackendServers", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def ModifyBackendServer(self, request):
        """修改服务器信息
        :param request: Request instance for ModifyBackendServer.
        :type request: :class:`ksyun.client.slb.v20250430.models.ModifyBackendServerRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyBackendServer", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """从服务器组移除服务器
        :param request: Request instance for DeregisterBackendServer.
        :type request: :class:`ksyun.client.slb.v20250430.models.DeregisterBackendServerRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeregisterBackendServer", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """注册服务器到服务组
        :param request: Request instance for RegisterBackendServer.
        :type request: :class:`ksyun.client.slb.v20250430.models.RegisterBackendServerRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RegisterBackendServer", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """查询服务器组
        :param request: Request instance for DescribeBackendServerGroups.
        :type request: :class:`ksyun.client.slb.v20250430.models.DescribeBackendServerGroupsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeBackendServerGroups", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """修改服务器组
        :param request: Request instance for ModifyBackendServerGroup.
        :type request: :class:`ksyun.client.slb.v20250430.models.ModifyBackendServerGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyBackendServerGroup", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """删除服务器组
        :param request: Request instance for DeleteBackendServerGroup.
        :type request: :class:`ksyun.client.slb.v20250430.models.DeleteBackendServerGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteBackendServerGroup", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """创建服务器组
        :param request: Request instance for CreateBackendServerGroup.
        :type request: :class:`ksyun.client.slb.v20250430.models.CreateBackendServerGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateBackendServerGroup", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def DescribeListeners(self, request):
        """查询监听器
        :param request: Request instance for DescribeListeners.
        :type request: :class:`ksyun.client.slb.v20250430.models.DescribeListenersRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeListeners", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def ModifyListener(self, request):
        """修改监听器
        :param request: Request instance for ModifyListener.
        :type request: :class:`ksyun.client.slb.v20250430.models.ModifyListenerRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyListener", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def DeleteListener(self, request):
        """删除监听器
        :param request: Request instance for DeleteListener.
        :type request: :class:`ksyun.client.slb.v20250430.models.DeleteListenerRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteListener", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def CreateListener(self, request):
        """创建监听器
        :param request: Request instance for CreateListener.
        :type request: :class:`ksyun.client.slb.v20250430.models.CreateListenerRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateListener", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def SetAccessLog(self, request):
        """创建/修改访问日志对接klog
        :param request: Request instance for SetAccessLog.
        :type request: :class:`ksyun.client.slb.v20250430.models.SetAccessLogRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("SetAccessLog", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def SetEnableAccessLog(self, request):
        """设置访问日志对接klog开关
        :param request: Request instance for SetEnableAccessLog.
        :type request: :class:`ksyun.client.slb.v20250430.models.SetEnableAccessLogRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("SetEnableAccessLog", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def SetLbProtocolLayers(self, request):
        """设置LB的协议层数
        :param request: Request instance for SetLbProtocolLayers.
        :type request: :class:`ksyun.client.slb.v20250430.models.SetLbProtocolLayersRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("SetLbProtocolLayers", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """修改高阶/hpa配置接口
        :param request: Request instance for ModifyLoadBalancer.
        :type request: :class:`ksyun.client.slb.v20250430.models.ModifyLoadBalancerRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyLoadBalancer", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def SetLoadBalancerStatus(self, request):
        """设置负载均衡状态
        :param request: Request instance for SetLoadBalancerStatus.
        :type request: :class:`ksyun.client.slb.v20250430.models.SetLoadBalancerStatusRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("SetLoadBalancerStatus", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def SetLoadBalancerName(self, request):
        """设置负载均衡名称
        :param request: Request instance for SetLoadBalancerName.
        :type request: :class:`ksyun.client.slb.v20250430.models.SetLoadBalancerNameRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("SetLoadBalancerName", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """查询负载均衡
        :param request: Request instance for DescribeLoadBalancers.
        :type request: :class:`ksyun.client.slb.v20250430.models.DescribeLoadBalancersRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeLoadBalancers", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def DeleteLoadBalancer(self, request):
        """删除负载均衡
        :param request: Request instance for DeleteLoadBalancer.
        :type request: :class:`ksyun.client.slb.v20250430.models.DeleteLoadBalancerRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteLoadBalancer", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        :type request: :class:`ksyun.client.slb.v20250430.models.CreateLoadBalancerRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateLoadBalancer", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def ModifyCertificateWithGroup(self, request):
        """监听器维度更换同域名的证书
        :param request: Request instance for ModifyCertificateWithGroup.
        :type request: :class:`ksyun.client.slb.v20250430.models.ModifyCertificateWithGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyCertificateWithGroup", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def DissociateCertificateWithGroup(self, request):
        """移除证书出证书组
        :param request: Request instance for DissociateCertificateWithGroup.
        :type request: :class:`ksyun.client.slb.v20250430.models.DissociateCertificateWithGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DissociateCertificateWithGroup", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def AssociateCertificateWithGroup(self, request):
        """添加证书进证书组
        :param request: Request instance for AssociateCertificateWithGroup.
        :type request: :class:`ksyun.client.slb.v20250430.models.AssociateCertificateWithGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AssociateCertificateWithGroup", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def DescribeListenerCertGroups(self, request):
        """描述证书组
        :param request: Request instance for DescribeListenerCertGroups.
        :type request: :class:`ksyun.client.slb.v20250430.models.DescribeListenerCertGroupsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeListenerCertGroups", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def DeleteListenerCertGroup(self, request):
        """删除证书组
        :param request: Request instance for DeleteListenerCertGroup.
        :type request: :class:`ksyun.client.slb.v20250430.models.DeleteListenerCertGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteListenerCertGroup", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def CreateListenerCertGroup(self, request):
        """创建证书组
        :param request: Request instance for CreateListenerCertGroup.
        :type request: :class:`ksyun.client.slb.v20250430.models.CreateListenerCertGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateListenerCertGroup", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def AddRules(self, request):
        """添加多个转发规则
        :param request: Request instance for AddRules.
        :type request: :class:`ksyun.client.slb.v20250430.models.AddRulesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AddRules", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """删除转发策略规则
        :param request: Request instance for DeleteRule.
        :type request: :class:`ksyun.client.slb.v20250430.models.DeleteRuleRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteRule", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def AddRule(self, request):
        """创建转发策略规则
        :param request: Request instance for AddRule.
        :type request: :class:`ksyun.client.slb.v20250430.models.AddRuleRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AddRule", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def ModifyRuleGroup(self, request):
        """修改转发策略
        :param request: Request instance for ModifyRuleGroup.
        :type request: :class:`ksyun.client.slb.v20250430.models.ModifyRuleGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyRuleGroup", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def DescribeRuleGroups(self, request):
        """描述转发策略
        :param request: Request instance for DescribeRuleGroups.
        :type request: :class:`ksyun.client.slb.v20250430.models.DescribeRuleGroupsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeRuleGroups", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def DeleteRuleGroup(self, request):
        """删除转发策略
        :param request: Request instance for DeleteRuleGroup.
        :type request: :class:`ksyun.client.slb.v20250430.models.DeleteRuleGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteRuleGroup", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def CreateRuleGroup(self, request):
        """创建转发策略
        :param request: Request instance for CreateRuleGroup.
        :type request: :class:`ksyun.client.slb.v20250430.models.CreateRuleGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateRuleGroup", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def SetLBModificationProtection(self, request):
        """负载均衡修改保护
        :param request: Request instance for SetLBModificationProtection.
        :type request: :class:`ksyun.client.slb.v20250430.models.SetLBModificationProtectionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("SetLBModificationProtection", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def SetLBDeleteProtection(self, request):
        """负载均衡删除保护
        :param request: Request instance for SetLBDeleteProtection.
        :type request: :class:`ksyun.client.slb.v20250430.models.SetLBDeleteProtectionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("SetLBDeleteProtection", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)
