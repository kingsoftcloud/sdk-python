import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class CdnClient(AbstractClient):
    _apiVersion = '2021-12-01'
    _endpoint = 'cdn.api.ksyun.com'
    _service = 'cdn'
    def GetRefreshOrPreloadTask(self, request):
        """刷新预热进度查询接口迭代
        :param request: Request instance for GetRefreshOrPreloadTask.
        :type request: :class:`ksyun.client.cdn.v20211201.models.GetRefreshOrPreloadTaskRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetRefreshOrPreloadTask", params, "application/json")
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


