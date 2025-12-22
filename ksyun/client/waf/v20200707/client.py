import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class WafClient(AbstractClient):
    _apiVersion = '2020-07-07'
    _endpoint = 'waf.api.ksyun.com'
    _service = 'waf'
    def CreateWaf(self, request):
        """创建waf（3.0）
        :param request: Request instance for CreateWaf.
        :type request: :class:`ksyun.client.waf.v20200707.models.CreateWafRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateWaf", params, "application/x-www-form-urlencoded")
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


    def DeleteWaf(self, request):
        """删除waf（3.0）
        :param request: Request instance for DeleteWaf.
        :type request: :class:`ksyun.client.waf.v20200707.models.DeleteWafRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteWaf", params, "application/x-www-form-urlencoded")
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


    def CreateDomain(self, request):
        """创建域名（3.0）
        :param request: Request instance for CreateDomain.
        :type request: :class:`ksyun.client.waf.v20200707.models.CreateDomainRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateDomain", params, "application/x-www-form-urlencoded")
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


    def DescribeDomains(self, request):
        """描述域名（3.0）
        :param request: Request instance for DescribeDomains.
        :type request: :class:`ksyun.client.waf.v20200707.models.DescribeDomainsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDomains", params, "application/x-www-form-urlencoded")
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


    def ModifyDomain(self, request):
        """修改域名（3.0）
        :param request: Request instance for ModifyDomain.
        :type request: :class:`ksyun.client.waf.v20200707.models.ModifyDomainRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyDomain", params, "application/x-www-form-urlencoded")
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


    def DeleteDomain(self, request):
        """删除域名（3.0）
        :param request: Request instance for DeleteDomain.
        :type request: :class:`ksyun.client.waf.v20200707.models.DeleteDomainRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteDomain", params, "application/x-www-form-urlencoded")
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


    def CreateAccessControlRule(self, request):
        """创建访问控制规则（3.0）
        :param request: Request instance for CreateAccessControlRule.
        :type request: :class:`ksyun.client.waf.v20200707.models.CreateAccessControlRuleRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateAccessControlRule", params, "application/x-www-form-urlencoded")
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


    def DescribeAccessControlRules(self, request):
        """描述访问控制规则（3.0）
        :param request: Request instance for DescribeAccessControlRules.
        :type request: :class:`ksyun.client.waf.v20200707.models.DescribeAccessControlRulesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeAccessControlRules", params, "application/x-www-form-urlencoded")
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


    def ModifyAccessControlRule(self, request):
        """修改访问控制规则（3.0）
        :param request: Request instance for ModifyAccessControlRule.
        :type request: :class:`ksyun.client.waf.v20200707.models.ModifyAccessControlRuleRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyAccessControlRule", params, "application/x-www-form-urlencoded")
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


    def DeleteAccessControlRule(self, request):
        """删除访问控制规则（3.0）
        :param request: Request instance for DeleteAccessControlRule.
        :type request: :class:`ksyun.client.waf.v20200707.models.DeleteAccessControlRuleRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteAccessControlRule", params, "application/x-www-form-urlencoded")
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
        """描述证书信息（3.0）
        :param request: Request instance for DescribeCertificates.
        :type request: :class:`ksyun.client.waf.v20200707.models.DescribeCertificatesRequest`
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


    def CreateIpv6Protection(self, request):
        """开启IPv6防护（3.0）
        :param request: Request instance for CreateIpv6Protection.
        :type request: :class:`ksyun.client.waf.v20200707.models.CreateIpv6ProtectionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateIpv6Protection", params, "application/x-www-form-urlencoded")
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


    def DeleteIpv6Protection(self, request):
        """关闭IPv6防护（3.0）
        :param request: Request instance for DeleteIpv6Protection.
        :type request: :class:`ksyun.client.waf.v20200707.models.DeleteIpv6ProtectionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteIpv6Protection", params, "application/x-www-form-urlencoded")
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


    def ModifyStorageTime(self, request):
        """修改日志存储时长（3.0）
        :param request: Request instance for ModifyStorageTime.
        :type request: :class:`ksyun.client.waf.v20200707.models.ModifyStorageTimeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyStorageTime", params, "application/x-www-form-urlencoded")
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


    def CreateAlbDomain(self, request):
        """创建域名(alb-waf)
        :param request: Request instance for CreateAlbDomain.
        :type request: :class:`ksyun.client.waf.v20200707.models.CreateAlbDomainRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateAlbDomain", params, "application/x-www-form-urlencoded")
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


    def ModifyAlbDomain(self, request):
        """修改域名
        :param request: Request instance for ModifyAlbDomain.
        :type request: :class:`ksyun.client.waf.v20200707.models.ModifyAlbDomainRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyAlbDomain", params, "application/x-www-form-urlencoded")
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


    def DeleteAlbDomain(self, request):
        """删除域名(alb-waf)
        :param request: Request instance for DeleteAlbDomain.
        :type request: :class:`ksyun.client.waf.v20200707.models.DeleteAlbDomainRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteAlbDomain", params, "application/x-www-form-urlencoded")
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


    def CreateAlbWaf(self, request):
        """创建waf(alb-waf)
        :param request: Request instance for CreateAlbWaf.
        :type request: :class:`ksyun.client.waf.v20200707.models.CreateAlbWafRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateAlbWaf", params, "application/x-www-form-urlencoded")
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


    def ModifyAlbWaf(self, request):
        """修改waf实例(alb-waf)
        :param request: Request instance for ModifyAlbWaf.
        :type request: :class:`ksyun.client.waf.v20200707.models.ModifyAlbWafRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyAlbWaf", params, "application/x-www-form-urlencoded")
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


    def DescribeAlbDomains(self, request):
        """描述域名
        :param request: Request instance for DescribeAlbDomains.
        :type request: :class:`ksyun.client.waf.v20200707.models.DescribeAlbDomainsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeAlbDomains", params, "application/x-www-form-urlencoded")
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


