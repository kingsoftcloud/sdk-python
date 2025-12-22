import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class TerClient(AbstractClient):
    _apiVersion = '2024-04-15'
    _endpoint = 'ter.api.ksyun.com'
    _service = 'ter'
    def DescribeStackOutputs(self, request):
        """查询资源栈输出
        :param request: Request instance for DescribeStackOutputs.
        :type request: :class:`ksyun.client.ter.v20240415.models.DescribeStackOutputsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeStackOutputs", params, "application/x-www-form-urlencoded")
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


    def DescribeStackEvents(self, request):
        """查询资源栈事件
        :param request: Request instance for DescribeStackEvents.
        :type request: :class:`ksyun.client.ter.v20240415.models.DescribeStackEventsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeStackEvents", params, "application/x-www-form-urlencoded")
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


    def DeleteTemplate(self, request):
        """删除模板
        :param request: Request instance for DeleteTemplate.
        :type request: :class:`ksyun.client.ter.v20240415.models.DeleteTemplateRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteTemplate", params, "application/x-www-form-urlencoded")
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


    def DescribeTemplateVersions(self, request):
        """查询模板版本
        :param request: Request instance for DescribeTemplateVersions.
        :type request: :class:`ksyun.client.ter.v20240415.models.DescribeTemplateVersionsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeTemplateVersions", params, "application/x-www-form-urlencoded")
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


    def DescribeTemplates(self, request):
        """查询模板
        :param request: Request instance for DescribeTemplates.
        :type request: :class:`ksyun.client.ter.v20240415.models.DescribeTemplatesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeTemplates", params, "application/x-www-form-urlencoded")
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


