import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class KmafClient(AbstractClient):
    _apiVersion = '2026-01-30'
    _endpoint = 'kmaf.api.ksyun.com'
    _service = 'kmaf'
    def QueryAnswer(self, request):
        """获取安全代答内容
        :param request: Request instance for QueryAnswer.
        :type request: :class:`ksyun.client.kmaf.v20260130.models.QueryAnswerRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("QueryAnswer", params, "application/json")
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


    def CheckModerate(self, request):
        """检测模型输入和输出内容
        :param request: Request instance for CheckModerate.
        :type request: :class:`ksyun.client.kmaf.v20260130.models.CheckModerateRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CheckModerate", params, "application/json")
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


