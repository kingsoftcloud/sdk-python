import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class BillClient(AbstractClient):
    _apiVersion = '2022-06-01'
    _endpoint = 'bill.api.ksyun.com'
    _service = 'bill'

    def GetMonthConsume(self, request):
        """获取日耗月账单
        :param request: Request instance for GetMonthConsume.
        :type request: :class:`ksyun.client.bill.v20220601.models.GetMonthConsumeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetMonthConsume", params, "application/json")
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

    def GetPostpayDetailConsume(self, request):
        """获取日耗账单明细
        :param request: Request instance for GetPostpayDetailConsume.
        :type request: :class:`ksyun.client.bill.v20220601.models.GetPostpayDetailConsumeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetPostpayDetailConsume", params, "application/json")
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
