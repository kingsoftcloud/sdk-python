import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class KcsClient(AbstractClient):
    _apiVersion = '2017-04-01'
    _endpoint = 'kcs.api.ksyun.com'
    _service = 'kcs'
    def DescribeCacheReadonlyNode(self, request):
        """获取只读实例列表
        :param request: Request instance for DescribeCacheReadonlyNode.
        :type request: :class:`ksyun.client.kcs.v20170401.models.DescribeCacheReadonlyNodeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeCacheReadonlyNode", params, "application/json")
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


    def AddCacheSlaveNode(self, request):
        """AddCacheSlaveNode
        :param request: Request instance for AddCacheSlaveNode.
        :type request: :class:`ksyun.client.kcs.v20170401.models.AddCacheSlaveNodeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AddCacheSlaveNode", params, "application/json")
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


    def DeleteCacheSlaveNode(self, request):
        """删除只读实例
        :param request: Request instance for DeleteCacheSlaveNode.
        :type request: :class:`ksyun.client.kcs.v20170401.models.DeleteCacheSlaveNodeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteCacheSlaveNode", params, "application/json")
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


