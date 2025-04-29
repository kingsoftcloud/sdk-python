import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class PdnsClient(AbstractClient):
    _apiVersion = '2016-03-04'
    _endpoint = 'pdns.api.ksyun.com'
    _service = 'pdns'

    def CreatePrivateDns(self, request):
        """创建内网DNS实例
        :param request: Request instance for CreatePrivateDns.
        :type request: :class:`ksyun.client.pdns.v20160304.models.CreatePrivateDnsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreatePrivateDns", params, "application/x-www-form-urlencoded")
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

    def DeletePrivateDns(self, request):
        """删除内网DNS实例
        :param request: Request instance for DeletePrivateDns.
        :type request: :class:`ksyun.client.pdns.v20160304.models.DeletePrivateDnsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeletePrivateDns", params, "application/x-www-form-urlencoded")
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

    def DescribePrivateDns(self, request):
        """描述内网DNS实例
        :param request: Request instance for DescribePrivateDns.
        :type request: :class:`ksyun.client.pdns.v20160304.models.DescribePrivateDnsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribePrivateDns", params, "application/x-www-form-urlencoded")
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

    def AssociateVpcs(self, request):
        """关联VPC
        :param request: Request instance for AssociateVpcs.
        :type request: :class:`ksyun.client.pdns.v20160304.models.AssociateVpcsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AssociateVpcs", params, "application/x-www-form-urlencoded")
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

    def DisassociateVpcs(self, request):
        """解绑VPC
        :param request: Request instance for DisassociateVpcs.
        :type request: :class:`ksyun.client.pdns.v20160304.models.DisassociateVpcsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DisassociateVpcs", params, "application/x-www-form-urlencoded")
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

    def CreateZone(self, request):
        """创建Zone
        :param request: Request instance for CreateZone.
        :type request: :class:`ksyun.client.pdns.v20160304.models.CreateZoneRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateZone", params, "application/x-www-form-urlencoded")
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

    def DeleteZone(self, request):
        """删除Zone
        :param request: Request instance for DeleteZone.
        :type request: :class:`ksyun.client.pdns.v20160304.models.DeleteZoneRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteZone", params, "application/x-www-form-urlencoded")
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

    def ModifyZone(self, request):
        """修改Zone
        :param request: Request instance for ModifyZone.
        :type request: :class:`ksyun.client.pdns.v20160304.models.ModifyZoneRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyZone", params, "application/x-www-form-urlencoded")
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

    def DescribeZone(self, request):
        """描述Zone
        :param request: Request instance for DescribeZone.
        :type request: :class:`ksyun.client.pdns.v20160304.models.DescribeZoneRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeZone", params, "application/x-www-form-urlencoded")
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

    def CreateRecord(self, request):
        """添加解析记录
        :param request: Request instance for CreateRecord.
        :type request: :class:`ksyun.client.pdns.v20160304.models.CreateRecordRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateRecord", params, "application/x-www-form-urlencoded")
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

    def DeleteRecord(self, request):
        """删除解析记录
        :param request: Request instance for DeleteRecord.
        :type request: :class:`ksyun.client.pdns.v20160304.models.DeleteRecordRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteRecord", params, "application/x-www-form-urlencoded")
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

    def ModifyRecord(self, request):
        """修改解析记录
        :param request: Request instance for ModifyRecord.
        :type request: :class:`ksyun.client.pdns.v20160304.models.ModifyRecordRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyRecord", params, "application/x-www-form-urlencoded")
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

    def DescribeRecord(self, request):
        """描述解析记录
        :param request: Request instance for DescribeRecord.
        :type request: :class:`ksyun.client.pdns.v20160304.models.DescribeRecordRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeRecord", params, "application/x-www-form-urlencoded")
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

    def CreateRecordData(self, request):
        """添加记录值
        :param request: Request instance for CreateRecordData.
        :type request: :class:`ksyun.client.pdns.v20160304.models.CreateRecordDataRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateRecordData", params, "application/x-www-form-urlencoded")
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

    def DeleteRecordData(self, request):
        """删除记录值
        :param request: Request instance for DeleteRecordData.
        :type request: :class:`ksyun.client.pdns.v20160304.models.DeleteRecordDataRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteRecordData", params, "application/x-www-form-urlencoded")
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

    def CreatePdnsZone(self, request):
        """创建内网DNSzone
        :param request: Request instance for CreatePdnsZone.
        :type request: :class:`ksyun.client.pdns.v20160304.models.CreatePdnsZoneRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreatePdnsZone", params, "application/x-www-form-urlencoded")
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

    def ModifyPdnsZone(self, request):
        """修改Zone的ttl
        :param request: Request instance for ModifyPdnsZone.
        :type request: :class:`ksyun.client.pdns.v20160304.models.ModifyPdnsZoneRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyPdnsZone", params, "application/x-www-form-urlencoded")
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

    def DeletePdnsZone(self, request):
        """删除Zone-二期
        :param request: Request instance for DeletePdnsZone.
        :type request: :class:`ksyun.client.pdns.v20160304.models.DeletePdnsZoneRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeletePdnsZone", params, "application/x-www-form-urlencoded")
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

    def DescribePdnsZones(self, request):
        """查询Zone-二期
        :param request: Request instance for DescribePdnsZones.
        :type request: :class:`ksyun.client.pdns.v20160304.models.DescribePdnsZonesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribePdnsZones", params, "application/x-www-form-urlencoded")
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

    def BindZoneVpc(self, request):
        """为Zone绑定VPC
        :param request: Request instance for BindZoneVpc.
        :type request: :class:`ksyun.client.pdns.v20160304.models.BindZoneVpcRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("BindZoneVpc", params, "application/x-www-form-urlencoded")
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

    def UnbindZoneVpc(self, request):
        """Zone解绑VPC
        :param request: Request instance for UnbindZoneVpc.
        :type request: :class:`ksyun.client.pdns.v20160304.models.UnbindZoneVpcRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UnbindZoneVpc", params, "application/x-www-form-urlencoded")
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

    def CreateZoneRecord(self, request):
        """创建Zone解析记录-二期
        :param request: Request instance for CreateZoneRecord.
        :type request: :class:`ksyun.client.pdns.v20160304.models.CreateZoneRecordRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateZoneRecord", params, "application/x-www-form-urlencoded")
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

    def DeleteZoneRecord(self, request):
        """删除Zone解析记录
        :param request: Request instance for DeleteZoneRecord.
        :type request: :class:`ksyun.client.pdns.v20160304.models.DeleteZoneRecordRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteZoneRecord", params, "application/x-www-form-urlencoded")
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

    def ModifyZoneRecord(self, request):
        """修改Zone解析记录
        :param request: Request instance for ModifyZoneRecord.
        :type request: :class:`ksyun.client.pdns.v20160304.models.ModifyZoneRecordRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyZoneRecord", params, "application/x-www-form-urlencoded")
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

    def DescribeZoneRecord(self, request):
        """查询Zone解析记录 - 二期
        :param request: Request instance for DescribeZoneRecord.
        :type request: :class:`ksyun.client.pdns.v20160304.models.DescribeZoneRecordRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeZoneRecord", params, "application/x-www-form-urlencoded")
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
