import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class BwsClient(AbstractClient):
    _apiVersion = '2016-03-04'
    _endpoint = 'bws.api.ksyun.com'
    _service = 'bws'

    def CreateBandWidthShare(self, request):
        """创建共享带宽
        :param request: Request instance for CreateBandWidthShare.
        :type request: :class:`ksyun.client.bws.v20160304.models.CreateBandWidthShareRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateBandWidthShare", params, "application/x-www-form-urlencoded")
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

    def DescribeBandWidthShares(self, request):
        """描述共享带宽
        :param request: Request instance for DescribeBandWidthShares.
        :type request: :class:`ksyun.client.bws.v20160304.models.DescribeBandWidthSharesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeBandWidthShares", params, "application/x-www-form-urlencoded")
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

    def AssociateBandWidthShare(self, request):
        """绑定共享带宽
        :param request: Request instance for AssociateBandWidthShare.
        :type request: :class:`ksyun.client.bws.v20160304.models.AssociateBandWidthShareRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AssociateBandWidthShare", params, "application/x-www-form-urlencoded")
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

    def DisassociateBandWidthShare(self, request):
        """解绑共享带宽
        :param request: Request instance for DisassociateBandWidthShare.
        :type request: :class:`ksyun.client.bws.v20160304.models.DisassociateBandWidthShareRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DisassociateBandWidthShare", params, "application/x-www-form-urlencoded")
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

    def ModifyBandWidthShare(self, request):
        """更新共享带宽配置
        :param request: Request instance for ModifyBandWidthShare.
        :type request: :class:`ksyun.client.bws.v20160304.models.ModifyBandWidthShareRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyBandWidthShare", params, "application/x-www-form-urlencoded")
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

    def DeleteBandWidthShare(self, request):
        """删除共享带宽
        :param request: Request instance for DeleteBandWidthShare.
        :type request: :class:`ksyun.client.bws.v20160304.models.DeleteBandWidthShareRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteBandWidthShare", params, "application/x-www-form-urlencoded")
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

    def QueryBwsTopEipMonitor(self, request):
        """查询BWS下EIP流量排名的TOP 50的网卡
        :param request: Request instance for QueryBwsTopEipMonitor.
        :type request: :class:`ksyun.client.bws.v20160304.models.QueryBwsTopEipMonitorRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("QueryBwsTopEipMonitor", params, "application/x-www-form-urlencoded")
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
