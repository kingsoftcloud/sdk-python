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


    def GetCdnDomains(self, request):
        """根据用户查询域名信息列表-V3版本
        :param request: Request instance for GetCdnDomains.
        :type request: :class:`ksyun.client.cdn.v20250503.models.GetCdnDomainsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetCdnDomains", params, "application/x-www-form-urlencoded")
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


    def DeleteCdnDomain(self, request):
        """删除加速域名
        :param request: Request instance for DeleteCdnDomain.
        :type request: :class:`ksyun.client.cdn.v20250503.models.DeleteCdnDomainRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteCdnDomain", params, "application/x-www-form-urlencoded")
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


    def GetCdnDomainBasicInfo(self, request):
        """获取指定加速域名配置的基本信息
        :param request: Request instance for GetCdnDomainBasicInfo.
        :type request: :class:`ksyun.client.cdn.v20250503.models.GetCdnDomainBasicInfoRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetCdnDomainBasicInfo", params, "application/x-www-form-urlencoded")
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


    def ModifyCdnDomainBasicInfo(self, request):
        """修改域名基本信息
        :param request: Request instance for ModifyCdnDomainBasicInfo.
        :type request: :class:`ksyun.client.cdn.v20250503.models.ModifyCdnDomainBasicInfoRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyCdnDomainBasicInfo", params, "application/x-www-form-urlencoded")
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


    def AddCdnDomain(self, request):
        """添加加速域名
        :param request: Request instance for AddCdnDomain.
        :type request: :class:`ksyun.client.cdn.v20250503.models.AddCdnDomainRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AddCdnDomain", params, "application/x-www-form-urlencoded")
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


    def GetDomainConfigs(self, request):
        """查询域名详细配置信息
        :param request: Request instance for GetDomainConfigs.
        :type request: :class:`ksyun.client.cdn.v20250503.models.GetDomainConfigsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetDomainConfigs", params, "application/x-www-form-urlencoded")
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


    def StartStopCdnDomain(self, request):
        """启用或停用域名根据域名id
        :param request: Request instance for StartStopCdnDomain.
        :type request: :class:`ksyun.client.cdn.v20250503.models.StartStopCdnDomainRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("StartStopCdnDomain", params, "application/x-www-form-urlencoded")
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


    def SetCacheRuleConfig(self, request):
        """设置缓存策略
        :param request: Request instance for SetCacheRuleConfig.
        :type request: :class:`ksyun.client.cdn.v20250503.models.SetCacheRuleConfigRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("SetCacheRuleConfig", params, "application/x-www-form-urlencoded")
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


    def SetBackOriginHostConfig(self, request):
        """设置回源host功能
        :param request: Request instance for SetBackOriginHostConfig.
        :type request: :class:`ksyun.client.cdn.v20250503.models.SetBackOriginHostConfigRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("SetBackOriginHostConfig", params, "application/x-www-form-urlencoded")
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


    def GetValidDomainList(self, request):
        """获取有效域名
        :param request: Request instance for GetValidDomainList.
        :type request: :class:`ksyun.client.cdn.v20250503.models.GetValidDomainListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetValidDomainList", params, "application/x-www-form-urlencoded")
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


    def GetDomainAuthContent(self, request):
        """获取域名归属校验内容
        :param request: Request instance for GetDomainAuthContent.
        :type request: :class:`ksyun.client.cdn.v20250503.models.GetDomainAuthContentRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetDomainAuthContent", params, "application/x-www-form-urlencoded")
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


    def SetVideoSeekConfig(self, request):
        """设置拖拽播放功能
        :param request: Request instance for SetVideoSeekConfig.
        :type request: :class:`ksyun.client.cdn.v20250503.models.SetVideoSeekConfigRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("SetVideoSeekConfig", params, "application/x-www-form-urlencoded")
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


    def SetPageCompressConfig(self, request):
        """设置智能压缩接口
        :param request: Request instance for SetPageCompressConfig.
        :type request: :class:`ksyun.client.cdn.v20250503.models.SetPageCompressConfigRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("SetPageCompressConfig", params, "application/x-www-form-urlencoded")
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


    def SetBrCompressConfig(self, request):
        """设置BR类型智能压缩接口
        :param request: Request instance for SetBrCompressConfig.
        :type request: :class:`ksyun.client.cdn.v20250503.models.SetBrCompressConfigRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("SetBrCompressConfig", params, "application/x-www-form-urlencoded")
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


    def SetIgnoreQueryStringConfig(self, request):
        """设置过滤参数功能
        :param request: Request instance for SetIgnoreQueryStringConfig.
        :type request: :class:`ksyun.client.cdn.v20250503.models.SetIgnoreQueryStringConfigRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("SetIgnoreQueryStringConfig", params, "application/x-www-form-urlencoded")
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


    def SetSetOriginAdvancedConfig(self, request):
        """设置高级回源策略
        :param request: Request instance for SetSetOriginAdvancedConfig.
        :type request: :class:`ksyun.client.cdn.v20250503.models.SetSetOriginAdvancedConfigRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("SetSetOriginAdvancedConfig", params, "application/x-www-form-urlencoded")
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


    def ValidateDomainOwner(self, request):
        """域名归属校验
        :param request: Request instance for ValidateDomainOwner.
        :type request: :class:`ksyun.client.cdn.v20250503.models.ValidateDomainOwnerRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ValidateDomainOwner", params, "application/x-www-form-urlencoded")
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


    def SetHttp2OptionConfig(self, request):
        """设置HTTP/2接口
        :param request: Request instance for SetHttp2OptionConfig.
        :type request: :class:`ksyun.client.cdn.v20250503.models.SetHttp2OptionConfigRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("SetHttp2OptionConfig", params, "application/x-www-form-urlencoded")
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


