import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class KingpayClient(AbstractClient):
    _apiVersion = 'V1'
    _endpoint = 'kingpay.api.ksyun.com'
    _service = 'kingpay'

    def QueryCashWalletAction(self, request):
        """获取用户账户余额
        :param request: Request instance for QueryCashWalletAction.
        :type request: :class:`ksyun.client.kingpay.v20240501.models.QueryCashWalletActionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("QueryCashWalletAction", params, "application/x-www-form-urlencoded")
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
