import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class KesClient(AbstractClient):
    _apiVersion = '2020-12-15'
    _endpoint = 'kes.api.ksyun.com'
    _service = 'kes'
    def DescribeCluster(self, request):
        """查询集群详情V2
        :param request: Request instance for DescribeCluster.
        :type request: :class:`ksyun.client.kes.v20201215.models.DescribeClusterRequest`
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


    def ListClusters(self, request):
        """查看集群列表V2
        :param request: Request instance for ListClusters.
        :type request: :class:`ksyun.client.kes.v20201215.models.ListClustersRequest`
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


    def ModifyClusterName(self, request):
        """修改集群名称V2
        :param request: Request instance for ModifyClusterName.
        :type request: :class:`ksyun.client.kes.v20201215.models.ModifyClusterNameRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyClusterName", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """创建集群V2
        :param request: Request instance for LaunchCluster.
        :type request: :class:`ksyun.client.kes.v20201215.models.LaunchClusterRequest`
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


    def ListInstanceGroups(self, request):
        """查询节点组详情V2
        :param request: Request instance for ListInstanceGroups.
        :type request: :class:`ksyun.client.kes.v20201215.models.ListInstanceGroupsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListInstanceGroups", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ServiceControl(self, request):
        """重启集群V2
        :param request: Request instance for ServiceControl.
        :type request: :class:`ksyun.client.kes.v20201215.models.ServiceControlRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ServiceControl", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ClusterHealthStatistic(self, request):
        """查看诊断报告V2
        :param request: Request instance for ClusterHealthStatistic.
        :type request: :class:`ksyun.client.kes.v20201215.models.ClusterHealthStatisticRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ClusterHealthStatistic", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def CheckClusterHealth(self, request):
        """立即诊断V2
        :param request: Request instance for CheckClusterHealth.
        :type request: :class:`ksyun.client.kes.v20201215.models.CheckClusterHealthRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CheckClusterHealth", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


