import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class KceClient(AbstractClient):
    _apiVersion = '2019-08-06'
    _endpoint = 'kce.api.ksyun.com'
    _service = 'kce'
    def DescribeCluster(self, request):
        """DescribeCluster
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
        """DescribeClusterInstance
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
        """DeleteCluster
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
        """DownloadClusterConfig
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
        """ModifyClusterInfo
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
        """DescribeInstanceImage
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
        """AddClusterInstances
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
        """DeleteClusterInstances
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
        """DescribeEpcForCluster
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
        """AddClusterEpcInstances
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
        """获取KEC实例列表
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
        """添加KEC节点到集群
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


    def ForceRemoveClusterInstance(self, request):
        """强制删除集群节点
        :param request: Request instance for ForceRemoveClusterInstance.
        :type request: :class:`ksyun.client.kce.v20190806.models.ForceRemoveClusterInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ForceRemoveClusterInstance", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """查询EPC镜像
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


