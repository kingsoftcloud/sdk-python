import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class KceClient(AbstractClient):
    _apiVersion = '2023-01-01'
    _endpoint = 'kce.api.ksyun.com'
    _service = 'kce'

    def DescribeEventLogs(self, request):
        """查询集群事件日志
        :param request: Request instance for DescribeEventLogs.
        :type request: :class:`ksyun.client.kce.v20230101.models.DescribeEventLogsRequest`
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

    def CreateAddonInstance(self, request):
        """创建插件实例
        :param request: Request instance for CreateAddonInstance.
        :type request: :class:`ksyun.client.kce.v20230101.models.CreateAddonInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateAddonInstance", params, "application/x-www-form-urlencoded")
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

    def DeleteAddonInstance(self, request):
        """删除插件实例
        :param request: Request instance for DeleteAddonInstance.
        :type request: :class:`ksyun.client.kce.v20230101.models.DeleteAddonInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteAddonInstance", params, "application/x-www-form-urlencoded")
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

    def DescribeAddonInstances(self, request):
        """查询插件实例
        :param request: Request instance for DescribeAddonInstances.
        :type request: :class:`ksyun.client.kce.v20230101.models.DescribeAddonInstancesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeAddonInstances", params, "application/x-www-form-urlencoded")
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

    def DescribeAddonList(self, request):
        """查询插件列表
        :param request: Request instance for DescribeAddonList.
        :type request: :class:`ksyun.client.kce.v20230101.models.DescribeAddonListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeAddonList", params, "application/x-www-form-urlencoded")
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
        :type request: :class:`ksyun.client.kce.v20230101.models.DescribeComponentParamsRequest`
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

    def DescribeNetwork(self, request):
        """查询集群网络
        :param request: Request instance for DescribeNetwork.
        :type request: :class:`ksyun.client.kce.v20230101.models.DescribeNetworkRequest`
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

    def DescribeNodeComponents(self, request):
        """查询节点组件列表
        :param request: Request instance for DescribeNodeComponents.
        :type request: :class:`ksyun.client.kce.v20230101.models.DescribeNodeComponentsRequest`
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

    def DescribeComponentList(self, request):
        """查询可安装的组件列表
        :param request: Request instance for DescribeComponentList.
        :type request: :class:`ksyun.client.kce.v20230101.models.DescribeComponentListRequest`
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
