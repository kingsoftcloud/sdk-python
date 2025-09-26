import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class CdnClient(AbstractClient):
    _apiVersion = '2016-09-01'
    _endpoint = 'cdn.api.ksyun.com'
    _service = 'cdn'
    def GetDomainLogs(self, request):
        """获取日志下载URL
        :param request: Request instance for GetDomainLogs.
        :type request: :class:`ksyun.client.cdn.v20160901.models.GetDomainLogsRequest`
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


    def GetRefreshOrPreloadTask(self, request):
        """刷新预热进度查询接口
        :param request: Request instance for GetRefreshOrPreloadTask.
        :type request: :class:`ksyun.client.cdn.v20160901.models.GetRefreshOrPreloadTaskRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetRefreshOrPreloadTask", params, "application/json")
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


    def RefreshCaches(self, request):
        """刷新缓存接口
        :param request: Request instance for RefreshCaches.
        :type request: :class:`ksyun.client.cdn.v20160901.models.RefreshCachesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RefreshCaches", params, "application/json")
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


