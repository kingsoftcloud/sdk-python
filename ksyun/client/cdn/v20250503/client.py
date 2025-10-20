import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class CdnClient(AbstractClient):
    _apiVersion = 'V3'
    _endpoint = 'cdn.api.ksyun.com'
    _service = 'cdn'
    def GetDomainLogs(self, request):
        """获取日志下载URL
        :param request: Request instance for GetDomainLogs.
        :type request: :class:`ksyun.client.cdn.v20250503.models.GetDomainLogsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetDomainLogs", params, "application/x-www-form-urlencoded")
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


    def GetClientRequestData(self, request):
        """访问数据查询接口
        :param request: Request instance for GetClientRequestData.
        :type request: :class:`ksyun.client.cdn.v20250503.models.GetClientRequestDataRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetClientRequestData", params, "application/x-www-form-urlencoded")
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


