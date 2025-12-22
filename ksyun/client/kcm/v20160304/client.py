import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class KcmClient(AbstractClient):
    _apiVersion = '2016-03-04'
    _endpoint = 'kcm.api.ksyun.com'
    _service = 'kcm'
    def CreateCertificate(self, request):
        """创建负载均衡证书
        :param request: Request instance for CreateCertificate.
        :type request: :class:`ksyun.client.kcm.v20160304.models.CreateCertificateRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateCertificate", params, "application/x-www-form-urlencoded")
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


    def DeleteCertificate(self, request):
        """删除SLB证书
        :param request: Request instance for DeleteCertificate.
        :type request: :class:`ksyun.client.kcm.v20160304.models.DeleteCertificateRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteCertificate", params, "application/x-www-form-urlencoded")
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


    def ModifyCertificate(self, request):
        """更新证书信息
        :param request: Request instance for ModifyCertificate.
        :type request: :class:`ksyun.client.kcm.v20160304.models.ModifyCertificateRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyCertificate", params, "application/x-www-form-urlencoded")
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


    def DescribeCertificates(self, request):
        """描述SLB证书
        :param request: Request instance for DescribeCertificates.
        :type request: :class:`ksyun.client.kcm.v20160304.models.DescribeCertificatesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeCertificates", params, "application/x-www-form-urlencoded")
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


    def ApplyCertificate(self, request):
        """申请证书
        :param request: Request instance for ApplyCertificate.
        :type request: :class:`ksyun.client.kcm.v20160304.models.ApplyCertificateRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ApplyCertificate", params, "application/x-www-form-urlencoded")
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


    def UpdateCertificate(self, request):
        """更新/补全证书信息
        :param request: Request instance for UpdateCertificate.
        :type request: :class:`ksyun.client.kcm.v20160304.models.UpdateCertificateRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateCertificate", params, "application/x-www-form-urlencoded")
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


    def ReIssueCertificate(self, request):
        """重新签发签发
        :param request: Request instance for ReIssueCertificate.
        :type request: :class:`ksyun.client.kcm.v20160304.models.ReIssueCertificateRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ReIssueCertificate", params, "application/x-www-form-urlencoded")
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


    def CancelTransaction(self, request):
        """取消证书申请
        :param request: Request instance for CancelTransaction.
        :type request: :class:`ksyun.client.kcm.v20160304.models.CancelTransactionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CancelTransaction", params, "application/x-www-form-urlencoded")
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


    def ListCertificates(self, request):
        """描述证书
        :param request: Request instance for ListCertificates.
        :type request: :class:`ksyun.client.kcm.v20160304.models.ListCertificatesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListCertificates", params, "application/json")
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


    def GetCertificateDetail(self, request):
        """获取证书详情
        :param request: Request instance for GetCertificateDetail.
        :type request: :class:`ksyun.client.kcm.v20160304.models.GetCertificateDetailRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetCertificateDetail", params, "application/json")
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


