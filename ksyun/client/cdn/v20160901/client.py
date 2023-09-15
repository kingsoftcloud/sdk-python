import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class CdnClient(AbstractClient):
    _apiVersion = '2016-09-01'
    _endpoint = 'cdn.api.ksyun.com'
    _service = 'cdn'
    def GetDomainPidDimensionUsageData(self, request):
        """查询pid维度-计费用量数据
        :param request: Request instance for GetDomainPidDimensionUsageData.
        :type request: :class:`ksyun.client.cdn.v20160901.models.GetDomainPidDimensionUsageDataRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetDomainPidDimensionUsageData", params, "application/x-www-form-urlencoded")
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


