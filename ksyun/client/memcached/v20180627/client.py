import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class MemcachedClient(AbstractClient):
    _apiVersion = '2018-06-27'
    _endpoint = 'memcached.api.ksyun.com'
    _service = 'memcached'
    def CreateCacheCluster(self, request):
        """创建实例。
        :param request: Request instance for CreateCacheCluster.
        :type request: :class:`ksyun.client.memcached.v20180627.models.CreateCacheClusterRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateCacheCluster", params, "application/x-www-form-urlencoded")
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


    def DeleteCacheCluster(self, request):
        """删除实例。
        :param request: Request instance for DeleteCacheCluster.
        :type request: :class:`ksyun.client.memcached.v20180627.models.DeleteCacheClusterRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteCacheCluster", params, "application/x-www-form-urlencoded")
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


    def ResizeCacheCluster(self, request):
        """更配缓存服务
        :param request: Request instance for ResizeCacheCluster.
        :type request: :class:`ksyun.client.memcached.v20180627.models.ResizeCacheClusterRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ResizeCacheCluster", params, "application/x-www-form-urlencoded")
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


    def DescribeCacheClusters(self, request):
        """查询实例列表
        :param request: Request instance for DescribeCacheClusters.
        :type request: :class:`ksyun.client.memcached.v20180627.models.DescribeCacheClustersRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeCacheClusters", params, "application/x-www-form-urlencoded")
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


    def DescribeCacheCluster(self, request):
        """查询实例详情
        :param request: Request instance for DescribeCacheCluster.
        :type request: :class:`ksyun.client.memcached.v20180627.models.DescribeCacheClusterRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeCacheCluster", params, "application/x-www-form-urlencoded")
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


    def FlushCacheCluster(self, request):
        """清空实例缓存
        :param request: Request instance for FlushCacheCluster.
        :type request: :class:`ksyun.client.memcached.v20180627.models.FlushCacheClusterRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("FlushCacheCluster", params, "application/x-www-form-urlencoded")
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


    def RenameCacheCluster(self, request):
        """修改实例名称
        :param request: Request instance for RenameCacheCluster.
        :type request: :class:`ksyun.client.memcached.v20180627.models.RenameCacheClusterRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RenameCacheCluster", params, "application/x-www-form-urlencoded")
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


    def UpdatePassword(self, request):
        """重置实例密码
        :param request: Request instance for UpdatePassword.
        :type request: :class:`ksyun.client.memcached.v20180627.models.UpdatePasswordRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdatePassword", params, "application/x-www-form-urlencoded")
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


    def DescribeCacheSecurityRules(self, request):
        """查询安全组规则
        :param request: Request instance for DescribeCacheSecurityRules.
        :type request: :class:`ksyun.client.memcached.v20180627.models.DescribeCacheSecurityRulesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeCacheSecurityRules", params, "application/x-www-form-urlencoded")
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


    def DeleteCacheSecurityRule(self, request):
        """删除安全组规则
        :param request: Request instance for DeleteCacheSecurityRule.
        :type request: :class:`ksyun.client.memcached.v20180627.models.DeleteCacheSecurityRuleRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteCacheSecurityRule", params, "application/x-www-form-urlencoded")
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


    def SetCacheSecurityRules(self, request):
        """设置安全组规则
        :param request: Request instance for SetCacheSecurityRules.
        :type request: :class:`ksyun.client.memcached.v20180627.models.SetCacheSecurityRulesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("SetCacheSecurityRules", params, "application/x-www-form-urlencoded")
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
        """查询地域列表
        :param request: Request instance for DescribeRegions.
        :type request: :class:`ksyun.client.memcached.v20180627.models.DescribeRegionsRequest`
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


    def DescribeAvailabilityZones(self, request):
        """查询可用区列表
        :param request: Request instance for DescribeAvailabilityZones.
        :type request: :class:`ksyun.client.memcached.v20180627.models.DescribeAvailabilityZonesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeAvailabilityZones", params, "application/x-www-form-urlencoded")
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


