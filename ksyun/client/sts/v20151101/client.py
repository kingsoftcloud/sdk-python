import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class StsClient(AbstractClient):
    _apiVersion = '2015-11-01'
    _endpoint = 'sts.api.ksyun.com'
    _service = 'sts'

    def AssumeRole(self, request):
        """获取角色的一个临时安全令牌
        :param request: Request instance for AssumeRole.
        :type request: :class:`ksyun.client.sts.v20151101.models.AssumeRoleRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AssumeRole", params, "application/x-www-form-urlencoded")
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
