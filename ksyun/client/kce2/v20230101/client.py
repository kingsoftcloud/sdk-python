import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class Kce2Client(AbstractClient):
    _apiVersion = '2023-01-01'
    _endpoint = 'kce2.api.ksyun.com'
    _service = 'kce2'
    def CreateCluster(self, request):
        """创建容器集群
        :param request: Request instance for CreateCluster.
        :type request: :class:`ksyun.client.kce2.v20230101.models.CreateClusterRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateCluster", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeClusters(self, request):
        """查询集群列表
        :param request: Request instance for DescribeClusters.
        :type request: :class:`ksyun.client.kce2.v20230101.models.DescribeClustersRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeClusters", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """删除容器集群
        :param request: Request instance for DeleteCluster.
        :type request: :class:`ksyun.client.kce2.v20230101.models.DeleteClusterRequest`
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


    def ModifyCluster(self, request):
        """修改集群配置
        :param request: Request instance for ModifyCluster.
        :type request: :class:`ksyun.client.kce2.v20230101.models.ModifyClusterRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyCluster", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeNodes(self, request):
        """查询集群节点列表
        :param request: Request instance for DescribeNodes.
        :type request: :class:`ksyun.client.kce2.v20230101.models.DescribeNodesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeNodes", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DeleteNode(self, request):
        """删除集群节点
        :param request: Request instance for DeleteNode.
        :type request: :class:`ksyun.client.kce2.v20230101.models.DeleteNodeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteNode", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ModifyNode(self, request):
        """修改节点组件
        :param request: Request instance for ModifyNode.
        :type request: :class:`ksyun.client.kce2.v20230101.models.ModifyNodeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyNode", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeComponentList(self, request):
        """查询可安装的组件列表
        :param request: Request instance for DescribeComponentList.
        :type request: :class:`ksyun.client.kce2.v20230101.models.DescribeComponentListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeComponentList", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeNodeComponents(self, request):
        """查询节点组件列表
        :param request: Request instance for DescribeNodeComponents.
        :type request: :class:`ksyun.client.kce2.v20230101.models.DescribeNodeComponentsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeNodeComponents", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeNetwork(self, request):
        """查询集群网络
        :param request: Request instance for DescribeNetwork.
        :type request: :class:`ksyun.client.kce2.v20230101.models.DescribeNetworkRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeNetwork", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeComponentParams(self, request):
        """查询组件参数版本
        :param request: Request instance for DescribeComponentParams.
        :type request: :class:`ksyun.client.kce2.v20230101.models.DescribeComponentParamsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeComponentParams", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeEventLogs(self, request):
        """查询集群事件日志
        :param request: Request instance for DescribeEventLogs.
        :type request: :class:`ksyun.client.kce2.v20230101.models.DescribeEventLogsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeEventLogs", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeClusterVersionList(self, request):
        """查询集群版本信息
        :param request: Request instance for DescribeClusterVersionList.
        :type request: :class:`ksyun.client.kce2.v20230101.models.DescribeClusterVersionListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeClusterVersionList", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def AddKecNodes(self, request):
        """给集群添加新kec节点或已有kec节点
        :param request: Request instance for AddKecNodes.
        :type request: :class:`ksyun.client.kce2.v20230101.models.AddKecNodesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AddKecNodes", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def AddEpcNodes(self, request):
        """给集群添加新Epc节点或已有Epc节点
        :param request: Request instance for AddEpcNodes.
        :type request: :class:`ksyun.client.kce2.v20230101.models.AddEpcNodesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AddEpcNodes", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


