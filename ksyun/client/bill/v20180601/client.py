import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class BillClient(AbstractClient):
    _apiVersion = '2018-06-01'
    _endpoint = 'bill.api.ksyun.com'
    _service = 'bill'
    def GetMonthBill(self, request):
        """获取月账单
        :param request: Request instance for GetMonthBill.
        :type request: :class:`ksyun.client.bill.v20180601.models.GetMonthBillRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetMonthBill", params, "application/json")
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


    def GetPostpayDetailBill(self, request):
        """获取账单明细
        :param request: Request instance for GetPostpayDetailBill.
        :type request: :class:`ksyun.client.bill.v20180601.models.GetPostpayDetailBillRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetPostpayDetailBill", params, "application/json")
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


    def GetProductCode(self, request):
        """获取产品线映射
        :param request: Request instance for GetProductCode.
        :type request: :class:`ksyun.client.bill.v20180601.models.GetProductCodeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetProductCode", params, "application/json")
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


