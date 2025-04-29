import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class KlsClient(AbstractClient):
    _apiVersion = '2017-01-01'
    _endpoint = 'kls.api.ksyun.com'
    _service = 'kls'

    def ListStreamDurations(self, request):
        """查询主播流时长接口
        :param request: Request instance for ListStreamDurations.
        :type request: :class:`ksyun.client.kls.v20170101.models.ListStreamDurationsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListStreamDurations", params, "application/json")
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

    def ListHistoryPubStreamsErrInfo(self, request):
        """查询流历史流错误信息
        :param request: Request instance for ListHistoryPubStreamsErrInfo.
        :type request: :class:`ksyun.client.kls.v20170101.models.ListHistoryPubStreamsErrInfoRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListHistoryPubStreamsErrInfo", params, "application/json")
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

    def ListHistoryPubStreamsInfo(self, request):
        """查询流历史信息接口
        :param request: Request instance for ListHistoryPubStreamsInfo.
        :type request: :class:`ksyun.client.kls.v20170101.models.ListHistoryPubStreamsInfoRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListHistoryPubStreamsInfo", params, "application/json")
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

    def ForbidStream(self, request):
        """禁止单路直播流推送
        :param request: Request instance for ForbidStream.
        :type request: :class:`ksyun.client.kls.v20170101.models.ForbidStreamRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ForbidStream", params, "application/json")
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

    def ResumeStream(self, request):
        """恢复单路直播流推送
        :param request: Request instance for ResumeStream.
        :type request: :class:`ksyun.client.kls.v20170101.models.ResumeStreamRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ResumeStream", params, "application/json")
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

    def GetBlacklist(self, request):
        """查询黑名单列表
        :param request: Request instance for GetBlacklist.
        :type request: :class:`ksyun.client.kls.v20170101.models.GetBlacklistRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetBlacklist", params, "application/json")
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

    def CheckBlacklist(self, request):
        """检查流是否在黑名单内
        :param request: Request instance for CheckBlacklist.
        :type request: :class:`ksyun.client.kls.v20170101.models.CheckBlacklistRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CheckBlacklist", params, "application/json")
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

    def ListRealtimeStreamsInfo(self, request):
        """获取流实时信息
        :param request: Request instance for ListRealtimeStreamsInfo.
        :type request: :class:`ksyun.client.kls.v20170101.models.ListRealtimeStreamsInfoRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListRealtimeStreamsInfo", params, "application/json")
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
