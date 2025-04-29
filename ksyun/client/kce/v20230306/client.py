import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class KceClient(AbstractClient):
    _apiVersion = '2023-03-06'
    _endpoint = 'kce.api.ksyun.com'
    _service = 'kce'

    def CreatePrometheusInstance(self, request):
        """创建Prometheus实例
        :param request: Request instance for CreatePrometheusInstance.
        :type request: :class:`ksyun.client.kce.v20230306.models.CreatePrometheusInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreatePrometheusInstance", params, "application/x-www-form-urlencoded")
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

    def DescribePrometheusInstance(self, request):
        """查询Prometheus实例
        :param request: Request instance for DescribePrometheusInstance.
        :type request: :class:`ksyun.client.kce.v20230306.models.DescribePrometheusInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribePrometheusInstance", params, "application/x-www-form-urlencoded")
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

    def UpdatePrometheusInstance(self, request):
        """更新Prometheus实例
        :param request: Request instance for UpdatePrometheusInstance.
        :type request: :class:`ksyun.client.kce.v20230306.models.UpdatePrometheusInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdatePrometheusInstance", params, "application/x-www-form-urlencoded")
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

    def DeletePrometheusInstance(self, request):
        """删除Prometheus实例
        :param request: Request instance for DeletePrometheusInstance.
        :type request: :class:`ksyun.client.kce.v20230306.models.DeletePrometheusInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeletePrometheusInstance", params, "application/x-www-form-urlencoded")
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

    def EnableGrafana(self, request):
        """开通/关闭Grafana
        :param request: Request instance for EnableGrafana.
        :type request: :class:`ksyun.client.kce.v20230306.models.EnableGrafanaRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("EnableGrafana", params, "application/x-www-form-urlencoded")
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

    def UpdateGrafanaPassword(self, request):
        """更新Grafana密码
        :param request: Request instance for UpdateGrafanaPassword.
        :type request: :class:`ksyun.client.kce.v20230306.models.UpdateGrafanaPasswordRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateGrafanaPassword", params, "application/x-www-form-urlencoded")
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

    def EnableGrafanaInternet(self, request):
        """开启/关闭Grafana公网访问
        :param request: Request instance for EnableGrafanaInternet.
        :type request: :class:`ksyun.client.kce.v20230306.models.EnableGrafanaInternetRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("EnableGrafanaInternet", params, "application/x-www-form-urlencoded")
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

    def DescribeGrafanaWhiteList(self, request):
        """查询可访问Grafana公网的IP白名单
        :param request: Request instance for DescribeGrafanaWhiteList.
        :type request: :class:`ksyun.client.kce.v20230306.models.DescribeGrafanaWhiteListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeGrafanaWhiteList", params, "application/x-www-form-urlencoded")
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

    def UpdateGrafanaWhiteList(self, request):
        """更新可访问Grafana公网的IP白名单
        :param request: Request instance for UpdateGrafanaWhiteList.
        :type request: :class:`ksyun.client.kce.v20230306.models.UpdateGrafanaWhiteListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateGrafanaWhiteList", params, "application/x-www-form-urlencoded")
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

    def AssociateCluster(self, request):
        """关联集群
        :param request: Request instance for AssociateCluster.
        :type request: :class:`ksyun.client.kce.v20230306.models.AssociateClusterRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AssociateCluster", params, "application/x-www-form-urlencoded")
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

    def DisassociateCluster(self, request):
        """解除关联集群
        :param request: Request instance for DisassociateCluster.
        :type request: :class:`ksyun.client.kce.v20230306.models.DisassociateClusterRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DisassociateCluster", params, "application/x-www-form-urlencoded")
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

    def DescribeAssociateClusterList(self, request):
        """查询关联集群列表
        :param request: Request instance for DescribeAssociateClusterList.
        :type request: :class:`ksyun.client.kce.v20230306.models.DescribeAssociateClusterListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeAssociateClusterList", params, "application/x-www-form-urlencoded")
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

    def DescribeMonitorList(self, request):
        """查询监控列表
        :param request: Request instance for DescribeMonitorList.
        :type request: :class:`ksyun.client.kce.v20230306.models.DescribeMonitorListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeMonitorList", params, "application/x-www-form-urlencoded")
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

    def DescribeMonitorCollectionConfig(self, request):
        """查询监控采集配置
        :param request: Request instance for DescribeMonitorCollectionConfig.
        :type request: :class:`ksyun.client.kce.v20230306.models.DescribeMonitorCollectionConfigRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeMonitorCollectionConfig", params, "application/x-www-form-urlencoded")
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

    def UpdateMonitorCollectionConfig(self, request):
        """更新监控采集配置
        :param request: Request instance for UpdateMonitorCollectionConfig.
        :type request: :class:`ksyun.client.kce.v20230306.models.UpdateMonitorCollectionConfigRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateMonitorCollectionConfig", params, "application/x-www-form-urlencoded")
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

    def DescribeMonitorMetricsList(self, request):
        """查询监控指标
        :param request: Request instance for DescribeMonitorMetricsList.
        :type request: :class:`ksyun.client.kce.v20230306.models.DescribeMonitorMetricsListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeMonitorMetricsList", params, "application/x-www-form-urlencoded")
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

    def DescribeTargetsList(self, request):
        """查询采集目标列表
        :param request: Request instance for DescribeTargetsList.
        :type request: :class:`ksyun.client.kce.v20230306.models.DescribeTargetsListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeTargetsList", params, "application/x-www-form-urlencoded")
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

    def DescribeAgentStatus(self, request):
        """查询agent状态
        :param request: Request instance for DescribeAgentStatus.
        :type request: :class:`ksyun.client.kce.v20230306.models.DescribeAgentStatusRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeAgentStatus", params, "application/x-www-form-urlencoded")
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

    def CreateMonitorCollectionConfig(self, request):
        """创建监控采集配置
        :param request: Request instance for CreateMonitorCollectionConfig.
        :type request: :class:`ksyun.client.kce.v20230306.models.CreateMonitorCollectionConfigRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateMonitorCollectionConfig", params, "application/x-www-form-urlencoded")
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

    def DeleteMonitorCollectionConfig(self, request):
        """删除监控采集配置
        :param request: Request instance for DeleteMonitorCollectionConfig.
        :type request: :class:`ksyun.client.kce.v20230306.models.DeleteMonitorCollectionConfigRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteMonitorCollectionConfig", params, "application/x-www-form-urlencoded")
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

    def EnableMetrics(self, request):
        """开启指标
        :param request: Request instance for EnableMetrics.
        :type request: :class:`ksyun.client.kce.v20230306.models.EnableMetricsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("EnableMetrics", params, "application/x-www-form-urlencoded")
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

    def DropMetrics(self, request):
        """废弃指标
        :param request: Request instance for DropMetrics.
        :type request: :class:`ksyun.client.kce.v20230306.models.DropMetricsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DropMetrics", params, "application/x-www-form-urlencoded")
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
