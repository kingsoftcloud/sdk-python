import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class Bill_unionClient(AbstractClient):
    _apiVersion = '2022-12-22'
    _endpoint = 'bill-union.api.ksyun.com'
    _service = 'bill-union'
    def QueryInstanceConsume(self, request):
        """查询实例按日汇总账单
        :param request: Request instance for QueryInstanceConsume.
        :type request: :class:`ksyun.client.bill_union.v20221222.models.QueryInstanceConsumeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("QueryInstanceConsume", params, "application/json")
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


    def QueryProjectConsume(self, request):
        """项目制按日汇总账单
        :param request: Request instance for QueryProjectConsume.
        :type request: :class:`ksyun.client.bill_union.v20221222.models.QueryProjectConsumeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("QueryProjectConsume", params, "application/json")
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


    def QueryProductConsume(self, request):
        """产品线按日汇总账单
        :param request: Request instance for QueryProductConsume.
        :type request: :class:`ksyun.client.bill_union.v20221222.models.QueryProductConsumeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("QueryProductConsume", params, "application/json")
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


    def QueryFinanceUnitConsume(self, request):
        """财务单元按日汇总账单
        :param request: Request instance for QueryFinanceUnitConsume.
        :type request: :class:`ksyun.client.bill_union.v20221222.models.QueryFinanceUnitConsumeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("QueryFinanceUnitConsume", params, "application/json")
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


    def QueryFinanceUnitConsumeOfMonth(self, request):
        """财务单元按月汇总账单
        :param request: Request instance for QueryFinanceUnitConsumeOfMonth.
        :type request: :class:`ksyun.client.bill_union.v20221222.models.QueryFinanceUnitConsumeOfMonthRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("QueryFinanceUnitConsumeOfMonth", params, "application/json")
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


    def QueryUserConsume(self, request):
        """计费类别按日汇总账单
        :param request: Request instance for QueryUserConsume.
        :type request: :class:`ksyun.client.bill_union.v20221222.models.QueryUserConsumeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("QueryUserConsume", params, "application/json")
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


