import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class KceClient(AbstractClient):
    _apiVersion = '2020-12-31'
    _endpoint = 'kce.api.ksyun.com'
    _service = 'kce'
    def CreateCluster(self, request):
        """创建集群新版
        :param request: Request instance for CreateCluster.
        :type request: :class:`ksyun.client.kce.v20201231.models.CreateClusterRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateCluster", params, "application/x-www-form-urlencoded")
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


