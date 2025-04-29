import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class KceClient(AbstractClient):
    _apiVersion = '2019-08-06'
    _endpoint = 'kce.api.ksyun.com'
    _service = 'kce'

    def DescribeCluster(self, request):
        """查询集群列表
        :param request: Request instance for DescribeCluster.
        :type request: :class:`ksyun.client.kce.v20190806.models.DescribeClusterRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeCluster", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def DescribeClusterInstance(self, request):
        """查询集群节点列表
        :param request: Request instance for DescribeClusterInstance.
        :type request: :class:`ksyun.client.kce.v20190806.models.DescribeClusterInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeClusterInstance", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def DeleteCluster(self, request):
        """删除集群
        :param request: Request instance for DeleteCluster.
        :type request: :class:`ksyun.client.kce.v20190806.models.DeleteClusterRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteCluster", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def DownloadClusterConfig(self, request):
        """下载集群配置文件
        :param request: Request instance for DownloadClusterConfig.
        :type request: :class:`ksyun.client.kce.v20190806.models.DownloadClusterConfigRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DownloadClusterConfig", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def ModifyClusterInfo(self, request):
        """修改集群基本信息
        :param request: Request instance for ModifyClusterInfo.
        :type request: :class:`ksyun.client.kce.v20190806.models.ModifyClusterInfoRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyClusterInfo", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def DescribeInstanceImage(self, request):
        """获取容器服务支持的节点操作系统
        :param request: Request instance for DescribeInstanceImage.
        :type request: :class:`ksyun.client.kce.v20190806.models.DescribeInstanceImageRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeInstanceImage", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def AddClusterInstances(self, request):
        """新增节点
        :param request: Request instance for AddClusterInstances.
        :type request: :class:`ksyun.client.kce.v20190806.models.AddClusterInstancesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AddClusterInstances", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def DeleteClusterInstances(self, request):
        """移除集群中的节点
        :param request: Request instance for DeleteClusterInstances.
        :type request: :class:`ksyun.client.kce.v20190806.models.DeleteClusterInstancesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteClusterInstances", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def DescribeEpcForCluster(self, request):
        """获取支持移入集群的裸金属服务器列表
        :param request: Request instance for DescribeEpcForCluster.
        :type request: :class:`ksyun.client.kce.v20190806.models.DescribeEpcForClusterRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeEpcForCluster", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def AddClusterEpcInstances(self, request):
        """移入裸金属服务器到集群
        :param request: Request instance for AddClusterEpcInstances.
        :type request: :class:`ksyun.client.kce.v20190806.models.AddClusterEpcInstancesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AddClusterEpcInstances", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def DescribeExistedInstances(self, request):
        """查询已经存在的云服务器
        :param request: Request instance for DescribeExistedInstances.
        :type request: :class:`ksyun.client.kce.v20190806.models.DescribeExistedInstancesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeExistedInstances", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def AddExistedInstances(self, request):
        """添加已有的服务器
        :param request: Request instance for AddExistedInstances.
        :type request: :class:`ksyun.client.kce.v20190806.models.AddExistedInstancesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AddExistedInstances", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def CreateNodePool(self, request):
        """创建节点池
        :param request: Request instance for CreateNodePool.
        :type request: :class:`ksyun.client.kce.v20190806.models.CreateNodePoolRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateNodePool", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def DescribeNodePool(self, request):
        """查询节点池详细信息
        :param request: Request instance for DescribeNodePool.
        :type request: :class:`ksyun.client.kce.v20190806.models.DescribeNodePoolRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeNodePool", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def DeleteNodePool(self, request):
        """删除节点池
        :param request: Request instance for DeleteNodePool.
        :type request: :class:`ksyun.client.kce.v20190806.models.DeleteNodePoolRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteNodePool", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def ModifyNodePool(self, request):
        """修改节点池
        :param request: Request instance for ModifyNodePool.
        :type request: :class:`ksyun.client.kce.v20190806.models.ModifyNodePoolRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyNodePool", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def ModifyNodeTemplate(self, request):
        """修改节点池模板
        :param request: Request instance for ModifyNodeTemplate.
        :type request: :class:`ksyun.client.kce.v20190806.models.ModifyNodeTemplateRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyNodeTemplate", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def ModifyNodePoolScaleUpPolicy(self, request):
        """修改节点池扩容策略
        :param request: Request instance for ModifyNodePoolScaleUpPolicy.
        :type request: :class:`ksyun.client.kce.v20190806.models.ModifyNodePoolScaleUpPolicyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyNodePoolScaleUpPolicy", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def ModifyNodePoolScaleDownPolicy(self, request):
        """修改节点池缩容策略
        :param request: Request instance for ModifyNodePoolScaleDownPolicy.
        :type request: :class:`ksyun.client.kce.v20190806.models.ModifyNodePoolScaleDownPolicyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyNodePoolScaleDownPolicy", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def AddClusterInstanceToNodePool(self, request):
        """将集群内节点移入节点池
        :param request: Request instance for AddClusterInstanceToNodePool.
        :type request: :class:`ksyun.client.kce.v20190806.models.AddClusterInstanceToNodePoolRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AddClusterInstanceToNodePool", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def ProtectedFromScaleDown(self, request):
        """节点池节点设置缩容保护
        :param request: Request instance for ProtectedFromScaleDown.
        :type request: :class:`ksyun.client.kce.v20190806.models.ProtectedFromScaleDownRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ProtectedFromScaleDown", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def DeleteClusterInstancesFromNodePool(self, request):
        """移出节点池节点
        :param request: Request instance for DeleteClusterInstancesFromNodePool.
        :type request: :class:`ksyun.client.kce.v20190806.models.DeleteClusterInstancesFromNodePoolRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteClusterInstancesFromNodePool", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def DescribeEpcImage(self, request):
        """获取裸金属服务器支持的系统镜像
        :param request: Request instance for DescribeEpcImage.
        :type request: :class:`ksyun.client.kce.v20190806.models.DescribeEpcImageRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeEpcImage", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def EditEventCollecting(self, request):
        """开启事件推送
        :param request: Request instance for EditEventCollecting.
        :type request: :class:`ksyun.client.kce.v20190806.models.EditEventCollectingRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("EditEventCollecting", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def DescribeNodePoolSummary(self, request):
        """查询集群全量节点池的轻量级API
        :param request: Request instance for DescribeNodePoolSummary.
        :type request: :class:`ksyun.client.kce.v20190806.models.DescribeNodePoolSummaryRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeNodePoolSummary", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)
