import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class KsccClient(AbstractClient):
    _apiVersion = 'V1'
    _endpoint = 'kscc.api.ksyun.com'
    _service = 'kscc'
    def UpdateUserQuota(self, request):
        """更新用户月度配额，如不存在则新增现在，如果存在则更新。当quotaAmount为null代表不限制。
        :param request: Request instance for UpdateUserQuota.
        :type request: :class:`ksyun.client.kscc.v1.models.UpdateUserQuotaRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateUserQuota", params, "application/json")
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
                raise KsyunSDKException(message=str(e))


    def DescribeUserCostSummary(self, request):
        """用户本月配额数据统计
        :param request: Request instance for DescribeUserCostSummary.
        :type request: :class:`ksyun.client.kscc.v1.models.DescribeUserCostSummaryRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeUserCostSummary", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(message=str(e))


