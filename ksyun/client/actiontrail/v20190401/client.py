import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class ActiontrailClient(AbstractClient):
    _apiVersion = '2019-04-01'
    _endpoint = 'actiontrail.api.ksyun.com'
    _service = 'actiontrail'

    def ListOperateLogs(self, request):
        """获取历史事件记录
        :param request: Request instance for ListOperateLogs.
        :type request: :class:`ksyun.client.actiontrail.v20190401.models.ListOperateLogsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListOperateLogs", params, "application/json")
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
