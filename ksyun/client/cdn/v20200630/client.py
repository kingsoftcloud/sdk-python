import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class CdnClient(AbstractClient):
    _apiVersion = '2020-06-30'
    _endpoint = 'cdn.api.ksyun.com'
    _service = 'cdn'
    def GetClientRequestData(self, request):
        """访问数据查询接口
        :param request: Request instance for GetClientRequestData.
        :type request: :class:`ksyun.client.cdn.v20200630.models.GetClientRequestDataRequest`
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


    def GetServerData(self, request):
        """服务数据查询接口
        :param request: Request instance for GetServerData.
        :type request: :class:`ksyun.client.cdn.v20200630.models.GetServerDataRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetServerData", params, "application/x-www-form-urlencoded")
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


    def GetDomainRankingListData(self, request):
        """查询域名排行V2
        :param request: Request instance for GetDomainRankingListData.
        :type request: :class:`ksyun.client.cdn.v20200630.models.GetDomainRankingListDataRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetDomainRankingListData", params, "application/x-www-form-urlencoded")
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


    def GetAreaIspData(self, request):
        """查询地区、运营商V2
        :param request: Request instance for GetAreaIspData.
        :type request: :class:`ksyun.client.cdn.v20200630.models.GetAreaIspDataRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetAreaIspData", params, "application/x-www-form-urlencoded")
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


    def GetTopReferData(self, request):
        """查询热门refererV2
        :param request: Request instance for GetTopReferData.
        :type request: :class:`ksyun.client.cdn.v20200630.models.GetTopReferDataRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetTopReferData", params, "application/x-www-form-urlencoded")
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


    def GetTopUrlData(self, request):
        """查询热门URLV2
        :param request: Request instance for GetTopUrlData.
        :type request: :class:`ksyun.client.cdn.v20200630.models.GetTopUrlDataRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetTopUrlData", params, "application/x-www-form-urlencoded")
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


    def GetRealTimeHitRateData(self, request):
        """命中率查询接口
        :param request: Request instance for GetRealTimeHitRateData.
        :type request: :class:`ksyun.client.cdn.v20200630.models.GetRealTimeHitRateDataRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetRealTimeHitRateData", params, "application/x-www-form-urlencoded")
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


    def GetReqHitRateData(self, request):
        """请求命中率详情查询接口
        :param request: Request instance for GetReqHitRateData.
        :type request: :class:`ksyun.client.cdn.v20200630.models.GetReqHitRateDataRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetReqHitRateData", params, "application/x-www-form-urlencoded")
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


    def GetFlowHitRateData(self, request):
        """流量命中率详情查询接口
        :param request: Request instance for GetFlowHitRateData.
        :type request: :class:`ksyun.client.cdn.v20200630.models.GetFlowHitRateDataRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetFlowHitRateData", params, "application/x-www-form-urlencoded")
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


    def GetDomainRequestPeriodRatioData(self, request):
        """数据对比V2
        :param request: Request instance for GetDomainRequestPeriodRatioData.
        :type request: :class:`ksyun.client.cdn.v20200630.models.GetDomainRequestPeriodRatioDataRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetDomainRequestPeriodRatioData", params, "application/x-www-form-urlencoded")
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


    def GetUvData(self, request):
        """查询独立IP数V2
        :param request: Request instance for GetUvData.
        :type request: :class:`ksyun.client.cdn.v20200630.models.GetUvDataRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetUvData", params, "application/x-www-form-urlencoded")
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


    def GetTopIpData(self, request):
        """查询TopIPV2
        :param request: Request instance for GetTopIpData.
        :type request: :class:`ksyun.client.cdn.v20200630.models.GetTopIpDataRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetTopIpData", params, "application/x-www-form-urlencoded")
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


    def GetSrcDomainHttpCodeDetailedData(self, request):
        """回源状态码详情查询接口
        :param request: Request instance for GetSrcDomainHttpCodeDetailedData.
        :type request: :class:`ksyun.client.cdn.v20200630.models.GetSrcDomainHttpCodeDetailedDataRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetSrcDomainHttpCodeDetailedData", params, "application/x-www-form-urlencoded")
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


    def GetSrcDomainHttpCodeData(self, request):
        """回源状态码查询接口
        :param request: Request instance for GetSrcDomainHttpCodeData.
        :type request: :class:`ksyun.client.cdn.v20200630.models.GetSrcDomainHttpCodeDataRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetSrcDomainHttpCodeData", params, "application/x-www-form-urlencoded")
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


    def GetDomainHttpCodeDetailedData(self, request):
        """服务状态码详情查询接口
        :param request: Request instance for GetDomainHttpCodeDetailedData.
        :type request: :class:`ksyun.client.cdn.v20200630.models.GetDomainHttpCodeDetailedDataRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetDomainHttpCodeDetailedData", params, "application/x-www-form-urlencoded")
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


    def GetDomainHttpCodeData(self, request):
        """服务状态码占比查询接口
        :param request: Request instance for GetDomainHttpCodeData.
        :type request: :class:`ksyun.client.cdn.v20200630.models.GetDomainHttpCodeDataRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetDomainHttpCodeData", params, "application/x-www-form-urlencoded")
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


    def GetEntryRateData(self, request):
        """ECN进入率查询接口
        :param request: Request instance for GetEntryRateData.
        :type request: :class:`ksyun.client.cdn.v20200630.models.GetEntryRateDataRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetEntryRateData", params, "application/json")
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


