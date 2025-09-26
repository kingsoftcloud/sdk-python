import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class TradeClient(AbstractClient):
    _apiVersion = '2025-03-21'
    _endpoint = 'trade.api.ksyun.com'
    _service = 'trade'

    def QueryUnPayOrders(self, request):
        """查询主账号待支付的订单列表
        :param request: Request instance for QueryUnPayOrders.
        :type request: :class:`ksyun.client.trade.v20250321.models.QueryUnPayOrdersRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("QueryUnPayOrders", params, "application/x-www-form-urlencoded")
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

    def QueryOrderInfo(self, request):
        """根据订单ID查询订单信息
        :param request: Request instance for QueryOrderInfo.
        :type request: :class:`ksyun.client.trade.v20250321.models.QueryOrderInfoRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("QueryOrderInfo", params, "application/x-www-form-urlencoded")
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

    def CancelOrder(self, request):
        """取消还未支付的订单，取消后不能再支付
        :param request: Request instance for CancelOrder.
        :type request: :class:`ksyun.client.trade.v20250321.models.CancelOrderRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CancelOrder", params, "application/x-www-form-urlencoded")
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

    def LaunchPayOrder(self, request):
        """通过订单ID支付订单，会自动扣余额的金额
        :param request: Request instance for LaunchPayOrder.
        :type request: :class:`ksyun.client.trade.v20250321.models.LaunchPayOrderRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("LaunchPayOrder", params, "application/x-www-form-urlencoded")
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
