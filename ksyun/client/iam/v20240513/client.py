import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class IamClient(AbstractClient):
    _apiVersion = '2024-05-13'
    _endpoint = 'iam.api.ksyun.com'
    _service = 'iam'
    def GetProjectInstanceListNew(self, request):
        """获取项目资源列表（新）
        :param request: Request instance for GetProjectInstanceListNew.
        :type request: :class:`ksyun.client.iam.v20240513.models.GetProjectInstanceListNewRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetProjectInstanceListNew", params, "application/json")
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


