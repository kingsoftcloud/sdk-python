import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class KcsClient(AbstractClient):
    _apiVersion = '2017-04-01'
    _endpoint = 'kcs.api.ksyun.com'
    _service = 'kcs'
    def DeleteCacheSlaveNode(self, request):
        """社区版主从实例删除只读实例
        :param request: Request instance for DeleteCacheSlaveNode.
        :type request: :class:`ksyun.client.kcs.v20170401.models.DeleteCacheSlaveNodeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteCacheSlaveNode", params, "application/x-www-form-urlencoded")
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


