import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class EipClient(AbstractClient):
    _apiVersion = '2016-03-04'
    _endpoint = 'eip.api.ksyun.com'
    _service = 'eip'
    def GetLines(self, request):
        """获取用户可选链路信息
        :param request: Request instance for GetLines.
        :type request: :class:`ksyun.client.eip.v20160304.models.GetLinesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetLines", params, "application/x-www-form-urlencoded")
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


    def DescribeAddresses(self, request):
        """描述EIP
        :param request: Request instance for DescribeAddresses.
        :type request: :class:`ksyun.client.eip.v20160304.models.DescribeAddressesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeAddresses", params, "application/x-www-form-urlencoded")
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


    def AllocateAddress(self, request):
        """创建EIP
        :param request: Request instance for AllocateAddress.
        :type request: :class:`ksyun.client.eip.v20160304.models.AllocateAddressRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AllocateAddress", params, "application/x-www-form-urlencoded")
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


    def ReleaseAddress(self, request):
        """删除EIP
        :param request: Request instance for ReleaseAddress.
        :type request: :class:`ksyun.client.eip.v20160304.models.ReleaseAddressRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ReleaseAddress", params, "application/x-www-form-urlencoded")
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


    def AssociateAddress(self, request):
        """绑定弹性IP
        :param request: Request instance for AssociateAddress.
        :type request: :class:`ksyun.client.eip.v20160304.models.AssociateAddressRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AssociateAddress", params, "application/x-www-form-urlencoded")
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


    def DisassociateAddress(self, request):
        """解绑弹性IP
        :param request: Request instance for DisassociateAddress.
        :type request: :class:`ksyun.client.eip.v20160304.models.DisassociateAddressRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DisassociateAddress", params, "application/x-www-form-urlencoded")
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


    def ModifyAddress(self, request):
        """更新弹性IP配置
        :param request: Request instance for ModifyAddress.
        :type request: :class:`ksyun.client.eip.v20160304.models.ModifyAddressRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyAddress", params, "application/x-www-form-urlencoded")
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


