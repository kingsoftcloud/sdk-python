import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class KcsClient(AbstractClient):
    _apiVersion = '2024-07-01'
    _endpoint = 'kcs.api.ksyun.com'
    _service = 'kcs'
    def DescribeCacheByRole(self, request):
        """缓存服务查询角色节点列表
        :param request: Request instance for DescribeCacheByRole.
        :type request: :class:`ksyun.client.kcs.v20240701.models.DescribeCacheByRoleRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeCacheByRole", params, "application/x-www-form-urlencoded")
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


