import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class TradeClient(AbstractClient):
    _apiVersion = '2020-08-31'
    _endpoint = 'trade.api.ksyun.com'
    _service = 'trade'
    def SetRenewal(self, request):
        """批量设置实例续费策略
        :param request: Request instance for SetRenewal.
        :type request: :class:`ksyun.client.trade.v20200831.models.SetRenewalRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("SetRenewal", params, "application/x-www-form-urlencoded")
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


