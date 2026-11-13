import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class AicpClient(AbstractClient):
    _apiVersion = '2026-10-22'
    _endpoint = 'aicp.api.ksyun.com'
    _service = 'aicp'
    def GetModelIdleResource(self, request):
        """模型闲时资源查询
        :param request: Request instance for GetModelIdleResource.
        :type request: :class:`ksyun.client.aicp.v20261022.models.GetModelIdleResourceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetModelIdleResource", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(message=str(e))


