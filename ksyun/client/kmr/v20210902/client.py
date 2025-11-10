import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class KmrClient(AbstractClient):
    _apiVersion = '2021-09-02'
    _endpoint = 'kmr.api.ksyun.com'
    _service = 'kmr'
    def DescribeCluster(self, request):
        """集群详情
        :param request: Request instance for DescribeCluster.
        :type request: :class:`ksyun.client.kmr.v20210902.models.DescribeClusterRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeCluster", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def LaunchCluster(self, request):
        """创建集群
        :param request: Request instance for LaunchCluster.
        :type request: :class:`ksyun.client.kmr.v20210902.models.LaunchClusterRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("LaunchCluster", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ScaleInInstanceGroups(self, request):
        """缩容集群
        :param request: Request instance for ScaleInInstanceGroups.
        :type request: :class:`ksyun.client.kmr.v20210902.models.ScaleInInstanceGroupsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ScaleInInstanceGroups", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ScaleOutInstanceGroups(self, request):
        """扩容集群
        :param request: Request instance for ScaleOutInstanceGroups.
        :type request: :class:`ksyun.client.kmr.v20210902.models.ScaleOutInstanceGroupsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ScaleOutInstanceGroups", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeClusterInfo(self, request):
        """集群详情描述
        :param request: Request instance for DescribeClusterInfo.
        :type request: :class:`ksyun.client.kmr.v20210902.models.DescribeClusterInfoRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeClusterInfo", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ListServiceStatus(self, request):
        """查看服务列表
        :param request: Request instance for ListServiceStatus.
        :type request: :class:`ksyun.client.kmr.v20210902.models.ListServiceStatusRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListServiceStatus", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ListClusters(self, request):
        """集群列表
        :param request: Request instance for ListClusters.
        :type request: :class:`ksyun.client.kmr.v20210902.models.ListClustersRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListClusters", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ListClusterVersions(self, request):
        """集群版本列表
        :param request: Request instance for ListClusterVersions.
        :type request: :class:`ksyun.client.kmr.v20210902.models.ListClusterVersionsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListClusterVersions", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeService(self, request):
        """查看服务详情
        :param request: Request instance for DescribeService.
        :type request: :class:`ksyun.client.kmr.v20210902.models.DescribeServiceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeService", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ListConfigurations(self, request):
        """配置列表
        :param request: Request instance for ListConfigurations.
        :type request: :class:`ksyun.client.kmr.v20210902.models.ListConfigurationsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListConfigurations", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ListConfigurationHistory(self, request):
        """配置历史
        :param request: Request instance for ListConfigurationHistory.
        :type request: :class:`ksyun.client.kmr.v20210902.models.ListConfigurationHistoryRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListConfigurationHistory", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ListTagValues(self, request):
        """标签值列表
        :param request: Request instance for ListTagValues.
        :type request: :class:`ksyun.client.kmr.v20210902.models.ListTagValuesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListTagValues", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ListTagKeys(self, request):
        """标签列表
        :param request: Request instance for ListTagKeys.
        :type request: :class:`ksyun.client.kmr.v20210902.models.ListTagKeysRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListTagKeys", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def BindTags(self, request):
        """绑定标签
        :param request: Request instance for BindTags.
        :type request: :class:`ksyun.client.kmr.v20210902.models.BindTagsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("BindTags", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def StartInstances(self, request):
        """启动实例
        :param request: Request instance for StartInstances.
        :type request: :class:`ksyun.client.kmr.v20210902.models.StartInstancesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("StartInstances", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def RestartInstances(self, request):
        """重启实例
        :param request: Request instance for RestartInstances.
        :type request: :class:`ksyun.client.kmr.v20210902.models.RestartInstancesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RestartInstances", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def StopInstances(self, request):
        """停止实例
        :param request: Request instance for StopInstances.
        :type request: :class:`ksyun.client.kmr.v20210902.models.StopInstancesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("StopInstances", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ListScaleStrategy(self, request):
        """弹性策略列表
        :param request: Request instance for ListScaleStrategy.
        :type request: :class:`ksyun.client.kmr.v20210902.models.ListScaleStrategyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListScaleStrategy", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ModifyScaleStrategy(self, request):
        """弹性策略描述
        :param request: Request instance for ModifyScaleStrategy.
        :type request: :class:`ksyun.client.kmr.v20210902.models.ModifyScaleStrategyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyScaleStrategy", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DeleteScaleStrategy(self, request):
        """删除弹性策略
        :param request: Request instance for DeleteScaleStrategy.
        :type request: :class:`ksyun.client.kmr.v20210902.models.DeleteScaleStrategyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteScaleStrategy", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ListScaleHistory(self, request):
        """弹性伸缩历史
        :param request: Request instance for ListScaleHistory.
        :type request: :class:`ksyun.client.kmr.v20210902.models.ListScaleHistoryRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListScaleHistory", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def AddLoadBasedScaleStrategy(self, request):
        """添加负载弹性策略
        :param request: Request instance for AddLoadBasedScaleStrategy.
        :type request: :class:`ksyun.client.kmr.v20210902.models.AddLoadBasedScaleStrategyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AddLoadBasedScaleStrategy", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ModifyLoadBasedScaleStrategy(self, request):
        """修改负载弹性策略
        :param request: Request instance for ModifyLoadBasedScaleStrategy.
        :type request: :class:`ksyun.client.kmr.v20210902.models.ModifyLoadBasedScaleStrategyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyLoadBasedScaleStrategy", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


