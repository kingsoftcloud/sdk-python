import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class KciClient(AbstractClient):
    _apiVersion = '2020-07-02'
    _endpoint = 'kci.api.ksyun.com'
    _service = 'kci'

    def CreateContainerGroup(self, request):
        """创建容器实例组
        :param request: Request instance for CreateContainerGroup.
        :type request: :class:`ksyun.client.kci.v20200702.models.CreateContainerGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateContainerGroup", params, "application/x-www-form-urlencoded")
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

    def DescribeContainerGroup(self, request):
        """查询容器实例组
        :param request: Request instance for DescribeContainerGroup.
        :type request: :class:`ksyun.client.kci.v20200702.models.DescribeContainerGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeContainerGroup", params, "application/x-www-form-urlencoded")
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

    def DescribeContainerGroupList(self, request):
        """用于控制台查询容器实例组列表
        :param request: Request instance for DescribeContainerGroupList.
        :type request: :class:`ksyun.client.kci.v20200702.models.DescribeContainerGroupListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeContainerGroupList", params, "application/x-www-form-urlencoded")
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

    def DeleteContainerGroup(self, request):
        """删除容器实例组
        :param request: Request instance for DeleteContainerGroup.
        :type request: :class:`ksyun.client.kci.v20200702.models.DeleteContainerGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteContainerGroup", params, "application/x-www-form-urlencoded")
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

    def DescribeContainerLog(self, request):
        """查询容器实例组日志
        :param request: Request instance for DescribeContainerLog.
        :type request: :class:`ksyun.client.kci.v20200702.models.DescribeContainerLogRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeContainerLog", params, "application/x-www-form-urlencoded")
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

    def DescribeRegions(self, request):
        """查询有权限创建容器实例的机房列表
        :param request: Request instance for DescribeRegions.
        :type request: :class:`ksyun.client.kci.v20200702.models.DescribeRegionsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeRegions", params, "application/x-www-form-urlencoded")
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

    def ExecContainerCommand(self, request):
        """生成执行容器命令的webSocketUri
        :param request: Request instance for ExecContainerCommand.
        :type request: :class:`ksyun.client.kci.v20200702.models.ExecContainerCommandRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ExecContainerCommand", params, "application/x-www-form-urlencoded")
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

    def DescribeContainerGroupCount(self, request):
        """查询容器实例数量
        :param request: Request instance for DescribeContainerGroupCount.
        :type request: :class:`ksyun.client.kci.v20200702.models.DescribeContainerGroupCountRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeContainerGroupCount", params, "application/x-www-form-urlencoded")
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

    def DescribeContainerGroupEvents(self, request):
        """查询容器实例事件信息
        :param request: Request instance for DescribeContainerGroupEvents.
        :type request: :class:`ksyun.client.kci.v20200702.models.DescribeContainerGroupEventsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeContainerGroupEvents", params, "application/x-www-form-urlencoded")
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

    def DescribeKciPackages(self, request):
        """查询容器实例在各机房可用区支持的标准规格大小
        :param request: Request instance for DescribeKciPackages.
        :type request: :class:`ksyun.client.kci.v20200702.models.DescribeKciPackagesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeKciPackages", params, "application/x-www-form-urlencoded")
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

    def CreateImageCache(self, request):
        """创建容器实例镜像缓存
        :param request: Request instance for CreateImageCache.
        :type request: :class:`ksyun.client.kci.v20200702.models.CreateImageCacheRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateImageCache", params, "application/x-www-form-urlencoded")
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

    def DeleteImageCache(self, request):
        """删除容器实例镜像缓存
        :param request: Request instance for DeleteImageCache.
        :type request: :class:`ksyun.client.kci.v20200702.models.DeleteImageCacheRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteImageCache", params, "application/x-www-form-urlencoded")
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

    def DescribeImageCache(self, request):
        """查询容器实例镜像缓存
        :param request: Request instance for DescribeImageCache.
        :type request: :class:`ksyun.client.kci.v20200702.models.DescribeImageCacheRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeImageCache", params, "application/x-www-form-urlencoded")
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

    def MatchImageCache(self, request):
        """匹配容器实例镜像缓存
        :param request: Request instance for MatchImageCache.
        :type request: :class:`ksyun.client.kci.v20200702.models.MatchImageCacheRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("MatchImageCache", params, "application/x-www-form-urlencoded")
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

    def DescribeImageCacheEvent(self, request):
        """查询镜像缓存制作事件
        :param request: Request instance for DescribeImageCacheEvent.
        :type request: :class:`ksyun.client.kci.v20200702.models.DescribeImageCacheEventRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeImageCacheEvent", params, "application/x-www-form-urlencoded")
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
