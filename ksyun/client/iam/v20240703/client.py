import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class IamClient(AbstractClient):
    _apiVersion = '2024-07-03'
    _endpoint = 'iam.api.ksyun.com'
    _service = 'iam'
    def ProjectsInfoByInstanceIds(self, request):
        """根据实例ID查询所属项目
        :param request: Request instance for ProjectsInfoByInstanceIds.
        :type request: :class:`ksyun.client.iam.v20240703.models.ProjectsInfoByInstanceIdsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ProjectsInfoByInstanceIds", params, "application/x-www-form-urlencoded")
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


