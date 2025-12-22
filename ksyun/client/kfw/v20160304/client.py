import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class KfwClient(AbstractClient):
    _apiVersion = '2016-03-04'
    _endpoint = 'kfw.api.ksyun.com'
    _service = 'kfw'
    def DescribeCfwAv(self, request):
        """查询防病毒
        :param request: Request instance for DescribeCfwAv.
        :type request: :class:`ksyun.client.kfw.v20160304.models.DescribeCfwAvRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeCfwAv", params, "application/x-www-form-urlencoded")
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


    def DeleteBatchCfwAddrbook(self, request):
        """批量删除地址簿
        :param request: Request instance for DeleteBatchCfwAddrbook.
        :type request: :class:`ksyun.client.kfw.v20160304.models.DeleteBatchCfwAddrbookRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteBatchCfwAddrbook", params, "application/x-www-form-urlencoded")
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


