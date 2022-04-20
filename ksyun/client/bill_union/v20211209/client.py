import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class Bill_unionClient(AbstractClient):
    _apiVersion = '2021-12-09'
    _endpoint = 'bill-union.api.ksyun.com'
    _service = 'bill-union'
    def DescribeCostBill(self, request):
        """获取预付费成本账单
        :param request: Request instance for DescribeCostBill.
        :type request: :class:`ksyun.client.bill_union.v20211209.models.DescribeCostBillRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DescribeCostBill", params)
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


