import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class Tagv2Client(AbstractClient):
    _apiVersion = '2020-09-01'
    _endpoint = 'tagv2.api.ksyun.com'
    _service = 'tagv2'

    def CreateTag(self, request):
        """创建标签
        :param request: Request instance for CreateTag.
        :type request: :class:`ksyun.client.tagv2.v20200901.models.CreateTagRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateTag", params, "application/x-www-form-urlencoded")
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

    def DeleteTag(self, request):
        """删除标签
        :param request: Request instance for DeleteTag.
        :type request: :class:`ksyun.client.tagv2.v20200901.models.DeleteTagRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteTag", params, "application/x-www-form-urlencoded")
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

    def ListTags(self, request):
        """获取标签列表
        :param request: Request instance for ListTags.
        :type request: :class:`ksyun.client.tagv2.v20200901.models.ListTagsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListTags", params, "application/x-www-form-urlencoded")
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

    def ListTagKeys(self, request):
        """获取标签键列表
        :param request: Request instance for ListTagKeys.
        :type request: :class:`ksyun.client.tagv2.v20200901.models.ListTagKeysRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListTagKeys", params, "application/x-www-form-urlencoded")
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

    def ListTagValues(self, request):
        """获取标签值列表
        :param request: Request instance for ListTagValues.
        :type request: :class:`ksyun.client.tagv2.v20200901.models.ListTagValuesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListTagValues", params, "application/x-www-form-urlencoded")
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

    def ListResources(self, request):
        """获取用户资源列表
        :param request: Request instance for ListResources.
        :type request: :class:`ksyun.client.tagv2.v20200901.models.ListResourcesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListResources", params, "application/x-www-form-urlencoded")
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

    def ListTagsByResourceIds(self, request):
        """根据资源ID获取资源标签
        :param request: Request instance for ListTagsByResourceIds.
        :type request: :class:`ksyun.client.tagv2.v20200901.models.ListTagsByResourceIdsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListTagsByResourceIds", params, "application/x-www-form-urlencoded")
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

    def ReplaceResourcesTags(self, request):
        """批量替换资源的全部标签
        :param request: Request instance for ReplaceResourcesTags.
        :type request: :class:`ksyun.client.tagv2.v20200901.models.ReplaceResourcesTagsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ReplaceResourcesTags", params, "application/x-www-form-urlencoded")
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

    def DetachResourceTags(self, request):
        """解绑资源标签
        :param request: Request instance for DetachResourceTags.
        :type request: :class:`ksyun.client.tagv2.v20200901.models.DetachResourceTagsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DetachResourceTags", params, "application/x-www-form-urlencoded")
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
