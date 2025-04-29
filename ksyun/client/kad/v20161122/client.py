import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class KadClient(AbstractClient):
    _apiVersion = '2016-11-22'
    _endpoint = 'kad.api.ksyun.com'
    _service = 'kad'

    def CreateForwardConf(self, request):
        """创建四层转发配置
        :param request: Request instance for CreateForwardConf.
        :type request: :class:`ksyun.client.kad.v20161122.models.CreateForwardConfRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateForwardConf", params, "application/x-www-form-urlencoded")
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

    def DeleteForwardConf(self, request):
        """删除四层转发配置
        :param request: Request instance for DeleteForwardConf.
        :type request: :class:`ksyun.client.kad.v20161122.models.DeleteForwardConfRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteForwardConf", params, "application/x-www-form-urlencoded")
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

    def DescribeForwardConf(self, request):
        """描述四层转发记录
        :param request: Request instance for DescribeForwardConf.
        :type request: :class:`ksyun.client.kad.v20161122.models.DescribeForwardConfRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeForwardConf", params, "application/json")
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

    def CreateForwardSource(self, request):
        """创建四层转发回源配置
        :param request: Request instance for CreateForwardSource.
        :type request: :class:`ksyun.client.kad.v20161122.models.CreateForwardSourceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateForwardSource", params, "application/x-www-form-urlencoded")
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

    def DeleteForwardSource(self, request):
        """删除四层转发回源配置
        :param request: Request instance for DeleteForwardSource.
        :type request: :class:`ksyun.client.kad.v20161122.models.DeleteForwardSourceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteForwardSource", params, "application/x-www-form-urlencoded")
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

    def DescribeForwardSource(self, request):
        """描述四层转发回源配置
        :param request: Request instance for DescribeForwardSource.
        :type request: :class:`ksyun.client.kad.v20161122.models.DescribeForwardSourceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeForwardSource", params, "application/json")
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
