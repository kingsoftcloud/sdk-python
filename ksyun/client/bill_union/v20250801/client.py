import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class Bill_unionClient(AbstractClient):
    _apiVersion = '2025-08-01'
    _endpoint = 'bill-union.api.ksyun.com'
    _service = 'bill-union'
    def QueryItemBills(self, request):
        """查询计费项账单
        :param request: Request instance for QueryItemBills.
        :type request: :class:`ksyun.client.bill_union.v20250801.models.QueryItemBillsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("QueryItemBills", params, "application/json")
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


    def QueryProductTypes(self, request):
        """产品子类型查询
        :param request: Request instance for QueryProductTypes.
        :type request: :class:`ksyun.client.bill_union.v20250801.models.QueryProductTypesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("QueryProductTypes", params, "application/x-www-form-urlencoded")
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


